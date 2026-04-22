---
title: Universal Transformer
type: concept
tags:
- LLM
status: 草稿
confidence: high
last_compiled: '2026-04-20'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/dad3e4f7d023484db5bd58e484dc489c
notion_id: dad3e4f7-d023-484d-b5bd-58e484dc489c
---

## 定义

**Universal Transformer** 是一种在深度维度上引入递归更新与可选停止机制的 Transformer 变体，通常被视为后续循环式 Transformer 研究的重要源头之一。

## 关键要点

- 它把并行自注意力与循环归纳偏置结合起来。

- 通过按位置重复更新表示，模型获得类似 RNN 的迭代特征。

- 动态 halting 机制为后续自适应计算研究提供了早期范式。

- 在当前语境下，它是理解 Looped Transformer 与 MoR 演化链条的起点文献之一。

## 来源引用

- [摘要：Mythos is a looped transformer!? 😳 Should be a Mixture-of-Recursions (MoR) — 2× faster, controlled effort.](summaries/摘要：Mythos is a looped transformer! 😳 Should be a Mixture-of-Recursions (MoR) — 2× faster, controlled effort.md)

## 关联概念

- [Mixture-of-Recursions](concepts/Mixture-of-Recursions.md)

- [Looped Transformer](concepts/Looped Transformer.md)

- [Latent Reasoning](concepts/Latent Reasoning.md)

- [Adaptive Token Routing](concepts/Adaptive Token Routing.md)

## 备注

- 适合放入“递归 Transformer 历史起点”这一知识脉络中。
