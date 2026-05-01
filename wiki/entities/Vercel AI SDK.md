---
title: Vercel AI SDK
type: entity
tags:
- 前端开发
- RAG/检索
- AI 产品
status: 审核中
confidence: high
last_compiled: '2026-04-27'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/fc6297f9ded54e7e86122060a880a81a
notion_id: fc6297f9-ded5-4e7e-8612-2060a880a81a
---

## 定义

Vercel AI SDK 是由 Next.js 团队打造的 TypeScript AI 工具包，定位为「框架无关的 AI 开发利器」，提供统一接口调用 100+ 个 AI 模型，并原生支持流式输出。每月下载量超 2000 万次，GitHub Stars 超 23,000，贡献者超 604 人。

**官网**：[sdk.vercel.ai](http://sdk.vercel.ai/) | 最新版本：v6（2025年底）

## 核心能力

- **多模型统一调用**：一套 API 覆盖 OpenAI、Anthropic、Google、Mistral 等 100+ 模型

- **Tool/Action 定义**：内置 `tool()` 方法，自动处理 prompt 构建和工具调用循环

- **流式优先**：原生 Server-Sent Events 流式输出

- **RAG 模板**：官方完整 RAG Chatbot 指南

## 核心观点（BoxMrChen）

许多所谓「Web3 AI Agent 框架」本质上是 Vercel AI SDK 的外壳复刻。建议开发者直接用 Vercel AI SDK + 自定义 Tool 类，而非追随「革命性」Web3 框架。

## 局限

- 对复杂多 Agent 编排支持不如 LangGraph 完善

- 与 Vercel 平台有一定绑定感

- 不支持 Edge Runtime 部署（限制场景）

## 来源引用

- [摘要：Web3 AI Agent 的真相：大多数都是 Vercel AI SDK 的外壳](summaries/摘要：Web3 AI Agent 的真相：大多数都是 Vercel AI SDK 的外壳.md)

- [原文链接](https://x.com/RHLSTHRM/status/2031383989488070972)｜《用 Vibe Coding 搭出 5 个链上 AI 交易 Agent：AI SDK + [LI.FI](http://li.fi/) MCP + 免 Gas 全攻略》｜来源条目：用 Vibe Coding 搭出 5 个链上 AI 交易 Agent：AI SDK + LI.FI MCP + 免 Gas 全攻略
