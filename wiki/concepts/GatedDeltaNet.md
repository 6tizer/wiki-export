---
title: GatedDeltaNet
type: concept
tags:
- LLM
status: 审核中
confidence: medium
last_compiled: '2026-04-23'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/7e01f6f540fd4460a6437418687acdd6
notion_id: 7e01f6f5-40fd-4460-a643-7418687acdd6
---

## 定义

GatedDeltaNet 是一种带递推状态的混合层结构。在这篇资料涉及的 Qwen 3.5 27B 架构中，它与全注意力层并存，因此树形验证不仅要处理 attention mask，还要处理沿父节点分叉的状态传递。

## 关键要点

- 文中提到 Qwen 3.5 27B 由 48 层 GatedDeltaNet 与 16 层全注意力层组成，属于 hybrid model。

- 对 DDTree 这类树状 speculative decoding 来说，难点不只是候选树本身，还包括递推状态如何在分支处正确 fork 与 commit。

- 项目通过自定义 Metal kernel 处理 parent-indexed recurrence，说明本地推理优化已经深入到算子级实现。

- 这个概念的价值在于提醒工程侧：支持 hybrid model 往往比支持纯 attention 模型更复杂。

## 来源引用

- [摘要：Tree-based speculative decoding for Apple Silicon.](summaries/摘要：Tree-based speculative decoding for Apple Silicon.md)（[原文](https://x.com/QingQ77/status/2045500092527087861)）

## 关联概念

- [DDTree](concepts/DDTree.md)

- [Tree Attention](concepts/Tree Attention.md)

- [Qwen3.5-27B](entities/Qwen3.5-27B.md)
