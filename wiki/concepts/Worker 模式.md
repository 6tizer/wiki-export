---
title: Worker 模式
type: concept
tags:
- 多Agent协作
- Agent 协作模式
status: 草稿
confidence: medium
last_compiled: '2026-04-28'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/0a3b4e6511a648fa943a51b3482aff5d
notion_id: 0a3b4e65-11a6-48fa-943a-51b3482aff5d
---

## 定义

Worker 模式是一种多 Agent 系统架构范式，主张将「Agent」从单一整体拆解为多个职责单一的 Worker（工作单元）。每个 Worker 有明确身份、定义的输入输出、只做一件事，Agent 是这些 Worker 组合的结果而非预先构建的整体。

核心转变：原子单元从 "Agent" 变为 "Worker"。

## 关键要点

- **窄范围原则**：一个 Worker 只负责一个职责——检索器只检索、验证器只验证、摘要器只摘要。"Boring is the feature"

- **可替换性**：每个 Worker 独立可测试、可基准化、可替换模型，不影响调用方

- **分层模型分配**：不同 Worker 可使用不同成本/能力的模型（如 Haiku 做 Worker、Opus 做编排），解决 Token 经济问题

- **关注点提取**：当发现瓶颈时，从现有 Worker 中提取一个关注点为新 Worker，调用方式不变

- **组合优于预构建**：Agent 不是你构建的东西，而是组合正常运作时你对它的称呼

## 与 Monolithic Agent 的对比

Monolithic Agent 在生产环境中面临三个问题：

1. **Token 经济**：一个 Agent 协调四个子 Agent 使用最贵模型，15K token 任务变 60K

1. **专业化损失**：一个模型同时充当路由器、编码器、审查器、摘要器，哪个都不擅长

1. **Vibes 调试**：当 Supervisor 和 Worker 共享状态时，出错只能重跑碰运气

## 来源引用

- [摘要：Agents 201: The Unit Shrank](summaries/摘要：Agents 201- The Unit Shrank.md)（[原文](https://x.com/ghumare64/status/2047401813364683007)）

## 关联概念

- [iii](entities/iii.md)

- [Supervisor 模式](concepts/Supervisor 模式.md)

- [Agent Swarms](concepts/Agent Swarms.md)
