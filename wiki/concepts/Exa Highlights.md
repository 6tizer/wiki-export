---
title: Exa Highlights
type: concept
tags:
- RAG/检索
- 上下文管理
status: 草稿
confidence: high
last_compiled: '2026-04-27'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/fff63fd6d0d6442e96085474e2fc8ccc
notion_id: fff63fd6-d0d6-442e-9608-5474e2fc8ccc
---

## 定义

Exa Highlights 是 Exa 推出的查询感知文本提取技术，能根据给定查询从网页中动态筛选最相关的 token 片段，将输入 token 量减少约 96%，同时保持与全文相当的 RAG 准确率。

## 关键要点

- 针对每次请求实时运行（非缓存），处理时间低于 100ms

- 在 SimpleQA 基准上，500 字符的 highlights 匹配 8000 字符全文的准确率，token 用量仅为 1/16

- 4k 字符的 highlights 表现优于 32k 字符的全文

- 特别适用于 frontier 模型（如 GPT 5.5）的长链路 Agent 任务，有效缓解 Context Bloat

- 对技术文档、API 参考、研究论文等长文档场景改善显著

- 通过 Exa API 的 "highlights" content type 即可调用

## 来源引用

- [摘要：Exa now reduces input tokens for web agents by 96%](summaries/摘要：Exa now reduces input tokens for web agents by 96%.md)（[原文](https://x.com/ExaAILabs/status/2047402544260116517)）

## 关联概念

- [Exa](entities/Exa.md)

- [Context Bloat](concepts/Context Bloat.md)
