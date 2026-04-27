---
title: Claude Code Teleport
type: concept
tags:
- 代码生成
- CLI 工具
status: 草稿
confidence: medium
last_compiled: '2026-04-27'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/3ea8e27846d34098a9f0a68ccdfeecbc
notion_id: 3ea8e278-46d3-4098-a9f0-a68ccdfeecbc
---

## 定义

Claude Code Teleport 是 Anthropic 为 Claude Code 推出的跨设备会话传输功能，允许用户在 Web 或移动端发起的编码会话通过 `--teleport` 标志无缝迁移到本地终端 CLI，保留完整的对话历史和上下文。

## 关键要点

- 用户可以在 Web/Mobile 端启动会话，然后在本地终端用 `--teleport` 命令继续，上下文完整保留

- 与 Remote Control 互补：Teleport 把云端会话拉到终端，Remote Control 让手机驱动本地终端

- Sessions sidebar 和 drag-and-drop 布局配合，支持多 Agent 并行管理

- 社区反馈指出：Teleport 恢复会话时不显示上下文窗口使用率，可能导致模型在高占用率时悄悄降质

## 来源引用

- [摘要：Claude Code Web/Mobile 刷新与 Teleport 功能发布](summaries/摘要：Claude Code Web-Mobile 刷新与 Teleport 功能发布.md)（[原文](https://x.com/ClaudeDevs/status/2047773528121049488)）
