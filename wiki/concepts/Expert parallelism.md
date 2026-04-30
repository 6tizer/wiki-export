---
title: Expert parallelism
type: concept
tags:
- LLM
- 推理优化
status: 审核中
confidence: medium
last_compiled: '2026-04-23'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/6a9b399699f94a9daf26e2457b79b428
notion_id: 6a9b3996-99f9-4a9d-af26-e2457b79b428
---

## 定义

Expert parallelism 是 MoE 模型常用的并行策略：把不同专家分散到不同设备上，注意力等共享层在多卡间复制，由门控网络把 token 动态路由给对应专家处理。

## 关键要点

- 它不是简单的数据并行或模型全量复制，而是按专家模块做分片。

- 每张 GPU 只持有部分专家权重，因此能够在总参数量很大的前提下降低单卡负担。

- 这类并行方式会把模型结构设计与推理引擎调度紧密耦合。

## 来源引用

- [摘要：Traditional ML Inference vs. LLM Inference](summaries/摘要：Traditional ML Inference vs. LLM Inference.md)（[原文](https://x.com/_avichawla/status/2026224423460843665)）

## 关联概念

- [MoE 架构](concepts/MoE 架构.md)

- [KV-aware routing](concepts/KV-aware routing.md)

- [Prefill-decode disaggregation](concepts/Prefill-decode disaggregation.md)
