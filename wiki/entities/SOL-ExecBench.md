---
title: SOL-ExecBench
type: entity
tags:
- 模型评测
- 多Agent协作
- 算力基础设施
status: 审核中
confidence: high
last_compiled: '2026-04-15'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/b56dd16ef2984be59e49ccff8695aeed
notion_id: b56dd16e-f298-4be5-9e49-ccff8695aeed
---

## 定义

SOL-ExecBench 是 NVIDIA 在本文中使用的问题生成与性能评测基准，用来从真实生产模型里抽取 CUDA 内核优化任务，并用统一标准衡量 agent 生成方案的效果。

## 关键要点

- 它从 124 个开源生产模型中生成了 235 个真实优化问题，而不是玩具样例

- 它同时承担 benchmark 与约束检查的角色，会用理论硬件上限过滤明显不可信的结果

- 这使多智能体系统的优化表现可以被量化比较，而不只是停留在案例叙事

## 关联概念

- [Agent Harness](concepts/Agent Harness.md)

- [Cursor](entities/Cursor.md)

## 来源引用

- [原文链接](https://cursor.com/blog/multi-agent-kernels)｜《Speeding up GPU kernels by 38% with a multi-agent system》｜源文章：Cursor × NVIDIA：多智能体系统用 3 周把 CUDA kernel 加速了 38%
