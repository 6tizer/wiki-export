---
title: Memory Flush
type: concept
tags:
- 长期记忆
- Harness 工程
status: 草稿
confidence: high
last_compiled: '2026-04-28'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/e57bbad261ab4e29a50fffb3ca60f719
notion_id: e57bbad2-61ab-4e29-a50f-ffb3ca60f719
---

## 定义

Memory Flush 是 Claude Code 工作流中的自动记忆落盘机制：在任务完成、每次提交、退出信号时自动将会话状态持久化到文件系统，确保关窗不丢进度、换 session 不丢上下文。

## 关键要点

- **触发时机**：任务完成、git commit、退出信号、上下文压缩前

- **持久化目标**：[today.md](http://today.md/)（当天进度）、[projects.md](http://projects.md/)（项目状态）、active-tasks.json（活跃任务）

- **核心原则**：「自动保存 > 靠人记得」——人总会忘，自动化才可靠

- **实现方式**：通过 Claude Code Hooks 的 Stop 和 PreCompact 事件触发

- **与 SSOT 配合**：落盘位置由 SSOT 路由表统一管理，避免信息分散

## 关联概念

- [claude-code-workflow](entities/claude-code-workflow.md)

- [Claude Code Hooks](concepts/Claude Code Hooks.md)

- [SSOT 路由表](concepts/SSOT 路由表.md)

- [完成前验证](concepts/完成前验证.md)

- [多档任务路由](concepts/多档任务路由.md)

## 来源引用

- [摘要：Claude Code 工作流模板 v2](summaries/摘要：Claude Code 工作流模板 v2.md)（[原文](https://x.com/runes_leo/status/2048013195563172162)）
