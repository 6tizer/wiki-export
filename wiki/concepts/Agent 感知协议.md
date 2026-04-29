---
title: Agent 感知协议
type: concept
tags:
- Harness 工程
status: 草稿
confidence: medium
last_compiled: '2026-04-30'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/4bdc544eeb1345e48857c7b287f447da
notion_id: 4bdc544e-eb13-45e4-8857-c7b287f447da
---

## 定义

Agent 感知协议是一类标准化 AI Agent 如何接收外部世界实时数据的协议规范。其核心理念：Agent 不应被动等待用户输入，而应通过结构化的感知层（Perception Layer）主动获取环境信号，实现从「被动响应」到「主动行动」的跃迁。

## 关键要点

- **World → Sensor → Agent 范式**：将感知分为三层——世界（数据源）、传感器（结构化采集）、Agent（决策执行），三者通过统一信号格式解耦

- **与 MCP 协议的关系**：MCP 解决 Agent ↔ 工具的双向交互；感知协议解决 World → Agent 的单向数据流。两者互补，分别覆盖「行动」和「感知」

- **可组合性**：传感器以标准包形式分发（如 npm），可自由组合、替换，降低 Agent 与特定数据源的耦合

- **代表实现**：World2Agent（W2A）是目前该范式的首个开源实现

## 关联概念

- [World2Agent](entities/World2Agent.md)

- [Proactive Agents](concepts/Proactive Agents.md)

## 来源引用

- [摘要：World → Sensor → Agent](summaries/摘要：World → Sensor → Agent.md)（[原文](https://x.com/hasantoxr/status/2049472203620815334)）
