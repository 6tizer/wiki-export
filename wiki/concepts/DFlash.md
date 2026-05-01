---
title: DFlash
type: concept
tags: []
status: 审核中
confidence: medium
last_compiled: '2026-04-23'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/6877aaf1183d48d1aa58d15118d8a812
notion_id: 6877aaf1-183d-48d1-aa58-d15118d8a812
---

## 定义

DFlash 是一种基于 block diffusion 的 speculative decoding 加速方法。它在每个位置只保留一个 draft 预测，再交给 target model 做批量验证。

## 关键要点

- 通过 block 级草稿生成替代逐 token 的线性草稿展开

- 相比传统 speculative decoding，它把多个位置的候选一次性提出来验证

- 由于每个 position 只保留一个预测，分叉点上的潜在正确候选仍可能被浪费

- DDTree 可以看作在 DFlash 基础上继续扩展分支表达能力的后续方案

## 来源引用

- [原文链接](https://x.com/nash_su/status/2043924682802712600)｜《Qwen 推理性能最高提升8倍！》｜项目页：[DDTree](https://liranringel.github.io/ddtree/)｜源文章：DDTree：在 DFlash 基础上再提速，Qwen3 推理性能最高飙升 8 倍

- [摘要：Tree-based speculative decoding for Apple Silicon.](summaries/摘要：Tree-based speculative decoding for Apple Silicon.md)（[原文](https://x.com/QingQ77/status/2045500092527087861)）

- [摘要：Worklanes, not just tabs.](summaries/摘要：Worklanes, not just tabs.md)（[原文](https://x.com/iotcoi/status/2046950805568164168)）

## 关联概念

- [DDTree](concepts/DDTree.md)

- [Speculative Decoding](concepts/Speculative Decoding.md)

- [Tree Attention](concepts/Tree Attention.md)

- [Block Diffusion](concepts/Block Diffusion.md)

- [ddtree-mlx](entities/ddtree-mlx.md)

- [MLX 框架](entities/MLX 框架.md)

- [vLLM](entities/vLLM.md)

- [Qwen3.6-27B](entities/Qwen3.6-27B.md)
