---
title: Supervisor 模式
type: concept
tags:
- 多Agent协作
- Agent 协作模式
status: 草稿
confidence: medium
last_compiled: '2026-04-28'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/a59d6f2eb12348649d1db09748486688
notion_id: a59d6f2e-b123-4864-9d1d-b09748486688
---

## 定义

Supervisor 模式是多 Agent 系统中的一种经典编排架构，由一个中央 Supervisor Agent 负责任务分解、分配和结果汇总，下属多个专业化子 Agent 各自执行特定任务。

## 关键要点

- **中央协调**：Supervisor 持有任务计划，将任务分解后分发给专业化子 Agent（检索器、编码器、分析器、摘要器等）

- **共享内存总线**：子 Agent 通过共享状态/消息总线与 Supervisor 通信

- **可还原为原语**：在 Worker 模式视角下，Supervisor 模式本质上只是一个 Function 调用其他 Function 的触发器组合，而非独立架构

- **成本问题**：如果所有节点都用最贵模型，成本会指数级上升（如 Claude Code 单会话 $11.55 的案例）

- **与 Swarm 模式互补**：Supervisor 是集中式协调，Swarm 是去中心化状态触发

## 来源引用

- [摘要：Agents 201: The Unit Shrank](summaries/摘要：Agents 201- The Unit Shrank.md)（[原文](https://x.com/ghumare64/status/2047401813364683007)）

## 关联概念

- [iii](entities/iii.md)

- [Worker 模式](concepts/Worker 模式.md)

- [Agent Swarms](concepts/Agent Swarms.md)
