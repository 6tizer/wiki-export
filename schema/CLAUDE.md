# Tizer's Knowledge Wiki

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
