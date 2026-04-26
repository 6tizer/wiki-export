---
title: ModelBox
type: entity
tags:
- CLI 工具
- OpenClaw
- 上下文管理
status: 审核中
confidence: high
last_compiled: '2026-04-26'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/a276112289294082b160df2f820aff93
notion_id: a2761122-8929-4082-b160-df2f820aff93
---

## 定义

ModelBox 是一个兼容 OpenAI 协议的调试代理工具，用来拦截、捕获和回放 Agent 与上游模型之间的请求，帮助开发者完整观察 system prompt、上下文拼接结果与请求载荷。

## 核心要点

- 支持 `mock` 与 `passthrough` 双模式，可以在不改动现有客户端的前提下调试 Agent 流量

- 通过 OpenAI 兼容接口承接 `/v1/responses` 与 `/v1/chat/completions`，适合接入 Hermes、OpenClaw 等 Agent

- 可以把真实请求以结构化日志落盘，便于排查 token 消耗、提示词膨胀与上下文污染问题

- 在这篇文章的语境里，ModelBox 被用来导出 Hermes Agent 的完整系统提示词，是分析提示词分层结构的关键抓手

## 来源引用

- [原文链接](https://x.com/LufzzLiz/status/2044258384556556743)｜[摘要：抽丝剥茧：深度解析 Hermes Agent 万字系统提示词（System Prompt）构成](summaries/摘要：抽丝剥茧：深度解析 Hermes Agent 万字系统提示词（System Prompt）构成.md)

## 关联概念

- [Hermes Agent](entities/Hermes Agent.md)

- [AGENTS.md](concepts/AGENTS.md.md)

- [SOUL.md](concepts/SOUL.md.md)

- [MEMORY.md](concepts/MEMORY.md.md)

- [Agent Skills](concepts/Agent Skills.md)
