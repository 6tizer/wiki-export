---
title: DeepGEMM
type: entity
tags:
- 推理优化
- 算力基础设施
status: 草稿
confidence: medium
last_compiled: '2026-04-28'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/a9f5bb80644f4049bfe6dcf51236c4e7
notion_id: a9f5bb80-644f-4049-bfe6-dcf51236c4e7
---

## 定义

DeepGEMM 是 DeepSeek 自研的矩阵乘法（GEMM）kernel 库，用于替代通用的 NVIDIA cuBLAS，以在保证 Batch Invariance 的前提下完成高性能矩阵运算。

## 关键要点

- **开发方**：DeepSeek

- **用途**：在大模型推理和训练中执行 batch-invariant 的矩阵乘法

- **设计动机**：通用 cuBLAS 的 split-K 优化会改变浮点归约顺序，破坏逐比特一致性；DeepGEMM 放弃 split-K，采用更受约束的计算路径

- **核心特性**：

  - 保证不同 batch 组织下的逐比特一致输出

  - 支持 FP4/FP8 等低精度计算

- **首次应用**：DeepSeek V4

## 来源引用

- [摘要：DeepSeek不惜代价保住它！V4关键特性被挖出来了](summaries/摘要：DeepSeek不惜代价保住它！V4关键特性被挖出来了.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzIzNjc1NzUzMw%3D%3D&mid=2247887476&idx=1&sn=0ae5c990a3f2376794effe890264a4cf&chksm=e90f4689c3631f787a3d75e7836cc7206e8ee5fa3f2182a39b1e5dbb15dc71b0f5c72dc6ab75#rd)）

## 关联概念

- [Batch Invariance](concepts/Batch Invariance.md)

- [Dual-kernel](concepts/Dual-kernel.md)

- [DeepSeek V4](entities/DeepSeek V4.md)
