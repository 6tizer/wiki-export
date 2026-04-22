---
title: Linearized RL
type: concept
tags:
- Agent 编排
status: 草稿
confidence: medium
last_compiled: '2026-04-20'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/809ea4d5e11040f190d9fcb07217931d
notion_id: 809ea4d5-e110-40f1-90d9-fcb07217931d
---

## 定义

Linearized RL 是 Teknium 用来描述的一种 Agent 学习范式：把传统强化学习里“多次运行、挑出优胜轨迹、再做训练”的流程，压缩到单次 Agent loop 内完成求解、沉淀与复用。

## 关键要点

- 它关注的不是参数更新，而是把一次成功任务转成可复用的技能与上下文经验

- 核心收益是某类任务一旦被解决，后续执行就会显著提效

- 它借用了后训练强化学习的选择逻辑，但把学习发生点前移到测试时与运行时

- 这种方法更像“运行中锁定经验”，而不是传统意义上的权重微调

## 来源引用

- [摘要：Interesting insights, especially this: Hermes starts off as any other agent does, inefficient and often not sure how to complete a task that is training didnt have priors for. However, solve it once a](summaries/摘要：Interesting insights, especially this- Hermes starts off as any other agent does, inefficient and often not sure how to complete a task that is training didnt have priors for. However, solve it once a.md)（[原文](https://x.com/Teknium/status/2046001396819067008)）

## 关联概念

- [Hermes Agent](entities/Hermes Agent.md)

- [Test-time Training](concepts/Test-time Training.md)

- [技能自我进化](concepts/技能自我进化.md)

- [Agent Skills](concepts/Agent Skills.md)

- [Agent Harness](concepts/Agent Harness.md)
