---
title: Memory-Layered Context
type: concept
tags:
- 记忆系统
- Agent 编排
status: 审核中
confidence: high
last_compiled: '2026-04-23'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/06964a6c47184f10abc389694d3fab8b
notion_id: 06964a6c-4718-4f10-abc3-89694d3fab8b
---

**定义**：Memory-Layered Context 是一种把长时运行智能体的上下文拆分为不同记忆层级的设计思路，让 agent 同时拥有长期记忆、工作记忆与组织级上下文治理能力。

### 关键要点

- 长期运行的 agent 不能只依赖单次会话状态，还需要跨会话的可持续记忆层。

- 记忆不仅要能写入和检索，还要防止 memory drift、跨流程污染与越权访问。

- 这一模式通常需要与身份、注册与网关等治理组件配合使用。

### 来源引用

- [摘要：5 Agent Design patterns for Long-running AI Agents](summaries/摘要：5 Agent Design patterns for Long-running AI Agents.md)（[原文](https://x.com/GoogleCloudTech/status/2046989964077146490)）
