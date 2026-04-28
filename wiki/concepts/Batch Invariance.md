---
title: Batch Invariance
type: concept
tags:
- 推理优化
- 训练/微调
status: 草稿
confidence: high
last_compiled: '2026-04-28'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/d4521c7fc85240fc9578c311611c9348
notion_id: d4521c7f-c852-40fc-9578-c311611c9348
---

## 定义

Batch Invariance（批次不变性）是一种大模型工程设计约束，要求对于同一个 token，无论它在批次中的位置、批次大小、以及与哪些其他请求一起被批处理，模型输出都保持**逐比特完全一致**（bitwise identical）。

别名：批次不变性

## 关键要点

- **核心目标**：确保预训练、后训练（SFT/RL/蒸馏）和推理全流程的数值可复现性

- **解决的问题**：线上服务的动态 batching 会改变 batch 组合，若无此约束，同一提示词可能因 batch 组织不同而产生完全不同的输出

- **工程价值**：

  - 训练/推理/RL 三阶段逐比特可复现

  - 异常定位更精确——排除 batch shape 和 kernel 路径变化导致的数值差异

  - 复杂后训练管线（RL、蒸馏、长链推理）更稳定

- **代价**：不能使用 split-KV（attention 并行归约）和 split-K（GEMM 并行归约）等常见性能优化，导致 GPU 利用率下降、工程复杂度上升

- **DeepSeek V4 的实践**：通过 Dual-kernel（注意力侧）和自研 DeepGEMM（矩阵乘法侧）实现 batch invariance，替代通用的 cuBLAS

## 来源引用

- [摘要：DeepSeek不惜代价保住它！V4关键特性被挖出来了](summaries/摘要：DeepSeek不惜代价保住它！V4关键特性被挖出来了.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzIzNjc1NzUzMw%3D%3D&mid=2247887476&idx=1&sn=0ae5c990a3f2376794effe890264a4cf&chksm=e90f4689c3631f787a3d75e7836cc7206e8ee5fa3f2182a39b1e5dbb15dc71b0f5c72dc6ab75#rd)）

## 关联概念

- [DeepGEMM](entities/DeepGEMM.md)

- [Dual-kernel](concepts/Dual-kernel.md)

- [DeepSeek V4](entities/DeepSeek V4.md)
