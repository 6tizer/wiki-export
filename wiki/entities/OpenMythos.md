---
title: OpenMythos
type: entity
tags:
- LLM
- 开发工具
status: 审核中
confidence: high
last_compiled: '2026-04-20'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/2b1c45c16ddf4ad8b6eb359c9b3dcd1b
notion_id: 2b1c45c1-6ddf-4ad8-b6eb-359c9b3dcd1b
---

## 定义

OpenMythos 是一个用 PyTorch 实现的开源实验项目，目标是以工程化方式复现 Claude Mythos 可能采用的循环深度 Transformer 架构假说。

## 关键要点

- 项目采用 Prelude → Recurrent Block → Coda 的三段式结构。

- 核心设计是通过重复执行同一组权重，把推理深度转移到循环次数上。

- 循环块中结合了 MoE 机制，以较少激活参数获得更高计算效率。

- 项目在发布后短时间内获得大量社区关注，说明这类“可运行假说”具备很强传播性。

## 关联概念

- [Claude Mythos](entities/Claude Mythos.md)

- [Recurrent-Depth Transformer](concepts/Recurrent-Depth Transformer.md)

- [自适应计算时间](concepts/自适应计算时间.md)

- [多潜在注意力](concepts/多潜在注意力.md)

- [MoE 架构](concepts/MoE 架构.md)

- [Parcae 架构](concepts/Parcae 架构.md)

## 来源引用

- [摘要：OpenMythos：社区用开源代码重建 Claude Mythos 的循环深度 Transformer 假说](summaries/摘要：OpenMythos：社区用开源代码重建 Claude Mythos 的循环深度 Transformer 假说.md)（[原文](https://x.com/KyeGomezB/status/2045659150340723107)）

- 摘要：OpenMythos：开源复现 Claude Mythos！想研究"推理时可以深入思考"的模型？也许这是你最好的开源选择！（[原文](https://mp.weixin.qq.com/s?__biz=MzY5NzIxODM2MQ%3D%3D&mid=2247484602&idx=1&sn=48770b7f95580e4cee6d0027db347794&chksm=f53c2679a92de78400c852ff7bc6114b837ef81101bec148324968db0ce2f6ec182eac20d190#rd)）
