---
title: FlashQLA
type: entity
tags:
- 推理优化
status: 草稿
confidence: high
last_compiled: '2026-04-29'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/555929a9bb534aa99b6dfd8c7e307d13
notion_id: 555929a9-bb53-4aa9-9b6d-fd8c7e307d13
---

## 定义

FlashQLA 是由 Qwen 团队开发的高性能线性注意力内核库，基于 TileLang 构建，专为 GDN（Gated Delta Network）Chunked Prefill 的前向和反向传播进行深度优化。在 NVIDIA Hopper（SM90+）GPU 上实现 2-3 倍前向加速和 2 倍反向加速，特别适用于端侧 agentic 推理和预训练场景。

**别名**：Flash Qwen Linear Attention

## 核心要点

- 基于 TileLang 的融合 warp-specialized 内核，实现数据搬运、Tensor Core 计算与 CUDA Core 计算的流水线重叠

- Gate-driven 自动片内 Context Parallelism（CP），在 TP、长序列、小 head 数场景下显著提升 SM 利用率

- 硬件友好的代数重构，在不牺牲数值精度的前提下降低 Tensor Core、CUDA Core 和 SFU 开销

- 反向传播采用 16 级 warp-specialized 流水线，在极其紧张的片上内存约束下实现 2 倍以上的内核级加速

- 需要 SM90+（Hopper）GPU、CUDA 12.8+、PyTorch 2.8+

## 档案信息

- 开发团队：Alibaba Qwen

- GitHub：[https://github.com/QwenLM/FlashQLA（235★）](https://github.com/QwenLM/FlashQLA（235★）)

- 许可证：MIT

- 博客：[https://qwen.ai/blog?id=flashqla](https://qwen.ai/blog?id=flashqla)

- 创建时间：2026-04-24

## 关联概念

- [TileLang](entities/TileLang.md)

- [GDN Chunked Prefill](concepts/GDN Chunked Prefill.md)

- [Warp Specialization](concepts/Warp Specialization.md)

- [线性注意力](concepts/线性注意力.md)

- [club-3090](entities/club-3090.md)

## 来源引用

- [摘要：Recipes for serving LLMs locally on RTX 3090s.](summaries/摘要：Recipes for serving LLMs locally on RTX 3090s.md)（[原文](https://x.com/Alibaba_Qwen/status/2049462758211772663)）
