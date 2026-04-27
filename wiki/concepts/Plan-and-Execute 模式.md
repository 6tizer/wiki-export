---
title: Plan-and-Execute 模式
type: concept
tags:
- Harness 工程
status: 草稿
confidence: medium
last_compiled: '2026-04-27'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/0d66790ac9e5465f958f2207cc88b450
notion_id: 0d66790a-c9e5-465f-958f-2207cc88b450
---

## 定义

Plan-and-Execute 是一种 Agent 推理策略，与 ReAct 的逐步推理不同，它先一次性生成完整执行计划，再按序执行各步骤，不在每一步重新推理。

别名：Plan-then-Execute、Planner-Executor 模式

## 关键要点

- **先规划后执行**：Agent 在第一轮对任务做全局拆解，生成有序步骤列表；后续步骤只做执行，不消耗推理 token

- **速度优势**：在结构明确的有界任务上，Plan-and-Execute 可比 ReAct 快 3.6 倍，因为大多数步骤不需要重新推理

- **适用场景**：任务边界清晰、步骤可预判的工作流（批量数据处理、固定流程自动化等）

- **劣势**：缺乏 ReAct 的自适应能力，当中间步骤产生意外结果时，原计划可能失效；需要额外的 re-planning 机制来应对计划过期

- **与 ReAct 互补**：两者不是非此即彼的关系，而是在 adaptability（适应性）和 speed/predictability（速度/可预测性）之间的权衡选择

## 关联概念

- [ReAct Agent](concepts/ReAct Agent.md)

- [Agent Harness](concepts/Agent Harness.md)

## 来源引用

- [摘要：Design principles for building an Agent harness](summaries/摘要：Design principles for building an Agent harness.md)（[原文](https://x.com/akshay_pachaar/status/2047671145475068038)）
