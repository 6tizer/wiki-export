---
title: Claude Context
type: entity
tags:
- Coding Agent
- Agent 技能
status: 审核中
confidence: medium
last_compiled: '2026-04-21'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/7c6ee75985c547d087aea07f9e455204
notion_id: 7c6ee759-85c5-47d0-87ae-a07f9e455204
---

## 定义

Claude Context 是一类把代码库转化为可检索上下文层的 MCP 工具/服务，文中具体指 Zilliz 推出的 hybrid vector search MCP，用来让代理在不反复读取整仓代码的前提下完成检索与理解。

## 档案要点

- 其核心思路是把“代码库本身”变成一个可召回的上下文系统，而不是每次任务都全文塞入模型。

- 相比输出压缩类工具，它更偏向检索增强与上下文层设计。

- 在本文里，它代表向量检索 + MCP 结合的 token 节流路线。

## 关联概念

- [Context Mode](concepts/Context Mode.md)

- [codebase-memory-mcp](entities/codebase-memory-mcp.md)

## 来源引用

- [摘要：The fastest and most efficient code intelligence engine for AI coding agents.](summaries/摘要：The fastest and most efficient code intelligence engine for AI coding agents.md)（[原文](https://x.com/DataChaz/status/2045784379155226971)）
