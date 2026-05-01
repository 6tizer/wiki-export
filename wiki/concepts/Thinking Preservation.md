---
title: Thinking Preservation
type: concept
tags:
- 推理优化
- 长期记忆
- 上下文管理
status: 审核中
confidence: medium
last_compiled: '2026-04-23'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/4370331d302e46b48fd08e765647fd1e
notion_id: 4370331d-302e-46b4-8fd0-8e765647fd1e
---

## 定义

Thinking Preservation 是 Qwen3.6 引入的一项能力设定，用来在多轮任务中保留历史推理上下文，使模型在长周期、多步骤决策过程中不容易出现推理断裂或“失忆”。

## 关键要点

- 核心目标不是扩展总上下文长度，而是让模型在连续任务中更稳定地延续先前的思考轨迹

- 这一能力特别适合 Agent 执行、复杂任务拆解、代码修复与多轮工具调用场景

- 它代表了模型优化重点从单轮回答质量，转向长流程任务可持续性

## 来源引用

- [摘要：都是你能部署的：Qwen3.6和Gemma4，谁更适合作为你的下一代本地MoE模型？](summaries/摘要：都是你能部署的：Qwen3.6和Gemma4，谁更适合作为你的下一代本地MoE模型？.md)（[原文](https://mp.weixin.qq.com/s?__biz=Mzg4MzYxODkzMg%3D%3D&mid=2247508057&idx=1&sn=623ac3d5cea6bb2fb7f65d8b28514e75&chksm=ce0870dc9fc80dacdba48c8c3e27ae39f6c6bb655f67fa6a631ff7b3946e041f012431b96de8#rd)）

- [摘要：Qwen3.6-27B](summaries/摘要：Qwen3.6-27B.md)（[原文](https://x.com/Alibaba_Qwen/status/2046939764428009914)）

## 关联概念

- [Agentic Coding](concepts/Agentic Coding.md)

- [Qwen3.6-35B-A3B](entities/Qwen3.6-35B-A3B.md)

- [Qwen3.6-27B](entities/Qwen3.6-27B.md)
