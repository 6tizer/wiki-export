---
title: Prefill-decode disaggregation
type: concept
tags:
- 推理优化
status: 审核中
confidence: medium
last_compiled: '2026-04-21'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/56f0676b2e2041dfbdd3ee8808c5980a
notion_id: 56f0676b-2e20-41df-bdd3-ee8808c5980a
---

## 定义

Prefill-decode disaggregation 是把大模型推理中的 prefill 阶段与 decode 阶段拆分到不同资源或流程中的服务架构做法，用来优化吞吐、延迟和资源利用。

## 关键要点

- prefill 与 decode 的计算特征不同，拆分后更容易做针对性调度。

- 这类优化常见于高并发、低延迟要求的在线推理场景。

## 来源引用

- [摘要：Traditional ML Inference vs. LLM Inference](summaries/摘要：Traditional ML Inference vs. LLM Inference.md)（[原文](https://x.com/_avichawla/status/2026224423460843665)）

- [摘要：Kimi K2.6 has landed, and it is live on Baseten!](summaries/摘要：Kimi K2.6 has landed, and it is live on Baseten!.md)（[原文](https://x.com/baseten/status/2046263526281576573)）

## 关联概念

- [Kimi K2.6](entities/Kimi K2.6.md)

- [Continuous batching](concepts/Continuous batching.md)

- [KV-aware routing](concepts/KV-aware routing.md)
