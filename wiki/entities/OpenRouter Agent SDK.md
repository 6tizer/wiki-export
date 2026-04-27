---
title: OpenRouter Agent SDK
type: entity
tags:
- 代码生成
- Harness 工程
status: 草稿
confidence: medium
last_compiled: '2026-04-27'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/3800d220033544b4bed201d3a096be64
notion_id: 3800d220-0335-44b4-bed2-01d3a096be64
---

## 定义

OpenRouter Agent SDK（npm 包名 `@openrouter/agent`）是 OpenRouter 官方发布的 TypeScript 工具包，用于在 OpenRouter 平台上快速构建 AI Agent。其核心原语 `callModel` 封装了多轮工具调用、停止条件、流式输出、状态管理和工具审批模式，使开发者无需手写调用循环即可构建 Agent 应用。

**别名**：`@openrouter/agent`

## 关键要点

- 基于 TypeScript，面向 Node.js 生态

- 核心 API 为 `callModel`，处理 multi-turn tool calling loop

- 内置支持 streaming、state management、tool approval patterns

- 与 OpenRouter 模型路由深度集成，可访问数百个模型

- 适合构建需要多步推理和工具使用的 Agent

## 关联概念

- [OpenRouter](entities/OpenRouter.md)

- [Hermes Agent](entities/Hermes Agent.md)

## 来源引用

- [摘要：Turn Your Hermes Agent Into an OpenRouter Expert](summaries/摘要：Turn Your Hermes Agent Into an OpenRouter Expert.md)（[原文](https://x.com/OpenRouter/status/2047506176447783155)）

- [摘要：Introducing "create-agent-tui"](summaries/摘要：Introducing create-agent-tui.md)（[原文](https://x.com/OpenRouter/status/2047701992798392484)）
