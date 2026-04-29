---
title: Agent RL
type: concept
tags:
- 训练/微调
- Harness 工程
status: 草稿
confidence: medium
last_compiled: '2026-04-29'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/68ba0a136a3d4c3abc734f74c63ccf61
notion_id: 68ba0a13-6a3d-4c3a-bc73-4f74c63ccf61
---

## 定义

Agent RL（Agent Reinforcement Learning）是一种专门针对 AI Agent 行为进行强化学习训练的方法，通过在真实代码执行沙箱中生成 trajectory、评分和过滤来优化模型的 agentic 编码能力。

## 关键要点

- **异步离策略**（Async Off-Policy）：Poolside 的 Agent RL 栈采用异步离策略架构，松耦合推理生成、沙箱执行编排、trajectory 评分、缓冲过滤和分布式训练等核心组件

- **训练流程**：模型在预训练和后训练之后进入 Agent RL 阶段，在 Poolside 自有的 agent harness 中进行实际编码任务的强化学习

- **核心思想**：不仅训练模型生成代码，更训练模型在长时域任务中的工具调用、推理交织和决策能力

- **应用场景**：用于提升模型在 SWE-bench 等真实软件工程基准上的表现

## 来源引用

- [摘要：Today we're releasing Laguna XS.2, Poolside's first open-weight model.](summaries/摘要：Today we're releasing Laguna XS.2, Poolside's first open-weight model.md)（[原文](https://x.com/poolsideai/status/2049144111626670282)）

## 关联概念

- [Laguna XS.2](entities/Laguna XS.2.md)

- [Poolside](entities/Poolside.md)

- [Data Automixing](concepts/Data Automixing.md)

- [Shimmer](entities/Shimmer.md)
