---
title: 摘要：OpenMythos：开源复现 Claude Mythos！想研究"推理时可以深入思考"的模型？也许这是你最好的开源选择！
type: summary
tags:
- LLM
- 开发工具
status: 已审核
confidence: high
last_compiled: '2026-04-20'
source_tags: ''
source_article_url: https://www.notion.so/348701074b688154a347e97010b45633
notion_url: https://www.notion.so/6d4b89c73fdc4fef861c4c6e9c0d7fdb
notion_id: 6d4b89c7-3fdc-4fef-861c-4c6e9c0d7fdb
---

## 一句话摘要

OpenMythos 以开源工程方式重建 Claude Mythos 的可能架构，把“推理时可以深入思考”落到可运行的循环深度 Transformer 方案上，并通过 ACT、MLA、MoE 与 Parcae 稳定化设计同时兼顾推理能力、显存占用与训练稳定性。

## 关键洞察

- Prelude → Recurrent Block → Coda 的三段式结构，把一部分“模型深度”转移为推理时的循环次数，实现训练较浅、推理可加深的思路。

- 循环块在每轮计算中重新注入编码后的输入，并叠加 loop index / LoRA 适配，目标是减少多轮递归时的状态漂移。

- Adaptive Computation Time 允许不同 token 按收敛程度提前停止，把更多计算预算留给真正困难的位置。

- Multi-Head Latent Attention 用更紧凑的 KV 表示替代标准注意力缓存，显著降低长序列推理的显存压力。

- Parcae / LTI 注入通过谱半径约束增强循环模型训练稳定性，让“推理时扩深”的设计更有工程落地性。

## 提取的概念

- [OpenMythos](entities/OpenMythos.md)

- [Claude Mythos](entities/Claude Mythos.md)

- [Recurrent-Depth Transformer](concepts/Recurrent-Depth Transformer.md)

- [自适应计算时间](concepts/自适应计算时间.md)

- [多潜在注意力](concepts/多潜在注意力.md)

- [MoE 架构](concepts/MoE 架构.md)

- [Parcae 架构](concepts/Parcae 架构.md)

## 原始文章信息

- 作者：AI开源提效指南

- 来源：微信

- 发布时间：2026-04-20 21:28

- 原文链接：[https://mp.weixin.qq.com/s?__biz=MzY5NzIxODM2MQ==&mid=2247484602&idx=1&sn=48770b7f95580e4cee6d0027db347794&chksm=f53c2679a92de78400c852ff7bc6114b837ef81101bec148324968db0ce2f6ec182eac20d190#rd](https://mp.weixin.qq.com/s?__biz=MzY5NzIxODM2MQ%3D%3D&mid=2247484602&idx=1&sn=48770b7f95580e4cee6d0027db347794&chksm=f53c2679a92de78400c852ff7bc6114b837ef81101bec148324968db0ce2f6ec182eac20d190#rd)

- 源文章页面：OpenMythos：开源复现 Claude Mythos！想研究"推理时可以深入思考"的模型？也许这是你最好的开源选择！

## 个人评注

这类项目很适合 Tizer 的内容流水线：一方面它能沉淀出“循环推理”“测试时计算扩展”“KV 缓存压缩”“训练稳定性”这类可复用概念节点，另一方面也能为 OpenClaw / HITL 后续持续追踪上游模型架构趋势提供更结构化的知识底座。
