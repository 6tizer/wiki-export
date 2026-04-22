---
title: Cursor CLI /btw
type: concept
tags:
- Agent 编排
- 上下文管理
status: 草稿
confidence: medium
last_compiled: '2026-04-21'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/b5b027cb0b4b4a5ab04abb060fcbb0c7
notion_id: b5b027cb-0b4b-4a5a-b04a-bb060fcbb0c7
---

## 定义

Cursor CLI /btw 是一种侧问机制，允许用户在当前 agent 任务继续运行时，插入一个简短的旁路问题而不打断主流程。

## 关键要点

- 它降低了多线程思考时的上下文切换成本。

- 这种设计体现了对 agent 会话编排的细化：主任务与临时问题可以并存。

- 对长任务、调试过程和探索式开发特别实用。

## 来源引用

- [摘要：How it works:](summaries/摘要：How it works-.md)（[原文](https://x.com/cursor_ai/status/2046324136377721128)）
