#!/usr/bin/env python3
"""
Wiki Markdown Exporter — 将 Notion 知识 Wiki 数据库导出为本地 Markdown 文件系统。

用法：
  python export.py --full                          # 首次全量导出
  python export.py --incremental                   # 增量同步（从 sync_state.json 读上次时间）
  python export.py --index-only                    # 只重建 index.md
"""

import argparse
import json
import os
import re
import sys
import time
import unicodedata
from datetime import datetime, timezone
from zoneinfo import ZoneInfo
from pathlib import Path

import requests
import yaml

# ── 配置 ──────────────────────────────────────────────

NOTION_TOKEN = os.environ.get("NOTION_TOKEN", "") or open(
    os.path.expanduser("~/.config/notion/api_key")
).read().strip()

DATABASE_ID = "f98c88d3-d587-494a-98ff-92fbaf9228c4"
GITHUB_REPO = "6tizer/wiki-export"
TYPE_TO_DIR = {"concept": "concepts", "entity": "entities", "synthesis": "syntheses", "summary": "summaries"}
OUTPUT_DIR = Path(os.environ.get("OUTPUT_DIR", "./wiki-export"))
TZ = ZoneInfo("Asia/Shanghai")
HTTP_PROXY = os.environ.get("HTTP_PROXY") or os.environ.get("http_proxy") or None
REQUEST_PROXIES = {"https": HTTP_PROXY, "http": HTTP_PROXY} if HTTP_PROXY else None

NOTION_API = "https://api.notion.com/v1"
NOTION_HEADERS = {
    "Authorization": f"Bearer {NOTION_TOKEN}",
    "Notion-Version": "2022-06-28",
    "Content-Type": "application/json",
}


def get_type_dir(page_type: str) -> str:
    """获取类型对应的子目录，已知类型用映射，未知类型直接用类型名。"""
    return TYPE_TO_DIR.get(page_type, page_type)

# 文件名非法字符映射
FILENAME_REPLACEMENTS = {
    "/": "-", ":": "-", "\\": "-", "*": "", "?": "", '"': "",
    "<": "", ">": "", "|": "",
}

# ── 限速器 ────────────────────────────────────────────


class RateLimiter:
    """Token bucket 限速器，2.5 req/s，支持 429 重试 + 指数退避。"""

    def __init__(self, rate: float = 2.5, max_retries: int = 5):
        self.rate = rate
        self.interval = 1.0 / rate
        self.last_request = 0.0
        self.max_retries = max_retries

    def wait(self):
        now = time.monotonic()
        elapsed = now - self.last_request
        if elapsed < self.interval:
            time.sleep(self.interval - elapsed)
        self.last_request = time.monotonic()

    def request(self, method: str, url: str, **kwargs) -> requests.Response:
        for attempt in range(self.max_retries):
            self.wait()
            try:
                resp = requests.request(method, url, headers=NOTION_HEADERS, proxies=REQUEST_PROXIES, **kwargs)
            except (requests.exceptions.SSLError,
                    requests.exceptions.ConnectionError,
                    requests.exceptions.Timeout) as e:
                backoff = min(2 ** attempt, 30)
                print(f"  ⚠️ 连接错误: {type(e).__name__}，等待 {backoff}s (attempt {attempt+1}/{self.max_retries})")
                time.sleep(backoff)
                continue

            if resp.status_code == 429:
                retry_after = float(resp.headers.get("Retry-After", 1))
                backoff = min(retry_after, 30)
                print(f"  ⏳ 429 限速，等待 {backoff:.1f}s (attempt {attempt+1}/{self.max_retries})")
                time.sleep(backoff)
                continue

            if resp.status_code >= 500:
                backoff = min(2 ** attempt, 30)
                print(f"  ⚠️ 服务器错误 {resp.status_code}，等待 {backoff}s (attempt {attempt+1}/{self.max_retries})")
                time.sleep(backoff)
                continue

            return resp

        raise RuntimeError(f"请求失败，已重试 {self.max_retries} 次: {url}")


limiter = RateLimiter()

# ── Notion API 封装 ───────────────────────────────────


def query_database(database_id: str, filter_obj: dict | None = None,
                   sorts: list | None = None, page_size: int = 100) -> list[dict]:
    """分页查询数据库，返回所有 results。"""
    all_results = []
    start_cursor = None

    while True:
        body: dict = {"page_size": page_size}
        if filter_obj:
            body["filter"] = filter_obj
        if sorts:
            body["sorts"] = sorts
        if start_cursor:
            body["start_cursor"] = start_cursor

        resp = limiter.request("POST", f"{NOTION_API}/databases/{database_id}/query", json=body)
        data = resp.json()
        all_results.extend(data.get("results", []))

        if not data.get("has_more"):
            break
        start_cursor = data.get("next_cursor")
        print(f"  📄 已获取 {len(all_results)} 条...")

    return all_results


def get_block_children(block_id: str) -> list[dict]:
    """获取 block 的所有子 blocks（自动分页）。"""
    all_blocks = []
    start_cursor = None

    while True:
        url = f"{NOTION_API}/blocks/{block_id}/children?page_size=100"
        if start_cursor:
            url += f"&start_cursor={start_cursor}"

        resp = limiter.request("GET", url)
        data = resp.json()
        all_blocks.extend(data.get("results", []))

        if not data.get("has_more"):
            break
        start_cursor = data.get("next_cursor")

    return all_blocks


def get_page(page_id: str) -> dict:
    """获取页面属性。"""
    resp = limiter.request("GET", f"{NOTION_API}/pages/{page_id}")
    return resp.json()

# ── 文件名清理 ────────────────────────────────────────


def sanitize_filename(name: str) -> str:
    """清理文件名中的非法字符。"""
    for old, new in FILENAME_REPLACEMENTS.items():
        name = name.replace(old, new)
    # 去除首尾空格和点号
    name = name.strip().strip(".")
    return name

# ── 属性提取 ──────────────────────────────────────────


def extract_title(page: dict) -> str:
    """从页面属性中提取标题。"""
    props = page.get("properties", {})
    for prop_name, prop_val in props.items():
        if prop_val.get("type") == "title":
            title_list = prop_val.get("title", [])
            if title_list:
                return "".join(t.get("plain_text", "") for t in title_list)
    return ""


def extract_select(page: dict, prop_name: str) -> str:
    """提取 select 属性值。"""
    prop = page.get("properties", {}).get(prop_name, {})
    if prop.get("type") == "select" and prop.get("select"):
        return prop["select"].get("name", "")
    return ""


def extract_multi_select(page: dict, prop_name: str) -> list[str]:
    """提取 multi_select 属性值。"""
    prop = page.get("properties", {}).get(prop_name, {})
    if prop.get("type") == "multi_select":
        return [item.get("name", "") for item in prop.get("multi_select", [])]
    return []


def extract_status(page: dict, prop_name: str) -> str:
    """提取 status 属性值。"""
    prop = page.get("properties", {}).get(prop_name, {})
    if prop.get("type") == "status" and prop.get("status"):
        return prop["status"].get("name", "")
    return ""


def extract_date(page: dict, prop_name: str) -> str:
    """提取 date 属性的 start 部分。"""
    prop = page.get("properties", {}).get(prop_name, {})
    if prop.get("type") == "date" and prop.get("date"):
        return prop["date"].get("start", "")[:10]  # 只取日期部分
    return ""


def extract_rich_text_prop(page: dict, prop_name: str) -> str:
    """提取 rich_text 属性值。"""
    prop = page.get("properties", {}).get(prop_name, {})
    if prop.get("type") == "rich_text":
        return "".join(t.get("plain_text", "") for t in prop.get("rich_text", []))
    return ""


def extract_url_prop(page: dict, prop_name: str) -> str:
    """提取 url 属性值。"""
    prop = page.get("properties", {}).get(prop_name, {})
    if prop.get("type") == "url":
        return prop.get("url", "") or ""
    return ""


def page_id_to_notion_url(page_id: str) -> str:
    """将 page_id 转为 Notion URL。"""
    clean_id = page_id.replace("-", "")
    return f"https://www.notion.so/{clean_id}"

# ── Block → Markdown 转换 ─────────────────────────────


def rich_text_to_markdown(rich_text_list: list[dict], page_map: dict[str, str] | None = None) -> str:
    """将 Notion rich_text 数组转换为 Markdown 文本。"""
    if not rich_text_list:
        return ""

    parts = []
    for rt in rich_text_list:
        text = rt.get("plain_text", "")
        annotations = rt.get("annotations", {})
        href = rt.get("href")
        rt_type = rt.get("type", "")

        # mention 类型特殊处理
        if rt_type == "mention":
            mention = rt.get("mention", {})
            mention_type = mention.get("type", "")

            if mention_type == "page" and page_map:
                mentioned_id = mention.get("page", {}).get("id", "")
                # 尝试带连字符和不带连字符两种格式
                mapped_path = page_map.get(mentioned_id) or page_map.get(mentioned_id.replace("-", ""))
                if mapped_path:
                    # 获取页面名称（从 plain_text）
                    name = text
                    parts.append(f"[{name}]({mapped_path})")
                    continue

            # 其他 mention 类型或未在映射表中 → 保留纯文本
            parts.append(text)
            continue

        # 应用格式注解
        if annotations.get("code"):
            text = f"`{text}`"
        if annotations.get("strikethrough"):
            text = f"~~{text}~~"
        if annotations.get("italic"):
            text = f"*{text}*"
        if annotations.get("bold"):
            text = f"**{text}**"

        # 链接
        if href:
            text = f"[{text}]({href})"

        parts.append(text)

    return "".join(parts)


def block_to_markdown(block: dict, page_map: dict[str, str] | None = None, indent: int = 0) -> str:
    """将单个 Notion block 转换为 Markdown 文本。"""
    btype = block.get("type", "")
    d = block.get(btype, {})
    prefix = "  " * indent

    # 含 rich_text 的类型
    if "rich_text" in d:
        text = rich_text_to_markdown(d["rich_text"], page_map)

        if btype == "heading_1":
            return f"# {text}"
        elif btype == "heading_2":
            return f"## {text}"
        elif btype == "heading_3":
            return f"### {text}"
        elif btype == "paragraph":
            return f"{prefix}{text}"
        elif btype == "bulleted_list_item":
            return f"{prefix}- {text}"
        elif btype == "numbered_list_item":
            return f"{prefix}1. {text}"
        elif btype == "to_do":
            checked = d.get("checked", False)
            checkbox = "[x]" if checked else "[ ]"
            return f"{prefix}- {checkbox} {text}"
        elif btype == "quote":
            return f"{prefix}> {text}"
        elif btype == "callout":
            icon = d.get("icon", {})
            emoji = icon.get("emoji", "") if icon.get("type") == "emoji" else ""
            return f"{prefix}> **{emoji}** {text}"
        elif btype == "toggle":
            return f"{prefix}<details><summary>{text}</summary>"
        elif btype == "code":
            lang = d.get("language", "")
            return f"{prefix}```{lang}\n{text}\n{prefix}```"
        else:
            return f"{prefix}{text}"

    # 表格
    if btype == "table":
        return ""  # 表格内容通过子 blocks 处理

    if btype == "table_row":
        cells = d.get("cells", [])
        row_parts = []
        for cell in cells:
            cell_text = rich_text_to_markdown(cell, page_map)
            row_parts.append(cell_text)
        return f"{prefix}| {' | '.join(row_parts)} |"

    # 其他类型
    if btype == "divider":
        return "---"
    if btype == "bookmark":
        url = d.get("url", "")
        caption = rich_text_to_markdown(d.get("caption", []), page_map)
        title = caption or url
        return f"[{title}]({url})"
    if btype == "image":
        url = _get_media_url(d)
        caption = rich_text_to_markdown(d.get("caption", []), page_map)
        alt = caption or "image"
        return f"![{alt}]({url})"
    if btype in ("video", "file", "pdf", "embed"):
        url = _get_media_url(d)
        return f"[media]({url})"
    if btype == "link_to_page":
        page_id = d.get("page_id", "")
        if page_map:
            mapped = page_map.get(page_id) or page_map.get(page_id.replace("-", ""))
            if mapped:
                return f"[→ 关联页面]({mapped})"
        return ""
    if btype == "child_page":
        title = d.get("title", "")
        return f"{prefix}**{title}**"
    if btype == "equation":
        expr = block.get("equation", {}).get("expression", "")
        return f"$${expr}$$"
    if btype == "table_of_contents":
        return ""
    if btype == "breadcrumb":
        return ""

    return ""


def _get_media_url(d: dict) -> str:
    """从媒体 block 中提取 URL。"""
    if d.get("external"):
        return d["external"].get("url", "")
    if d.get("file"):
        return d["file"].get("url", "")
    if d.get("url"):
        return d["url"]
    return ""


def convert_blocks_to_markdown(blocks: list[dict], page_map: dict[str, str] | None = None,
                                indent: int = 0) -> str:
    """将 block 列表转换为 Markdown 文本，递归处理子 blocks。"""
    lines = []
    in_table = False
    table_has_header = False

    for block in blocks:
        btype = block.get("type", "")

        # 表格处理：收集 table + table_row blocks
        if btype == "table":
            table_has_header = d_get(block, "table.has_column_header", False)
            # 获取子 blocks（table_row）
            if block.get("has_children"):
                children = get_block_children(block["id"])
                table_lines = []
                for i, child in enumerate(children):
                    row_md = block_to_markdown(child, page_map, indent)
                    if row_md:
                        table_lines.append(row_md)
                    # 第一行后加分隔线
                    if i == 0 and table_has_header:
                        cell_count = len(child.get("table_row", {}).get("cells", []))
                        table_lines.append(f"{'  ' * indent}| {' | '.join(['---'] * cell_count)} |")
                lines.extend(table_lines)
            in_table = False
            continue

        if btype == "table_row":
            # 独立的 table_row（不在 table 下，理论上不该出现）
            row_md = block_to_markdown(block, page_map, indent)
            if row_md:
                lines.append(row_md)
            continue

        # 普通 block
        md = block_to_markdown(block, page_map, indent)
        if md:
            lines.append(md)

        # 递归处理子 blocks
        if block.get("has_children") and btype not in ("table",):
            children = get_block_children(block["id"])
            child_md = convert_blocks_to_markdown(children, page_map, indent + 1)
            if child_md:
                lines.append(child_md)
            # toggle 关闭标签
            if btype == "toggle":
                lines.append(f"{'  ' * indent}</details>")

    return "\n\n".join(lines)


def d_get(obj: dict, path: str, default=None):
    """安全获取嵌套字典值，路径用点分隔。"""
    keys = path.split(".")
    current = obj
    for key in keys:
        if isinstance(current, dict):
            current = current.get(key)
        else:
            return default
        if current is None:
            return default
    return current

# ── 映射表构建 ────────────────────────────────────────


def build_page_map(pages: list[dict]) -> dict[str, str]:
    """构建 page_id → 相对文件路径的映射。

    返回格式: {page_id: "concepts/Mem0.md"}
    """
    page_map = {}
    for page in pages:
        page_id = page["id"]
        page_type = extract_select(page, "类型")
        title = extract_title(page)

        if not page_type:
            continue

        filename = sanitize_filename(title) if title else page_id[:8]
        filename = f"{filename}.md"

        type_dir = get_type_dir(page_type)
        relative_path = f"{type_dir}/{filename}"

        # 同时存储带连字符和不带连字符的版本
        page_map[page_id] = relative_path
        page_map[page_id.replace("-", "")] = relative_path

    return page_map

# ── sync_state.json 管理 ────────────────────────────────


SYNC_STATE_FILE = "sync_state.json"


def load_sync_state() -> dict:
    """加载 sync_state.json。"""
    path = OUTPUT_DIR / SYNC_STATE_FILE
    if path.exists():
        return json.loads(path.read_text(encoding="utf-8"))
    return {}


def save_sync_state(state: dict):
    """保存 sync_state.json。"""
    path = OUTPUT_DIR / SYNC_STATE_FILE
    path.write_text(json.dumps(state, ensure_ascii=False, indent=2), encoding="utf-8")


def build_sync_state(pages: list[dict], page_map: dict[str, str]) -> dict:
    """从页面列表构建完整的 sync_state。"""
    now_utc = datetime.now(timezone.utc)
    now_local = now_utc.astimezone(TZ)

    page_mapping = {}
    for page in pages:
        page_id = page["id"]
        page_type = extract_select(page, "类型")
        if not page_type:
            continue
        rel_path = page_map.get(page_id, "")
        if not rel_path:
            continue
        page_mapping[page_id] = {
            "type": page_type,
            "file_path": f"wiki/{rel_path}",
            "last_edited": page.get("last_edited_time", ""),
        }

    return {
        "last_sync_time": now_local.isoformat(),
        "last_full_export_time": now_local.isoformat(),
        "total_pages_exported": len(page_mapping),
        "page_mapping": page_mapping,
    }


def update_sync_state(state: dict, pages: list[dict], page_map: dict[str, str]):
    """增量更新 sync_state（只更新变更部分）。"""
    now_utc = datetime.now(timezone.utc)
    now_local = now_utc.astimezone(TZ)

    if "page_mapping" not in state:
        state["page_mapping"] = {}

    for page in pages:
        page_id = page["id"]
        page_type = extract_select(page, "类型")
        if not page_type:
            continue
        rel_path = page_map.get(page_id, "")
        if not rel_path:
            continue
        state["page_mapping"][page_id] = {
            "type": page_type,
            "file_path": f"wiki/{rel_path}",
            "last_edited": page.get("last_edited_time", ""),
        }

    state["last_sync_time"] = now_local.isoformat()
    state["total_pages_exported"] = len(state["page_mapping"])


# ── 断点续传（用于 --full 的 exported_pages.json）───────


def load_exported() -> set[str]:
    """加载已导出的 page_id 列表。"""
    progress_file = OUTPUT_DIR / "exported_pages.json"
    if progress_file.exists():
        data = json.loads(progress_file.read_text())
        return set(data.get("exported", []))
    return set()


def save_exported(exported: set[str]):
    """保存已导出的 page_id 列表。"""
    progress_file = OUTPUT_DIR / "exported_pages.json"
    progress_file.write_text(json.dumps({"exported": sorted(exported)}, ensure_ascii=False, indent=2))


# ── 单页导出 ──────────────────────────────────────────


def export_page(page: dict, page_map: dict[str, str], exported: set[str]) -> bool:
    """导出单个页面为 Markdown 文件。"""
    page_id = page["id"]
    page_type = extract_select(page, "类型")
    title = extract_title(page)

    if not page_type:
        return False

    # 断点续传：跳过已导出的
    if page_id in exported:
        return True

    # 获取页面内容
    blocks = get_block_children(page_id)
    content_md = convert_blocks_to_markdown(blocks, page_map)

    # 构建 frontmatter
    tags = extract_multi_select(page, "标签")
    status = extract_status(page, "状态")
    confidence = extract_select(page, "置信度")
    last_compiled = extract_date(page, "最后编译时间")
    source_tags = extract_rich_text_prop(page, "来源标签")
    source_url = extract_url_prop(page, "源文章URL")

    frontmatter = {
        "title": title,
        "type": page_type,
        "tags": tags,
        "status": status,
        "confidence": confidence,
        "last_compiled": last_compiled,
        "source_tags": source_tags,
        "source_article_url": source_url,
        "notion_url": page_id_to_notion_url(page_id),
        "notion_id": page_id,
    }

    # 写文件
    filename = sanitize_filename(title) if title else page_id[:8]
    filename = f"{filename}.md"
    type_dir = OUTPUT_DIR / "wiki" / get_type_dir(page_type)
    type_dir.mkdir(parents=True, exist_ok=True)

    file_path = type_dir / filename

    # 组装最终内容
    yaml_str = yaml.dump(frontmatter, allow_unicode=True, default_flow_style=False, sort_keys=False)
    full_content = f"---\n{yaml_str}---\n\n{content_md}\n"

    file_path.write_text(full_content, encoding="utf-8")
    exported.add(page_id)

    return True

# ── index.md 生成 ─────────────────────────────────────


def generate_index(pages: list[dict], page_map: dict[str, str]):
    """生成 wiki/index.md。"""
    indexed = [p for p in pages if extract_select(p, "类型")]

    # 按标签分组
    tag_groups: dict[str, dict[str, list]] = {}
    for page in indexed:
        page_type = extract_select(page, "类型")
        title = extract_title(page)
        tags = extract_multi_select(page, "标签")
        page_id = page["id"]
        rel_path = page_map.get(page_id, "")

        for tag in tags:
            if tag not in tag_groups:
                tag_groups[tag] = {}
            if page_type not in tag_groups[tag]:
                tag_groups[tag][page_type] = []
            tag_groups[tag][page_type].append((title, rel_path))

    # 统计（动态按类型）
    type_counts: dict[str, int] = {}
    for p in indexed:
        t = extract_select(p, "类型")
        type_counts[t] = type_counts.get(t, 0) + 1

    now = datetime.now(TZ).strftime("%Y-%m-%d")

    type_summary = " · ".join(f"{v} {k}s" for k, v in sorted(type_counts.items()))

    lines = [
        "---",
        f"type: index",
        f"type_counts: {json.dumps(type_counts, ensure_ascii=False)}",
        f"total: {sum(type_counts.values())}",
        f"last_updated: {now}",
        "---",
        "",
        "# 📚 知识 Wiki Index",
        "",
        f"> {type_summary}",
        f"> 导出时间: {now}",
        "",
        "## 使用方式",
        "1. 搜索本文件定位感兴趣的条目名称",
        "2. 沿文件路径读取具体 .md 文件",
        "3. 沿关联概念的 wikilinks 跳转探索",
        "",
    ]

    # 按标签输出
    for tag in sorted(tag_groups.keys()):
        group = tag_groups[tag]
        lines.append(f"## {tag}")

        for ptype in sorted(group.keys()):
            items = group[ptype]
            if items:
                lines.append(f"### {ptype.capitalize()}s")
                for title, path in sorted(items, key=lambda x: x[0]):
                    lines.append(f"- [{title}]({path})")
                lines.append("")

    # 非 concept/entity 的类型单独列出
    non_core_types = [t for t in sorted(type_counts.keys()) if t not in ("concept", "entity")]
    for ntype in non_core_types:
        all_items = [(extract_title(p), page_map.get(p["id"], "")) for p in indexed if extract_select(p, "类型") == ntype]
        if all_items:
            lines.append(f"## {ntype.capitalize()}s（所有{ntype}）")
            for title, path in sorted(all_items, key=lambda x: x[0]):
                lines.append(f"- [{title}]({path})")

    index_path = OUTPUT_DIR / "wiki" / "index.md"
    index_path.parent.mkdir(parents=True, exist_ok=True)
    index_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    total_c = type_counts.get("concept", 0)
    total_e = type_counts.get("entity", 0)
    total_s = type_counts.get("synthesis", 0)
    print(f"✅ 已生成 wiki/index.md ({total_c}C + {total_e}E + {total_s}S)")

# ── Schema 文件生成 ───────────────────────────────────


SCHEMA_CLAUDE_MD = """# Tizer's Knowledge Wiki

## 概述
这是一个 AI 编译的个人知识库，由 Notion AI Agent 集群自动编译维护。
包含 733 个核心概念（concept）、360 个实体档案（entity）、45 篇综合分析（synthesis）、777 篇单篇摘要（summary）。
知识来源：微信公众号、X/Twitter、技术博客、会议记录。

## 目录结构
- `schema/CLAUDE.md` — 你正在读的文件（入口）
- `schema/WIKI-SCHEMA.md` — 详细的类型定义和命名规范
- `wiki/index.md` — 全局目录（按标签分组，只列 concept/entity/synthesis）
- `wiki/concepts/` — 733 个核心概念
- `wiki/entities/` — 360 个实体档案
- `wiki/syntheses/` — 45 篇综合分析
- `wiki/summaries/` — 777 篇摘要（通过 concept 中的 wikilink 按需跳转）

## 查询流程
1. 先读 `wiki/index.md` 了解全局
2. 根据标签和名称定位目标文件
3. 读取 .md 文件的 YAML frontmatter 判断相关性
4. 读取正文获取详细内容
5. 沿 wikilinks（`[名称](路径)`）跳转探索关联概念

## 文件格式约定
- 每个 .md 文件包含 YAML frontmatter（title/type/tags/status/confidence）
- `notion_id` 字段用于反向追溯到 Notion 原始页面
- 优先引用 status=已审核 且 confidence=high 的条目
- 草稿条目内容可能不完整，引用时需标注

## 标签体系（14 个一级标签）
Agent 框架 · Agent 编排 · Agent 技能 · Coding Agent · LLM · 记忆系统 · OpenClaw · Crypto/DeFi · 知识管理 · 开发工具 · 工作流 · 安全/隐私 · 内容创作 · 商业/生态

## 写入规则（如果你需要更新知识库）
- 可以改写正文中分隔线（`---`）上方的「编译真相」区
- 分隔线下方的「来源引用」区只允许追加，不允许修改或删除
- 新增条目需遵循 schema/WIKI-SCHEMA.md 的命名规范
"""


def write_schema_claude_md():
    """写入 schema/CLAUDE.md。"""
    path = OUTPUT_DIR / "schema" / "CLAUDE.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(SCHEMA_CLAUDE_MD.strip() + "\n", encoding="utf-8")
    print("✅ 已生成 schema/CLAUDE.md")


def write_schema_wiki_schema():
    """写入 schema/WIKI-SCHEMA.md（从 Notion 读取的 Schema 规则）。"""
    schema_page_id = "5616b847-5113-4607-a28a-810ec9b26386"
    blocks = get_block_children(schema_page_id)
    content = convert_blocks_to_markdown(blocks)

    path = OUTPUT_DIR / "schema" / "WIKI-SCHEMA.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content + "\n", encoding="utf-8")
    print("✅ 已生成 schema/WIKI-SCHEMA.md")

# ── Git 操作 ──────────────────────────────────────────


def git_commit_and_push(message: str, force: bool = False):
    """Git add + commit + push。无变更时不提交。"""
    import subprocess

    wiki_dir = OUTPUT_DIR
    if not (wiki_dir / ".git").exists():
        subprocess.run(["git", "init"], cwd=wiki_dir, check=True)
        subprocess.run(["git", "remote", "add", "origin", f"git@github.com:{GITHUB_REPO}.git"],
                       cwd=wiki_dir, check=True, capture_output=True)

    subprocess.run(["git", "add", "-A"], cwd=wiki_dir, check=True)

    # 检查是否有变更
    result = subprocess.run(["git", "diff", "--cached", "--quiet"],
                            cwd=wiki_dir, capture_output=True)
    if result.returncode == 0:
        print("  ℹ️ 无变更，跳过提交")
        return False

    subprocess.run(["git", "commit", "-m", message], cwd=wiki_dir, check=True)

    push_cmd = ["git", "push", "-u", "origin", "main"]
    if force:
        push_cmd.append("--force")

    result = subprocess.run(push_cmd, cwd=wiki_dir, capture_output=True, text=True)
    if result.returncode != 0:
        # push 失败，尝试 pull --rebase 后重试
        print(f"  ⚠️ Push 失败，尝试 rebase...")
        rebase_result = subprocess.run(
            ["git", "pull", "--rebase", "origin", "main"],
            cwd=wiki_dir, capture_output=True, text=True
        )
        if rebase_result.returncode == 0:
            retry = subprocess.run(push_cmd, cwd=wiki_dir, capture_output=True, text=True)
            if retry.returncode != 0:
                print(f"  ❌ Rebase 后 push 仍失败: {retry.stderr.strip()}")
                return False
        else:
            print(f"  ❌ Rebase 失败: {rebase_result.stderr.strip()}")
            # rebase 失败时中止，避免残留状态
            subprocess.run(["git", "rebase", "--abort"], cwd=wiki_dir, capture_output=True)
            return False

    print(f"  ✅ 已推送到 {GITHUB_REPO}")
    return True

# ── 主流程 ────────────────────────────────────────────


def cmd_full(args):
    """全量导出。"""
    print("🚀 开始全量导出...")

    # 1. 查询数据库
    print("\n📥 步骤 1: 查询数据库...")
    filter_obj = {
        "property": "类型",
        "select": {"is_not_empty": True}
    }
    sorts = [
        {"property": "类型", "direction": "ascending"},
        {"property": "名称", "direction": "ascending"},
    ]
    all_pages = query_database(DATABASE_ID, filter_obj, sorts)

    pages = [p for p in all_pages if extract_select(p, "类型")]
    print(f"  共 {len(pages)} 个有效页面（过滤掉了 {len(all_pages) - len(pages)} 个无类型的）")

    # 2. 构建映射表
    print("\n🗺️  步骤 2: 构建映射表...")
    page_map = build_page_map(pages)
    print(f"  映射表条目: {len(page_map) // 2}")

    # 3. 逐页导出
    print("\n📝 步骤 3: 逐页导出...")
    exported = load_exported()
    print(f"  已导过 {len(exported)} 个页面")

    success = 0
    skipped = 0
    failed = 0

    for i, page in enumerate(pages):
        page_id = page["id"]
        title = extract_title(page)
        page_type = extract_select(page, "类型")

        if page_id in exported:
            skipped += 1
            continue

        try:
            export_page(page, page_map, exported)
            success += 1

            if (success + skipped) % 50 == 0:
                print(f"  📊 进度: {success + skipped}/{len(pages)} (新导出 {success}, 跳过 {skipped})")
                save_exported(exported)

        except Exception as e:
            failed += 1
            print(f"  ❌ 导出失败 [{page_type}] {title}: {e}")
            save_exported(exported)  # 失败也保存进度

    save_exported(exported)
    print(f"\n  导出完成: 成功 {success}, 跳过 {skipped}, 失败 {failed}")

    # 4. 生成 index.md
    print("\n📋 步骤 4: 生成 index.md...")
    generate_index(pages, page_map)

    # 5. 生成 schema 文件
    print("\n📖 步骤 5: 生成 schema 文件...")
    write_schema_claude_md()
    write_schema_wiki_schema()

    # 6. 生成 sync_state.json
    print("\n💾 步骤 6: 生成 sync_state.json...")
    state = build_sync_state(pages, page_map)
    save_sync_state(state)
    print(f"  ✅ sync_state.json 已生成 ({len(state['page_mapping'])} pages)")

    # 7. Git commit + push
    print("\n📤 步骤 7: Git push...")
    now = datetime.now(TZ).strftime("%Y-%m-%d %H:%M")
    git_commit_and_push(f"feat(wiki): full export {now}", force=True)

    print("\n🎉 全量导出完成！")


def cmd_incremental(args):
    """增量同步。从 sync_state.json 读取上次同步时间。"""
    # 1. 读取 sync_state
    state = load_sync_state()
    if not state.get("last_sync_time"):
        print("❌ 未找到 sync_state.json 或无上次同步记录，请先运行 --full")
        sys.exit(1)

    last_sync = state["last_sync_time"]
    print(f"🚀 开始增量同步 (上次同步: {last_sync})...")

    # 解析时间：转为 UTC 用于 Notion API 查询
    last_sync_dt = datetime.fromisoformat(last_sync)
    last_sync_utc = last_sync_dt.astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    print(f"  查询条件: last_edited_time > {last_sync_utc}")

    # 2. 查询变更页面
    print("\n📥 步骤 1: 查询变更页面...")
    filter_obj = {
        "and": [
            {"property": "类型", "select": {"is_not_empty": True}},
            {"timestamp": "last_edited_time", "last_edited_time": {"after": last_sync_utc}},
        ]
    }
    changed_pages = query_database(DATABASE_ID, filter_obj)
    changed_pages = [p for p in changed_pages if extract_select(p, "类型")]
    print(f"  变更页面: {len(changed_pages)} 个")

    # 3. 获取全量页面列表（构建映射表 + 删除检测）
    print("\n🗺️  步骤 2: 获取全量映射表...")
    all_pages = query_database(DATABASE_ID, {"property": "类型", "select": {"is_not_empty": True}})
    all_valid = [p for p in all_pages if extract_select(p, "类型")]
    page_map = build_page_map(all_valid)
    print(f"  全量页面: {len(all_valid)}, 映射条目: {len(page_map) // 2}")

    # 4. 重新导出变更页面
    print("\n📝 步骤 3: 重新导出变更页面...")
    exported = load_exported()
    updated = 0
    for page in changed_pages:
        page_id = page["id"]
        # 强制重新导出：先从 exported 集合中移除
        exported.discard(page_id)
        try:
            export_page(page, page_map, exported)
            updated += 1
            print(f"  ✅ [{extract_select(page, '类型')}] {extract_title(page)}")
        except Exception as e:
            print(f"  ❌ {extract_title(page)}: {e}")

    save_exported(exported)
    print(f"  导出完成: {updated} 个页面已更新")

    # 5. 删除检测
    print("\n🗑️  步骤 4: 删除检测...")
    notion_active_ids = set(p["id"] for p in all_valid)
    # 同时包含不带连字符的版本，防止 page_mapping 中的旧格式 key 误匹配
    notion_active_ids_no_hyphen = set(pid.replace("-", "") for pid in notion_active_ids)
    deleted = 0

    for page_id, info in list(state.get("page_mapping", {}).items()):
        if page_id not in notion_active_ids and page_id not in notion_active_ids_no_hyphen:
            file_path = OUTPUT_DIR / info["file_path"]
            if file_path.exists():
                file_path.unlink()
                deleted += 1
                print(f"  🗑️ 删除: {info['file_path']}")

    print(f"  删除完成: {deleted} 个文件")

    # 6. 重建 index.md
    print("\n📋 步骤 5: 重建 index.md...")
    generate_index(all_valid, page_map)

    # 7. 更新 sync_state.json
    print("\n💾 步骤 6: 更新 sync_state.json...")
    update_sync_state(state, all_valid, page_map)
    # 从 page_mapping 中移除已删除的
    for page_id in list(state["page_mapping"].keys()):
        if page_id not in notion_active_ids:
            del state["page_mapping"][page_id]
    save_sync_state(state)

    # 8. Git commit + push
    print("\n📤 步骤 7: Git push...")
    if updated > 0 or deleted > 0:
        now = datetime.now(TZ).strftime("%Y-%m-%d %H:%M")
        git_commit_and_push(f"sync: {updated} updated, {deleted} deleted, {now}")
    else:
        # 即使无页面变更，index.md 可能更新了
        import subprocess
        subprocess.run(["git", "add", "-A"], cwd=OUTPUT_DIR, check=True)
        result = subprocess.run(["git", "diff", "--cached", "--quiet"],
                                cwd=OUTPUT_DIR, capture_output=True)
        if result.returncode != 0:
            now = datetime.now(TZ).strftime("%Y-%m-%d %H:%M")
            git_commit_and_push(f"sync: index updated, {now}")
        else:
            print("  ℹ️ 无任何变更，跳过提交")

    print("\n🎉 增量同步完成！")


def cmd_index_only(args):
    """只重建 index.md。"""
    print("🚀 重建 index.md...")

    all_pages = query_database(DATABASE_ID, {"property": "类型", "select": {"is_not_empty": True}})
    pages = [p for p in all_pages if extract_select(p, "类型")]
    page_map = build_page_map(pages)

    generate_index(pages, page_map)
    print("🎉 index.md 已重建！")


def main():
    parser = argparse.ArgumentParser(description="Wiki Markdown Exporter")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--full", action="store_true", help="首次全量导出")
    group.add_argument("--incremental", action="store_true", help="增量同步")
    group.add_argument("--index-only", action="store_true", help="只重建 index.md")
    parser.add_argument("--output", type=str, help="输出目录")

    args = parser.parse_args()

    if args.output:
        global OUTPUT_DIR
        OUTPUT_DIR = Path(args.output)

    if args.full:
        cmd_full(args)
    elif args.incremental:
        cmd_incremental(args)
    elif args.index_only:
        cmd_index_only(args)


if __name__ == "__main__":
    main()
