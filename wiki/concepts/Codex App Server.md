---
title: Codex App Server
type: concept
tags:
- Harness 工程
- 代码生成
status: 草稿
confidence: high
last_compiled: '2026-04-30'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/3746e0e851aa4b12aa8a479a6b41d8dd
notion_id: 3746e0e8-51aa-4b12-aa8a-479a6b41d8dd
---

## 定义

Codex App Server 是 OpenAI Codex 内置的无头（headless）运行模式，通过 JSON-RPC 协议以编程方式控制 Codex，支持启动对话线程、触发执行轮次、读取执行结果等操作，是实现大规模 Agent 编排的关键基础设施。

## 关键要点

- 通过 JSON-RPC 接口提供程序化控制，比 CLI 或 tmux 方式更可扩展

- 支持动态工具调用（dynamic tool calls），可封装外部 API（如 Linear GraphQL）而不暴露访问令牌

- 是 Symphony 等编排系统的底层执行引擎

- 安全设计：通过函数封装隔离敏感凭证，Agent 永远不直接接触原始 token

## 来源引用

- [摘要：OpenAI开源Symphony：给每一个任务配一个永不下班的 AI员工](summaries/摘要：OpenAI开源Symphony：给每一个任务配一个永不下班的 AI员工.md)（[原文](https://x.com/vista8/status/2049484504444834126)）

## 关联概念

- [Symphony](concepts/Symphony.md)

- [Codex](entities/Codex.md)

- [Harness Engineering](concepts/Harness Engineering.md)
