---
title: 摘要：不只是DeepSeek V4，还有个万亿级大模型，训推全程国产芯片
type: summary
tags:
- 训练/微调
- 算力基础设施
- 商业/生态
status: 已审核
confidence: high
last_compiled: '2026-04-30'
source_tags: ''
source_article_url: https://www.notion.so/352701074b6881e1ab85d14f8b75b5a4
notion_url: https://www.notion.so/Tizer/6e2553b3665e426e8f6f4f3de55cdc42
notion_id: 6e2553b3-665e-426e-8f6f-4f3de55cdc42
---

## 一句话摘要

美团用全国产算力集群（5~6万张国产加速卡）训推出万亿参数级 MoE 大模型 LongCat-2.0-Preview，实现了业内首个「英伟达含量为零」的全流程国产化万亿模型训推。

## 关键洞察

- **全国产算力首次支撑万亿级模型**：LongCat-2.0-Preview（1.6T 总参数 / 48B 激活 / 1M 上下文）训推全程使用国产芯片，刷新国产算力规模上限

- **LongCat-Flash 是方法论预演**：去年开源的 560B Flash 模型技术报告中刻意回避「GPU」用词、优化显存到 60GB 以下、强调确定性计算——这些细节指向其训练已在国产芯片上完成

- **底层算子深度自研是关键**：团队在国产芯片上自研了确定性 FAG 算子（性能损失仅 5%）、确定性 Scatter 并行算子和 GEMM Tiling，这些是整网确定性训练的基础

- **架构创新降低硬件压力**：N-gram Embedding 将参数从专家层前移到 embedding 层，配合轻量稀疏注意力机制，同时降低通信和显存开销

- **路径分野比参数对齐更重要**：与 DeepSeek V4 同日发布、参数量级相当，但 DeepSeek V4 仅首发推理用国产算力，LongCat 则是训推全流程国产化

## 提取的概念

- [LongCat](entities/LongCat.md)

- [DeepSeek V4](entities/DeepSeek V4.md)

- [确定性训练](concepts/确定性训练.md)

- [N-gram Embedding](concepts/N-gram Embedding.md)

- [DORA](entities/DORA.md)

- [国产算力基础设施](concepts/国产算力基础设施.md)

## 原始文章信息

- **作者**：机器之心（编辑：Sia）

- **来源**：微信公众号

- **发布时间**：2026-04-30

- **链接**：[原文](https://mp.weixin.qq.com/s?__biz=MzA3MzI4MjgzMw%3D%3D&mid=2651031117&idx=1&sn=b9aacd983e393ee1ae42f2851c300de9&chksm=859d232aed1a7ffb25ee00767e0aad4a30b7afb686da93b07f98091e58cf2b2119f8c2cc1f66#rd)

## 个人评注

这篇文章对 Tizer 的内容管线有几个值得关注的点：

- **国产算力路线验证**：LongCat 证明国产芯片已能支撑最前沿任务，这对依赖国产算力的团队是重要信号

- **「用软件工程的勤奋弥补硬件生态的欠缺」** 这一思路与 OpenClaw 的 Harness 工程理念类似——通过系统层面的精细控制，在受限环境中达到生产级可靠性

- 确定性训练方法论可复用到更多需要严格可复现性的场景
