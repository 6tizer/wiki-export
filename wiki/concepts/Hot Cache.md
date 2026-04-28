---
title: Hot Cache
type: concept
tags:
- 知识管理
- 上下文管理
- 长期记忆
- 记忆系统
- RAG/检索
status: 审核中
confidence: medium
last_compiled: '2026-04-23'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/4b23cf57ea1a43bba6ab7a447cfcede1
notion_id: 4b23cf57-ea1a-43bb-a6ab-7a447cfcede1
---

## 定义

Hot Cache 是一种会话级高频知识缓存层，通常把最近的重要上下文、任务状态与关键结论压缩到单独文件中，让 Agent 在新会话开始时先读取这层“热记忆”，避免每次都从完整知识库重新扫描。

## 关键要点

- 它是长期知识库与当前工作上下文之间的中间层，兼顾低成本加载与上下文连续性

- 在 claude-obsidian 里，Hot Cache 用来保存最近会话的高价值状态，使问答与写作能快速续接

- 它适合和 index、wiki 页面按层级配合：先读热缓存，再读索引，最后按需下钻具体页面

- 它的价值不只是节省 token，更在于让跨会话工作保持“不断线”

## 关联概念

- [claude-obsidian](entities/claude-obsidian.md)

- [Karpathy LLM Wiki 方法论](concepts/Karpathy LLM Wiki 方法论.md)

- [Obsidian Bases](concepts/Obsidian Bases.md)

- [第二大脑系统](concepts/第二大脑系统.md)

- [autoresearch](entities/autoresearch.md)

- [Contradiction Callouts](concepts/Contradiction Callouts.md)

## 来源引用

- [摘要：custom slash commands](summaries/摘要：custom slash commands.md)（[原文](https://x.com/hasantoxr/status/2046174499226403038)）

- [摘要：new update to the LLM Knowledge base](summaries/摘要：new update to the LLM Knowledge base.md)（[原文](https://x.com/shannholmberg/status/2047013785857302550)）
