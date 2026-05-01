---
title: Looped Transformer
type: concept
tags: []
status: 审核中
confidence: high
last_compiled: '2026-04-20'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/e1a9e61669ee42a8b024a6ef190ba56d
notion_id: e1a9e616-69ee-42a8-b024-a6ef190ba56d
---

## 定义

**Looped Transformer** 指把同一组 Transformer 层按循环方式重复执行多次，而不是堆叠许多彼此独立的层，以更少参数获得更深的有效计算深度。

## 关键要点

- 它通过参数共享把“深度”与“参数量”部分解耦。

- 循环结构天然更贴近迭代算法，因此常被视为更适合推理与逐步求解的归纳偏置。

- 这类模型支持在推理阶段增加循环次数，以提升测试时计算量。

- 它是理解 MoR、latent reasoning、recursive depth 等工作的基础母题。

## 来源引用

- [摘要：Mythos is a looped transformer!? 😳 Should be a Mixture-of-Recursions (MoR) — 2× faster, controlled effort.](summaries/摘要：Mythos is a looped transformer! 😳 Should be a Mixture-of-Recursions (MoR) — 2× faster, controlled effort.md)

## 关联概念

- [Mixture-of-Recursions](concepts/Mixture-of-Recursions.md)

- [Latent Reasoning](concepts/Latent Reasoning.md)

- [Adaptive Token Routing](concepts/Adaptive Token Routing.md)

- [Universal Transformer](concepts/Universal Transformer.md)

## 备注

- 该概念可视为递归式语言模型与动态深度研究的共同起点。
