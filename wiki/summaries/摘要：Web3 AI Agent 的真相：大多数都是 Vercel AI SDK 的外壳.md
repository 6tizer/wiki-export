---
title: 摘要：Web3 AI Agent 的真相：大多数都是 Vercel AI SDK 的外壳
type: summary
tags:
- 链上协议
- 多Agent协作
- AI 产品
status: 已审核
confidence: high
last_compiled: '2026-04-11'
source_tags: Agent, LLM, 自动化
source_article_url: ''
notion_url: https://www.notion.so/Tizer/1f636de0a7ee4590aa227b65cd8cfffd
notion_id: 1f636de0-a7ee-4590-aa22-7b65cd8cfffd
---

## 一句话摘要

BoxMrChen 指出大多数 Web3 AI Agent 框架本质上是 Vercel AI SDK 或 LangChain 的外壳复刻，建议开发者直接用成熟工具库而非追随「革命性」新框架。

## 关键洞察

- **Vercel AI SDK 被严重低估**：每月下载 2000 万次，Stars 23000+，支持 100+ 模型，已是完整解决方案

- **ElizaOS 在重新实现已有东西**：其基础 Agent 运行时逻辑，某种程度上就是在复刻 Vercel AI SDK 已做好的东西

- **Web3 的「贡献」实质**：大多数就是写了几个调用 Solana 或 EVM API 的 Tool 类

- **实用建议**：先把 Vercel AI SDK 文档读一遍，把 LangChain 示例跑一跑，再评估那些「革命性」Web3 框架

- **LangChain 的复杂 Agent 首选**：RAG 和多 Agent 编排方面 LangChain JS 功能最全面

## 提取的概念

[ElizaOS](entities/ElizaOS.md) · [LangChain](entities/LangChain.md) · [Vercel AI SDK](entities/Vercel AI SDK.md)

## 原始文章信息

- **作者**：BoxMrChen

- **来源**：X 书签

- **发布时间**：2025-01-13

- **链接**：[https://x.com/BoxMrChen/status/1878535029401505981](https://x.com/BoxMrChen/status/1878535029401505981)

## 个人评注

这篇文章提供了实用的工具选型原则：在评估新框架时，先看它是否只是已有工具的包装。对 Tizer 实际 Agent 工具选型有直接指导意义。
