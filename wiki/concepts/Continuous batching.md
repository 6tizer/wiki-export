---
title: Continuous batching
type: concept
tags:
- 推理优化
- 模型部署
- AI 产品
status: 审核中
confidence: high
last_compiled: '2026-04-23'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/42c8263439704e78aea410fbffa47a08
notion_id: 42c82634-3970-4e78-aea4-10fbffa47a08
---

## 定义

Continuous batching 是一种面向大模型推理服务的调度技术：请求进入后不会被固定锁在同一批次里等待整批结束，而是随着序列完成持续替换新请求，以保持 GPU 持续高利用率。

## 关键要点

- LLM 的输入与输出长度都可变，不同请求会在不同时间结束，静态批处理容易造成 GPU 空转。

- Continuous batching 会在某条序列生成到结束标记后，立刻把空出来的位置换成新请求。

- 这种机制的核心收益是提升吞吐、降低等待时间，并让在线推理系统更适合高并发场景。

## 来源引用

- [摘要：Traditional ML Inference vs. LLM Inference](summaries/摘要：Traditional ML Inference vs. LLM Inference.md)（[原文](https://x.com/_avichawla/status/2026224423460843665)）

## 关联概念

- [Prefill-decode disaggregation](concepts/Prefill-decode disaggregation.md)

- [KV Prefix Caching](concepts/KV Prefix Caching.md)

- [KV-aware routing](concepts/KV-aware routing.md)
