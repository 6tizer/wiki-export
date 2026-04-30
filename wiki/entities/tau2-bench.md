---
title: tau2-bench
type: entity
tags:
- 模型评测
status: 草稿
confidence: medium
last_compiled: '2026-04-30'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/18fe1b506115471182dbc664ad8a54fe
notion_id: 18fe1b50-6115-4711-82db-c664ad8a54fe
---

## 定义

tau2-bench 是一个用于评估 LLM Agent 多轮工具调用与指令遵循能力的基准测试套件。它专注于 Agent 在复杂多步骤任务中的表现，常被用于衡量 harness 层面的工程改进对 Agent 性能的实际影响。

## 关键要点

- **评测维度**：多轮工具调用（multi-turn tool use）+ 指令遵循（instruction following）

- **难度分层**：包含精选的高难度任务子集，前沿模型尚未饱和，更适合度量 harness 级别变化的影响

- **实际应用**：Deep Agents 团队使用 tau2-bench 子集验证 Harness Profile 的效果，观察到启用模型特定 Profile 后性能提升 10-20 个百分点

## 关联概念

- [Deep Agents](entities/Deep Agents.md)

- [Harness Profile](concepts/Harness Profile.md)

- [Terminal-Bench 2.0](entities/Terminal-Bench 2.0.md)

## 来源引用

- [摘要：Tuning Deep Agents to Work Well with Different Models](summaries/摘要：Tuning Deep Agents to Work Well with Different Models.md)（[原文](https://x.com/Vtrivedy10/status/2049535740233523600)）
