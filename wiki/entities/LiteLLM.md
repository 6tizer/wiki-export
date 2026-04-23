---
title: LiteLLM
type: entity
tags:
- 开发工具
status: 草稿
confidence: medium
last_compiled: '2026-04-23'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/26f21056c46e4e938853bbca055a4231
notion_id: 26f21056-c46e-4e93-8853-bbca055a4231
---

## 定义

LiteLLM 是一个统一多模型 API 的代理与适配层，能够把不同模型提供方包装成兼容 OpenAI / Anthropic 风格的调用接口，常被用作本地模型、聚合平台与上层 Agent 产品之间的桥梁。

## 关键要点

- 可作为代理层，把本地模型、OpenRouter 等上游能力接入统一接口。

- 在 Agent 产品里，它的价值不只是“转发请求”，还包括协议适配、路由与后端解耦。

- 当 Claude Desktop 支持第三方推理时，LiteLLM 这类中间层会成为连接桌面体验与外部模型生态的重要枢纽。

## 来源引用

- [摘要：Anthropic has quietly shipped third-party inference for Cowork and Code in Claude Desktop.](summaries/摘要：Anthropic has quietly shipped third-party inference for Cowork and Code in Claude Desktop.md)（[原文](https://x.com/PawelHuryn/status/2047039360856387944)）

## 关联概念

- [OpenRouter](entities/OpenRouter.md)

- [AI 模型网关](concepts/AI 模型网关.md)

- [本地模型推理](concepts/本地模型推理.md)

- [Claude Cowork](entities/Claude Cowork.md)

- [Claude Code](entities/Claude Code.md)
