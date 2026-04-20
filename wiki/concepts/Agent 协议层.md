---
title: Agent 协议层
type: concept
tags:
- Agent 编排
status: 草稿
confidence: medium
last_compiled: '2026-04-20'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/891bb693f6d94eeabb4c1f714231a3e9
notion_id: 891bb693-f6d9-4eea-bb4c-1f714231a3e9
---

## 定义

Agent 协议层是 Agent 与用户、其他 Agent、外部工具之间的交互契约层，用来约束消息格式、调用边界、失败处理与结果回传。

## 关键要点

- 它描述的是协作规则，而不是某个具体工具或模型能力

- 人机、Agent 间、Agent 与工具之间往往是三种不同的协议表面，各自有不同的失败模式

- 将协议层外置，有助于把沟通约束从临时 Prompt 中抽离成可维护的系统资产

## 关联概念

- [Agent Harness](concepts/Agent Harness.md)

- [Agent Skills](concepts/Agent Skills.md)

- [记忆分层架构](concepts/记忆分层架构.md)

- [MCP 协议](concepts/MCP 协议.md)

- [A2A 协议](concepts/A2A 协议.md)

- [Mediator 层](concepts/Mediator 层.md)

## 来源引用

- [摘要：Memory](summaries/摘要：Memory.md)（[原文](https://x.com/akshay_pachaar/status/2045510648474530263)）
