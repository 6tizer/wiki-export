---
title: Agent 对等通信
type: concept
tags:
- 多Agent协作
- Agent 协作模式
status: 草稿
confidence: medium
last_compiled: '2026-04-28'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/0efb067c0e414779aec9c5143c0372bb
notion_id: 0efb067c-0e41-4779-aec9-c5143c0372bb
---

## 定义

Agent 对等通信（Peer-to-Peer Agent Communication）是一种 Agent 间通信模式，区别于传统的主从式任务委托（delegate_task / spawn 子 agent）。在对等通信中，两个 Agent 拥有各自独立的记忆、上下文和判断力，以平等身份进行信息交换和协作。

## 关键要点

- **对等 vs 主从**：传统 multi-agent 框架多采用 orchestrator → worker 模式（spawn 子 agent 干完活就消失）；对等通信则让每个 Agent 保持独立身份和持久 session

- **Session 注入**：消息注入到对方正在活着的 session 中，回复来自 Agent 本体而非临时副本

- **上下文互补**：不同 Agent 拥有不同的原生 Context，对等交流可以产生多角度见解（如 Claude Code 和 Hermes Agent 互相 code review）

- **隐私边界**：对等通信天然支持隐私隔离，各 Agent 只暴露选择性信息

- **实现方式**：可基于 Google A2A 协议、自定义 webhook 等机制实现

## 与相关概念的区别

- **delegate_task**：上下级关系，子 agent 完成任务后消失

- **Agent 对等通信**：平等关系，双方都保持持久状态

- **群聊协作**：多 Agent 在同一频道交流，对等通信更偏向 1:1 session 注入

## 来源引用

- [摘要：Hermes-a2a](summaries/摘要：Hermes-a2a.md)（[原文](https://x.com/0xViviennn/status/2047626457191780527)）

## 关联概念

- [hermes-a2a](entities/hermes-a2a.md)

- [A2A 协议](concepts/A2A 协议.md)

- [Hermes Agent](entities/Hermes Agent.md)

- [Context Compaction](concepts/Context Compaction.md)
