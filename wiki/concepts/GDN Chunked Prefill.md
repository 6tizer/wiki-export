---
title: GDN Chunked Prefill
type: concept
tags:
- 推理优化
status: 草稿
confidence: medium
last_compiled: '2026-04-29'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/9ad4beef2c4646d0b6fa64f1109f4a69
notion_id: 9ad4beef-2c46-46d0-b6fa-64f1109f4a69
---

## 定义

GDN Chunked Prefill（Gated Delta Network 分块预填充）是一种针对线性注意力模型的计算优化策略，将长序列的 prefill 阶段分块处理，结合门控机制（Gate）实现高效的注意力计算。Qwen3.5/3.6 系列模型采用此架构。

## 核心要点

- 利用 GDN 门控的指数衰减特性，自动实现片内 Context Parallelism

- 分块处理长序列的预填充，降低显存压力

- FlashQLA 将其前向和反向传播分别优化为两个独立内核，而非融合为单一内核

- 在大 batch size 下虽有额外内存 I/O 开销，但在边缘设备和长上下文场景表现更优

## 关联概念

- [FlashQLA](entities/FlashQLA.md)

- [TileLang](entities/TileLang.md)

- [线性注意力](concepts/线性注意力.md)

- [Warp Specialization](concepts/Warp Specialization.md)

## 来源引用

- [摘要：Recipes for serving LLMs locally on RTX 3090s.](summaries/摘要：Recipes for serving LLMs locally on RTX 3090s.md)（[原文](https://x.com/Alibaba_Qwen/status/2049462758211772663)）
