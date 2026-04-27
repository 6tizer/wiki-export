---
title: DeepSeek Sparse Attention
type: concept
tags:
- 推理优化
- 上下文管理
status: 草稿
confidence: medium
last_compiled: '2026-04-27'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/990921d65bde4c04b842b35149c5c00e
notion_id: 990921d6-5bde-4c04-b842-b35149c5c00e
---

## 定义

DeepSeek Sparse Attention（DSA）是 DeepSeek 在 V4 系列模型中引入的新型稀疏注意力机制，旨在大幅降低超长上下文（1M token）场景下的内存与计算开销，实现低成本的百万级上下文推理。

## 关键要点

- 专为 1M token 上下文窗口设计，显著降低长上下文推理的内存和计算成本

- 与 MoE 架构配合使用，在 DeepSeek-V4-Pro（1.6T/49B）和 V4-Flash（284B/13B）上均有部署

- 使百万级上下文从高端闭源模型独占能力变为开源可用的标配

## 关联概念

- [DeepSeek V4](entities/DeepSeek V4.md)

- [MoE 架构](concepts/MoE 架构.md)

- [1M 上下文](concepts/1M 上下文.md)

## 来源引用

- [摘要：DeepSeek-V4 Preview 正式发布并开源，开启低成本百万上下文时代](summaries/摘要：DeepSeek-V4 Preview 正式发布并开源，开启低成本百万上下文时代.md)（[原文](https://x.com/deepseek_ai/status/2047516922263285776)）
