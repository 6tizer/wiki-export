---
title: 摘要：Claude Code Hooks：用 settings.json 把 AI 编程助手从「偶尔听话」升级成「永不出错的工程队友」
type: summary
tags:
- Coding Agent
status: 已审核
confidence: high
last_compiled: '2026-04-12'
source_tags: Agent, 自动化, LLM, Claude, Hooks
source_article_url: https://www.notion.so/33d701074b68812eb95be233c9e5a03b
notion_url: https://www.notion.so/95548ae67e4a4f6382808fe6a40c720e
notion_id: 95548ae6-7e4a-4f63-8280-8fe6a40c720e
---

### 一句话摘要

Claude Code Hooks 通过 PreToolUse 和 PostToolUse 等事件把规则从提示建议升级成确定性执行，补上了 AI 编程工作流里最关键的治理层。

### 关键洞察

- [CLAUDE.md](http://claude.md/) 负责建议，Hooks 负责强制，两者分别解决语义引导和物理约束。

- PreToolUse 适合拦截危险命令和敏感文件访问。

- PostToolUse 适合把测试、格式化和审计日志嵌入开发闭环。

### 提取的概念

- [Claude Code Hooks](concepts/Claude Code Hooks.md)

- [PreToolUse](concepts/PreToolUse.md)

- [PostToolUse](concepts/PostToolUse.md)

### 原始文章信息

- 作者：@AYi_AInotes

- 来源：X书签

- 发布时间：2026-04-04

- 链接：[原文](https://x.com/AYi_AInotes/status/2040238450373435857)

### 个人评注

这类 hook 机制对 Tizer 的 HITL 流程非常关键，因为真正可落地的 Agent 不是“更听话”，而是有明确、可执行、可阻断的工程边界。
