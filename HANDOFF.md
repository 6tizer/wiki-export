# HANDOFF.md — 2026-04-18

## 当前任务目标

Wiki 知识库同步维护：停用 Notion Worker，改用 Python cron + 自动 README 统计更新。

## 已完成

1. **Notion Worker 停用**（4/17）— 移除 sync 定义，只保留 `triggerWikiSync` tool 用于手动触发。Worker 频繁超时的根因：`queryAllPages()` 每次 sync 都拉 2800+ 页面做 pageMap，超出平台时间限制。
2. **Python cron 改为 2H + flock** — 从 6H 改为 2H，加 `flock -n /tmp/wiki-sync.lock` 防并发
3. **README.md 添加标记区域** — `<!-- stats:start/end -->` 包裹统计数字，脚本只替换该区域
4. **创建 `update-readme-stats.py`** — 读本地文件计数替换标记区域，已测试通过
5. **README 已更新为 2,743+**（本地实际文件数），尚未 commit/push

## 未完成

### 需手动执行：更新 crontab

Claude 沙盒权限无法修改 crontab。在终端执行：

```bash
crontab -l | sed 's|export.py --incremental >>|export.py --incremental \&\& /opt/homebrew/bin/python3 update-readme-stats.py >>|' | crontab -
```

验证：`crontab -l` 应看到 `... export.py --incremental && /opt/homebrew/bin/python3 update-readme-stats.py >> sync.log ...`

### 需 commit + push

```bash
# wiki-export 子仓库
cd /Users/mac-mini/claude-workspace/wiki-export/wiki-export
git add README.md
git commit -m "feat(readme): add auto-updating stats markers"
git push

# 父目录的 stats 脚本
cd /Users/mac-mini/claude-workspace/wiki-export
git add update-readme-stats.py
git commit -m "feat: add README stats auto-update script"
```

## 关键决策

- **Worker 停用理由**：`queryAllPages()` 每次拉 2800+ 页，超出 Workers 平台时间限制导致僵尸状态
- **删除功能假阳性**：中文字符（×, ：等）导致文件名匹配失败，~2000 文件被误删（4/14）
- **统计来源用本地文件计数**：README 描述仓库实际内容，和 Notion 数量差异反映同步状态
- **标记区域方案**：手动编辑 README 不影响自动统计区域

## 三端数据（4/18 快照）

| 端 | 总数 |
|----|------|
| Notion | 2,800（含 lint-report/qa/index） |
| 本地/GitHub | 2,743（仅 concept/entity/synthesis/summary） |

## 关键文件

| 文件 | 说明 |
|------|------|
| `export.py` | 同步脚本，支持 --full/--incremental/--index-only |
| `update-readme-stats.py` | README 统计更新，标记区域替换 |
| `wiki-export/README.md` | 含 `<!-- stats:start/end -->` 标记 |
| `wiki-export/sync_state.json` | 增量同步状态 |
| `wiki-worker/src/index.ts` | Worker（仅保留 tool，sync 已移除） |
