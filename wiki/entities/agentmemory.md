---
title: agentmemory
type: entity
tags:
- 记忆系统
- Coding Agent
status: 草稿
confidence: high
last_compiled: '2026-04-20'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/166de7d4ee3446c5bea8a1e9d0cd2430
notion_id: 166de7d4-ee34-46c5-bea8-a1e9d0cd2430
---

## 定义

agentmemory 是一个面向 AI Coding Agent 的持久化记忆层与记忆服务器，目标是把长期记忆从具体 harness 中解耦出来，让 Claude Code、Cursor、Gemini CLI、OpenCode 等不同代理共享同一套可迁移的上下文资产。

## 关键要点

- 它把记忆定位为独立基础设施，而不是某个单一 Agent 框架的附属功能

- 检索层结合 BM25、向量检索、知识图谱与 RRF 融合，以兼顾关键词命中、语义召回与结构关系

- 注入层强调 token 预算控制、记忆衰减与置信度评分，减少上下文膨胀和记忆污染

- 它的核心价值是让用户在更换 harness 时，尽可能保留已积累的长期上下文

## 关联概念

- [Agent Harness](concepts/Agent Harness.md)

- [持久化跨会话记忆](concepts/持久化跨会话记忆.md)

- [混合检索](concepts/混合检索.md)

- [RRF 融合检索](concepts/RRF 融合检索.md)

- [Memory Lock-in](concepts/Memory Lock-in.md)

## 来源引用

- [摘要：local-first AI assistant built for personal AI sovereignty](summaries/摘要：local-first AI assistant built for personal AI sovereignty.md)（[原文](https://x.com/ghumare64/status/2045291112454402194)）
