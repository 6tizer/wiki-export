---
title: Latent Reasoning
type: concept
tags: []
status: 审核中
confidence: medium
last_compiled: '2026-04-20'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/aca9d465af654bbc8dc823ac7586bd76
notion_id: aca9d465-af65-4bbc-8dc8-23ac7586bd76
---

## 定义

**Latent Reasoning** 指模型把部分推理过程保留在隐藏状态或潜空间中完成，而不是全部外显为自然语言 token，从而用内部计算替代显式链式思考。

## 关键要点

- 它强调“先在潜空间里想，再决定输出什么”。

- 这种思路通常和循环深度、递归计算或测试时扩展计算一起出现。

- 相比显式 CoT，latent reasoning 更节省输出 token，也更适合表达难以自然语言化的中间过程。

- Coconut、Ouro、递归深度模型等工作都可归入这一方向。

## 来源引用

- [摘要：Mythos is a looped transformer!? 😳 Should be a Mixture-of-Recursions (MoR) — 2× faster, controlled effort.](summaries/摘要：Mythos is a looped transformer! 😳 Should be a Mixture-of-Recursions (MoR) — 2× faster, controlled effort.md)

## 关联概念

- [Mixture-of-Recursions](concepts/Mixture-of-Recursions.md)

- [Looped Transformer](concepts/Looped Transformer.md)

- [Adaptive Token Routing](concepts/Adaptive Token Routing.md)

- [Universal Transformer](concepts/Universal Transformer.md)

## 备注

- 这是理解“测试时多想几步但不多吐字”这类架构设计的核心术语。
