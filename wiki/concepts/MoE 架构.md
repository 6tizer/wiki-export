---
title: MoE 架构
type: concept
tags:
- LLM
status: 审核中
confidence: high
last_compiled: '2026-04-22'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/a9669a8629a347708a59fa2700716269
notion_id: a9669a86-29a3-4770-8a59-fa2700716269
---

## 定义

MoE（Mixture of Experts，混合专家）是一种模型架构，将参数分为多个「专家」模块，每次推理时只激活与当前输入最相关的少数专家，实现大参数量但低计算成本的高效推理。

## 核心要点

- 条件计算：不是每次都使用所有参数，而是通过路由机制选择最适合的专家

- 效率优势：总参数量大但激活参数少，如 Qwen3.5 的 397B/17B（总参/激活）

- 与线性注意力结合：Qwen3.5 使用 MoE + 线性注意力混合架构，进一步提升效率

- 吞吐量提升：在长上下文场景下优势明显，Qwen3.5 解码速度是密集模型的 7-19 倍

- 本地部署可行性：激活参数少使本地部署成为可能

## 关联概念

- [OpenMythos](entities/OpenMythos.md)

- [Claude Mythos](entities/Claude Mythos.md)

- [Recurrent-Depth Transformer](concepts/Recurrent-Depth Transformer.md)

- [自适应计算时间](concepts/自适应计算时间.md)

- [多潜在注意力](concepts/多潜在注意力.md)

- [Parcae 架构](concepts/Parcae 架构.md)

- [隐式思维链](concepts/隐式思维链.md)

- [Qwen3.6-35B-A3B](entities/Qwen3.6-35B-A3B.md)

- [Gemma4-26B-A4B](entities/Gemma4-26B-A4B.md)

- [Qwen3.5-27B](entities/Qwen3.5-27B.md)

- [混合注意力](concepts/混合注意力.md)

## 来源引用

- [摘要：OpenMythos：社区用开源代码重建 Claude Mythos 的循环深度 Transformer 假说](summaries/摘要：OpenMythos：社区用开源代码重建 Claude Mythos 的循环深度 Transformer 假说.md)（[原文](https://x.com/KyeGomezB/status/2045659150340723107)）

- [摘要：Gemma 4 全系列在 M5 Max 本地运行测评](summaries/摘要：Gemma 4 全系列在 M5 Max 本地运行测评.md)（[原文](https://x.com/googlegemma/status/2042310203845329311)，Gemma，2026-04）

- [摘要：Qwen3.5 开源多模态大模型](summaries/摘要：Qwen3.5 开源多模态大模型.md)（开源星探，2026-02-17）

- [摘要：OpenClaw杀出中国黑马——Step 3.5 Flash 与 Agent 时代](summaries/摘要：OpenClaw杀出中国黑马——Step 3.5 Flash 与 Agent 时代.md)（新智元，2026-02-28）

- Qwen3.6-35B-A3B：用3B的算力跑35B的智慧，阿里最强开源编程模型来了（[原文](https://x.com/Alibaba_Qwen/status/2044768734234243427)，Qwen，2026-04）

- [摘要：OpenMythos：开源复现 Claude Mythos！想研究"推理时可以深入思考"的模型？也许这是你最好的开源选择！](summaries/摘要：OpenMythos：开源复现 Claude Mythos！想研究推理时可以深入思考的模型？也许这是你最好的开源选择！.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzY5NzIxODM2MQ%3D%3D&mid=2247484602&idx=1&sn=48770b7f95580e4cee6d0027db347794&chksm=f53c2679a92de78400c852ff7bc6114b837ef81101bec148324968db0ce2f6ec182eac20d190#rd)）

- [摘要：都是你能部署的：Qwen3.6和Gemma4，谁更适合作为你的下一代本地MoE模型？](summaries/摘要：都是你能部署的：Qwen3.6和Gemma4，谁更适合作为你的下一代本地MoE模型？.md)（[原文](https://mp.weixin.qq.com/s?__biz=Mzg4MzYxODkzMg%3D%3D&mid=2247508057&idx=1&sn=623ac3d5cea6bb2fb7f65d8b28514e75&chksm=ce0870dc9fc80dacdba48c8c3e27ae39f6c6bb655f67fa6a631ff7b3946e041f012431b96de8#rd)）
