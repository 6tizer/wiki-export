---
title: Block Diffusion
type: concept
tags:
- 推理优化
status: 审核中
confidence: medium
last_compiled: '2026-04-23'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/eab1e2ef31d24583a98a5303c2fc59d2
notion_id: eab1e2ef-31d2-4583-a98a-5303c2fc59d2
---

## 定义

Block Diffusion 是一种按 block 而非逐 token 生成后续候选分布的草稿生成方式，可用于 speculative decoding 的 draft 阶段。

## 关键要点

- 一次前向可为多个连续位置生成候选分布

- 这种并行草稿生成方式为 DFlash 和 DDTree 构建多 token 候选提供了基础

- 它把“下一 token 预测”扩展为“下一段位置分布预测”

- 价值在于为后续批量验证或树状验证创造更高并行度

## 来源引用

- [原文链接](https://x.com/nash_su/status/2043924682802712600)｜《Qwen 推理性能最高提升8倍！》｜项目页：[DDTree](https://liranringel.github.io/ddtree/)｜源文章：DDTree：在 DFlash 基础上再提速，Qwen3 推理性能最高飙升 8 倍

- [摘要：Tree-based speculative decoding for Apple Silicon.](summaries/摘要：Tree-based speculative decoding for Apple Silicon.md)（[原文](https://x.com/QingQ77/status/2045500092527087861)）

## 关联概念

- [DDTree](concepts/DDTree.md)

- [DFlash](concepts/DFlash.md)

- [Speculative Decoding](concepts/Speculative Decoding.md)

- [Tree Attention](concepts/Tree Attention.md)

- [ddtree-mlx](entities/ddtree-mlx.md)

- [Qwen3.5-27B](entities/Qwen3.5-27B.md)
