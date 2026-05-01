---
title: context-timeline
type: entity
tags:
- Harness 工程
- 上下文管理
status: 草稿
confidence: medium
last_compiled: '2026-04-28'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/0e4798447d8d4b4abb19fc4d87278115
notion_id: 0e479844-7d8d-4b4a-bb19-fc4d87278115
---

## 定义

context-timeline 是一个 Claude Code Hook，用于实时可视化 Claude Code 的上下文窗口和子代理（Subagent）运行状态。通过浏览器界面展示主 Agent 上下文时间线以及各 Subagent 的独立上下文。

## 关键要点

- 安装方式：`npx claude-code-templates@latest --hook monitoring/context-timeline`

- 基于 Claude Code Hooks 机制实现，监听 SessionStart、PreToolUse、PostToolUse、Stop 事件

- 实时显示主 Agent 上下文窗口和并行运行的 Subagent 的上下文状态

- 可直观观察 Subagent 何时启动、何时结束、以及返回给主 Agent 的上下文大小

- 由 @dani_avila7 开发，托管在 [aitmpl.com](http://aitmpl.com/)（AI Templates 平台）

## 来源引用

- [摘要：Keep your Claude Code context clean with Subagents](summaries/摘要：Keep your Claude Code context clean with Subagents.md)（[原文](https://x.com/dani_avila7/status/2048486242321662189)）

## 关联概念

- [Sub agent 上下文隔离](concepts/Sub agent 上下文隔离.md)

- [Claude Code 上下文管理](concepts/Claude Code 上下文管理.md)

- [Claude Code Hooks](concepts/Claude Code Hooks.md)
