---
title: Prompt Cache
type: concept
tags: []
status: 审核中
confidence: high
last_compiled: '2026-04-27'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/4e2afe2db2f34ebb81964b6efcc11354
notion_id: 4e2afe2d-b2f3-4ebb-8196-4b6efcc11354
---

## 定义

Prompt Cache 是模型服务对重复 prompt 前缀进行缓存复用的机制，使相同或高度稳定的上下文在后续请求中不必按全价重复计算，从而降低长上下文会话的成本与延迟。

## 关键要点

- 它的收益前提是 prompt 前缀足够稳定、会话节奏足够连续。

- 在研究型工作流里，频繁切换 session、长时间停顿或不断追加大段新上下文，都会显著降低缓存命中率。

- Prompt Cache 能缓解成本问题，但无法替代外部检索；如果原始大语料仍然反复塞进主会话，整体成本依然偏高。

- 在本文场景中，作者强调“把语料留在 NotebookLM，只把蒸馏后的答案交给 Claude”，比单靠 Cache 更省钱。

## 来源引用

- [摘要：用好NotebookLM立省80%Token](summaries/摘要：用好NotebookLM立省80%Token.md)（[原文](https://x.com/MinLiBuilds/status/2046002143937941988)）

- [摘要：Claude Code's Limits Are Generous. The Problem Is Your Harness.](summaries/摘要：Claude Code's Limits Are Generous. The Problem Is Your Harness.md)（[原文](https://x.com/PawelHuryn/status/2048170309396926577)）

## 关联概念

- [NotebookLM](entities/NotebookLM.md)

- [Claude Code](entities/Claude Code.md)

- [RAG](concepts/RAG.md)
