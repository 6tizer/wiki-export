---
title: LongCat
type: entity
tags:
- 训练/微调
- 算力基础设施
- AI 产品
status: 草稿
confidence: high
last_compiled: '2026-04-30'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/a3dc5dbc15064ddab720eb5806d859ba
notion_id: a3dc5dbc-1506-4dda-b720-eb5806d859ba
---

## 定义

LongCat 是美团自研的大语言模型系列，采用 MoE（Mixture of Experts）架构。该系列的核心特点是训推全流程基于国产芯片完成，英伟达算力占比为零，是业内首个实现全国产算力支撑万亿参数级模型训推的项目。

**别名/版本线**：LongCat-Flash（560B，2025年9月开源）→ LongCat-Flash-Lite → LongCat-2.0-Preview（1.6T，2026年4月）

## 关键要点

- LongCat-2.0-Preview 总参数约 1.6T，平均激活参数约 48B，支持 1M 级超长上下文

- LongCat-Flash 总参数 560B，动态激活参数 186~313B，是 2.0 的工程验证前身

- 训练使用 5~6 万张国产加速卡，刷新国产算力支撑超大模型训练的规模上限

- 架构创新包括 N-gram Embedding（将参数前移至 embedding 层）和轻量稀疏注意力机制

- 团队自研了确定性 FlashAttention 反向梯度算子、Scatter 并行算子、确定性 GEMM Tiling 等底层组件

- 开源了 DORA 异步训练框架

- LongCat-2.0-Preview 处于受邀内测阶段，每天 1000 万 token 额度

## 来源引用

- [摘要：不只是DeepSeek V4，还有个万亿级大模型，训推全程国产芯片](summaries/摘要：不只是DeepSeek V4，还有个万亿级大模型，训推全程国产芯片.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzA3MzI4MjgzMw%3D%3D&mid=2651031117&idx=1&sn=b9aacd983e393ee1ae42f2851c300de9&chksm=859d232aed1a7ffb25ee00767e0aad4a30b7afb686da93b07f98091e58cf2b2119f8c2cc1f66#rd)）

## 关联概念

- [DeepSeek V4](entities/DeepSeek V4.md)

- [确定性训练](concepts/确定性训练.md)

- [N-gram Embedding](concepts/N-gram Embedding.md)

- [DORA](entities/DORA.md)

- [国产算力基础设施](concepts/国产算力基础设施.md)
