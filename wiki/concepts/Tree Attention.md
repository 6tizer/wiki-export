---
title: Tree Attention
type: concept
tags:
- LLM
status: 草稿
confidence: medium
last_compiled: '2026-04-23'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/e873937a365544a99b81de7a22bdaa06
notion_id: e873937a-3655-44a9-9b81-de7a22bdaa06
---

## 定义

Tree Attention 是面向树状候选结构的注意力计算方式。它让 target model 能在一次前向计算中为整棵 draft tree 打分并验证可接受路径。

## 关键要点

- 通过树状 mask 表达不同分支之间的可见性关系

- 把原本多轮串行验证压缩为单轮并行验证

- 是 DDTree 能够高效验证多分支草稿的关键机制之一

- 它关注的不只是生成候选，更是如何高效地一次性验证候选

## 来源引用

- [原文链接](https://x.com/nash_su/status/2043924682802712600)｜《Qwen 推理性能最高提升8倍！》｜项目页：[DDTree](https://liranringel.github.io/ddtree/)｜源文章：DDTree：在 DFlash 基础上再提速，Qwen3 推理性能最高飙升 8 倍

- [摘要：Tree-based speculative decoding for Apple Silicon.](summaries/摘要：Tree-based speculative decoding for Apple Silicon.md)（[原文](https://x.com/QingQ77/status/2045500092527087861)）

## 关联概念

- [DDTree](concepts/DDTree.md)

- [DFlash](concepts/DFlash.md)

- [Speculative Decoding](concepts/Speculative Decoding.md)

- [Block Diffusion](concepts/Block Diffusion.md)

- [ddtree-mlx](entities/ddtree-mlx.md)

- [GatedDeltaNet](concepts/GatedDeltaNet.md)
