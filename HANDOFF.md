# HANDOFF.md — 2026-04-14

## 当前任务目标

将 Notion 知识 Wiki 数据库导出为本地 Markdown 文件系统，推送到 GitHub 私有仓库，并建立自动化增量同步 + 查询 Skill。

## 已完成的步骤

### Phase 1: 全量导出（已完成 ✅）
1. 编写 `export.py` — 全量导出脚本（限速器、断点续传、Block→Markdown 转换、mention→wikilink）
2. 修复数据库 ID 错误 — 文档写的 `1c770107...` 返回 404，实际 ID 为 `f98c88d3-d587-494a-98ff-92fbaf9228c4`
3. 修复目录名复数形式 — `entitys` → `entities`，`synthesiss` → `syntheses`，`summarys` → `summaries`（用 TYPE_TO_DIR 映射表）
4. 修复 SSL 连接错误 — 在限速器中添加 SSL/Connection error 异常捕获和指数退避
5. 全量导出 1915 页成功（733C + 360E + 777S + 43Syn）
6. Git push 到 https://github.com/6tizer/wiki-export

### Phase 2: 增量同步自动化（已完成 ✅）
1. 改造 `--incremental` 模式 — 从 sync_state.json 自动读取上次同步时间，不再需要 --since
2. 新增 sync_state.json 管理 — 含 last_sync_time、page_mapping（全量映射）
3. 新增删除检测 — 对比 Notion 活跃页面 vs 本地文件，自动删除已移除的页面
4. 新增 Git 自动提交 — 无变更时不产生空提交（git diff --cached --quiet）
5. `--full` 完成后自动生成 sync_state.json
6. 时区改为 Asia/Shanghai（UTC+8）
7. Cron 已配置 — 每天凌晨 3:00 运行，日志输出到 /tmp/wiki-sync.log

### Wiki 查询 Skill（已完成 ✅）
1. 创建 `~/.claude/skills/wiki/SKILL.md`（v3.1）
2. 通过子 Agent 隔离上下文，主对话只拿到精炼答案
3. 相关性驱动的分层检索（L0 索引定位 → L1 语义匹配 → L2 按需深入）
4. 不依赖 Lint/Fixer 运维质量和 synthesis 覆盖面
5. 全局 CLAUDE.md 已加自动触发规则

### Notion 页面更新（已完成 ✅）
- Phase 1 页面 `b3d361de` — 追加了执行记录（5 个问题 + 性能数据）
- Phase 2 页面 `6d3852cf` — 追加了执行记录（4 个问题 + 验收标准逐项检查）

## 关键文件

| 文件 | 路径 | 说明 |
|------|------|------|
| export.py | ~/claude-workspace/wiki-export/export.py | 导出脚本主文件 |
| sync_state.json | ~/claude-workspace/wiki-export/wiki-export/sync_state.json | 增量同步状态（1913 页映射） |
| wiki Skill | ~/.claude/skills/wiki/SKILL.md | v3.1 查询 Skill |
| 全局 CLAUDE.md | ~/.claude/CLAUDE.md | 已加 Wiki 自动触发规则 |
| settings.json | ~/.claude/settings.json | 已加 Bash 自动授权规则 + cron |

## 关键决策及理由

1. **不用 notion-client SDK** — requests 直接调 REST API，核心工作量在 Block→Markdown 转换，SDK 帮不上忙
2. **TYPE_TO_DIR 映射表** — Python 简单加 s 不对（entitys/synthesiss），用显式映射
3. **相关性驱动而非标签加权** — 不依赖 Lint/Fixer 的 status/confidence 运维质量
4. **Wiki 查询用子 Agent 隔离** — 避免知识库文件内容污染主对话上下文

## 已知问题和风险

1. **Synthesis 同名冲突已解决** — 用户在 Notion 删除了 2 对重复条目（45→43），但 index.md 统计可能偶尔显示不一致（Notion 查询分页差异）
2. **SSL 错误间歇出现** — 每次全量查询约 1 次 SSLEOFError，重试后成功，根因可能是 Mac mini 网络环境
3. **cron 工作目录** — 需要传 `--output ./wiki-export` 参数，否则会在错误目录生成文件
4. **Wiki Skill 刚创建** — 需要更多实际使用来验证检索质量，特别是跨领域和冷门话题的查询

## 下一步建议

- 等今晚 cron 自动触发后检查 /tmp/wiki-sync.log 确认增量同步正常
- 在日常使用中测试 /wiki Skill，积累需要改进的场景
- 如需 Notion 端也有更新，可在 Phase 页面追加执行记录
