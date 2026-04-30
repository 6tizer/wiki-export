---
title: N-gram Embedding
type: concept
tags:
- 推理优化
- 训练/微调
status: 草稿
confidence: medium
last_compiled: '2026-04-30'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/c1033428b54a4cba9b7a9d6b52723a74
notion_id: c1033428-b54a-4cba-9b7a-9d6b52723a74
---

## 定义

N-gram Embedding 是 LongCat 模型系列（由美团提出）中的一种架构创新，将传统 MoE 模型中部分原本位于 FFN 专家层的参数前移至 embedding 层，并引入 N-gram（词组级）建模能力，使高频语言模式可以在 embedding 层直接匹配命中，减少对逐层专家计算的依赖。

## 关键要点

- 传统 MoE 模型依赖扩展 FFN 专家数量提升能力，但跨节点通信开销随专家数量线性增长

- N-gram Embedding 将部分参数从专家层前移至 embedding 层，降低跨节点通信压力

- 在 LongCat-Flash-Lite 中首次验证，LongCat-2.0-Preview 中继续增强

- 效果：保持 1.6T 参数容量的同时，在代码生成、指令理解与专业语义任务中获得更稳定表现，推理成本得到控制

## 来源引用

- [摘要：不只是DeepSeek V4，还有个万亿级大模型，训推全程国产芯片](summaries/摘要：不只是DeepSeek V4，还有个万亿级大模型，训推全程国产芯片.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzA3MzI4MjgzMw%3D%3D&mid=2651031117&idx=1&sn=b9aacd983e393ee1ae42f2851c300de9&chksm=859d232aed1a7ffb25ee00767e0aad4a30b7afb686da93b07f98091e58cf2b2119f8c2cc1f66#rd)）

## 关联概念

- [LongCat](entities/LongCat.md)

- [确定性训练](concepts/确定性训练.md)

- [DORA](entities/DORA.md)
