---
title: 摘要：Keep your Claude Code context clean with Subagents
type: summary
tags:
- 上下文管理
- Harness 工程
- CLI 工具
status: 已审核
confidence: high
last_compiled: '2026-04-28'
source_tags: ''
source_article_url: https://www.notion.so/34f701074b6881eba8c7ff8e483c58e5
notion_url: https://www.notion.so/Tizer/97455ae2f61749df841574979ccc71a0
notion_id: 97455ae2-f617-49df-8415-74979ccc71a0
---

## 一句话摘要

Claude Code 的 Subagent 机制通过上下文隔离解决长会话中的噪音堆积问题，每个子代理在独立窗口完成工作后只返回最终摘要，保持主上下文干净。

## 关键洞察

- **Subagent 本质是上下文隔离器**：子代理拥有独立的 system prompt、工具集和权限，在自己的上下文窗口运行任务，只将最终结果返回主 Agent，避免 grep/find/ls 等中间调用污染主上下文

- **内置 Subagent（Explore & Plan）**：Claude Code 自带两个高频子代理——Explore 用于代码搜索、Plan 用于架构分析并输出实现步骤，将原本需要 50+ 次工具调用的噪音压缩为 3 行结论

- **上下文分叉（Forking）解决冷启动**：默认 Subagent 从空白上下文开始；设置 `CLAUDE_CODE_FORK_SUBAGENT=1` 后，子代理继承父级完整上下文，且共享 prompt cache 前缀（第 2 个及之后的子代理输入 token 成本降低约 10 倍）

- **自定义 Subagent 通过 Markdown 文件声明**：在 `.claude/agents/` 或 `~/.claude/agents/` 放置带 frontmatter 的 Markdown 文件即可定义专用子代理，Claude Code 根据 description 自动匹配调用

- **Context Compaction 的局限**：长会话后 Claude 压缩上下文时会将信息扁平化，重要细节可能在摘要中丢失——这正是 Subagent 隔离模式优于「全部堆在主窗口」的根本原因

## 提取的概念

- [Sub agent 上下文隔离](concepts/Sub agent 上下文隔离.md)

- [Context Engineering](concepts/Context Engineering.md)

- [Claude Code 上下文管理](concepts/Claude Code 上下文管理.md)

- [会话分叉](concepts/会话分叉.md)

- [context-timeline](entities/context-timeline.md)

## 原始文章信息

- **作者**：@dani_avila7

- **来源**：X书签

- **发布时间**：2026-04-26

- **原文链接**：[https://x.com/dani_avila7/status/2048486242321662189](https://x.com/dani_avila7/status/2048486242321662189)

## 个人评注

这篇文章对 Claude Code 的 Subagent 机制做了非常清晰的实操梳理。对 Tizer 的工作流有几个直接启发：

- **OpenClaw Skill 设计**：Subagent 的 Markdown 声明方式（frontmatter + system prompt）与 OpenClaw 的 Skill 文件格式高度相似，可以直接复用这套模式设计 OpenClaw 的 Skill 子代理

- **Wiki Compiler 优化**：当前 Compiler Agent 在单次编译中执行大量 SQL 查重和页面读取，可以考虑将概念查重逻辑封装为 Subagent，隔离中间查询噪音

- **Forking 对长任务的价值**：批量编译模式下，如果能 fork 已建立的数据库 schema 上下文给每个文章的编译子任务，可以避免重复加载 schema 的 token 开销
