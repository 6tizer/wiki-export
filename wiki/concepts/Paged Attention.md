---
title: Paged Attention
type: concept
tags:
- LLM
- 推理优化
status: 审核中
confidence: high
last_compiled: '2026-04-23'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/ee60b432712c4ace99aac287097c082c
notion_id: ee60b432-712c-4ace-99aa-c287097c082c
---

## 定义

Paged Attention 是一种 KV Cache 内存管理机制，它把原本需要连续存放的缓存拆成非连续的页块，并通过索引表定位所需块，从而减少显存碎片与浪费。

## 关键要点

- 大模型生成时需要反复读取历史 token 的 Key/Value 向量，KV Cache 会随上下文长度线性增长。

- 如果缓存必须连续分配，长上下文和多请求场景很容易导致显存碎片与内存浪费。

- Paged Attention 通过分页式管理缓存，让推理引擎按需加载所需块，而不是一次搬运整段缓存。

## 来源引用

- [摘要：Traditional ML Inference vs. LLM Inference](summaries/摘要：Traditional ML Inference vs. LLM Inference.md)（[原文](https://x.com/_avichawla/status/2026224423460843665)）

## 关联概念

- [KV Prefix Caching](concepts/KV Prefix Caching.md)

- [KV-aware routing](concepts/KV-aware routing.md)

- [MoE 架构](concepts/MoE 架构.md)
