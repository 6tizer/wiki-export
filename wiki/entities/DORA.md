---
title: DORA
type: entity
tags:
- 训练/微调
status: 草稿
confidence: medium
last_compiled: '2026-04-30'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/4ed59278285e463599c26316d918047d
notion_id: 4ed59278-285e-4635-99c2-6316d918047d
---

## 定义

DORA 是美团 LongCat 团队开源的异步训练框架，专门针对国产芯片环境（中等性能加速卡、约 60GB 可用显存）下的大规模 MoE 模型训练进行优化。

## 关键要点

- 论文中明确提到：「our production cluster consists of midrange accelerators, especially with only around 60GB of available device memory」

- 针对显存受限的国产加速卡环境设计异步训练策略

- 与 V-ZB 算法配合，将训练峰值显存压到 60GB 以下

- 已开源，是 LongCat 全国产训练工程栈的关键组件之一

## 来源引用

- [摘要：不只是DeepSeek V4，还有个万亿级大模型，训推全程国产芯片](summaries/摘要：不只是DeepSeek V4，还有个万亿级大模型，训推全程国产芯片.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzA3MzI4MjgzMw%3D%3D&mid=2651031117&idx=1&sn=b9aacd983e393ee1ae42f2851c300de9&chksm=859d232aed1a7ffb25ee00767e0aad4a30b7afb686da93b07f98091e58cf2b2119f8c2cc1f66#rd)）

## 关联概念

- [LongCat](entities/LongCat.md)

- [确定性训练](concepts/确定性训练.md)

- [N-gram Embedding](concepts/N-gram Embedding.md)
