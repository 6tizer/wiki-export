---
title: LLM-Driven Replan
type: concept
tags:
- Agent 编排
status: 草稿
confidence: medium
last_compiled: '2026-04-20'
source_tags: Multi-Agent, Agent, 自动化, LLM
source_article_url: https://www.notion.so/348701074b68811e9eddc16eb1202200
notion_url: https://www.notion.so/e54787b6278948bd9c8dd5fe21857cc0
notion_id: e54787b6-2789-48bd-9c8d-d5fe21857cc0
---

## 定义

LLM-Driven Replan 是一种由大模型依据执行结果动态调整后续计划的编排机制：当子 Agent 失败或返回异常状态时，父 Agent 不是机械重试，而是基于状态、退出原因与工具轨迹重新规划执行路径。

## 关键要点

- 将基础设施层的自动重试与编排层的策略重规划分开处理，避免把所有失败都当成同一种错误

- 父 Agent 可以根据 status、exit_reason、tool_trace 等结构化结果判断是换路径、缩小范围还是改目标

- 这种机制提升了多 Agent 系统的故障自愈能力，比单纯“失败就重跑”更节省预算

- 它本质上把失败结果也变成了可推理的上下文输入

## 来源引用

- [摘要：Hermes 多 Agent 深水区：三个高级实战技巧](summaries/摘要：Hermes 多 Agent 深水区：三个高级实战技巧.md)（[原文](https://x.com/BTCqzy1/status/2045720855137903046)）

## 关联概念

- [Hermes Agent](entities/Hermes Agent.md)

- [delegate_task](concepts/delegate_task.md)

- [Stateless Ephemeral Unit](concepts/Stateless Ephemeral Unit.md)

- [Subdirectory Hints](concepts/Subdirectory Hints.md)
