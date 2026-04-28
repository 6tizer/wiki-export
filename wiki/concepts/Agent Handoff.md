---
title: Agent Handoff
type: concept
tags:
- Agent 编排
status: 审核中
confidence: high
last_compiled: '2026-04-20'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/d69631b44eaa420da11e136d42b16f30
notion_id: d69631b4-4eaa-420d-a11e-136d42b16f30
---

## 定义

Agent Handoff 是多 Agent 系统中的任务交接机制：当当前 Agent 判断某个问题超出自身职责范围时，把控制权转交给更适合处理该任务的另一个 Agent。

## 关键要点

- 它强调按职责边界做动态转交，而不是把所有路由逻辑硬编码在外层工作流里。

- 这种机制让多 Agent 协作更接近“专家接力”，便于把复杂任务拆给不同角色处理。

- 相比固定图编排，handoff 更突出运行时判断与 Agent 自主决策。

- 在 OpenAI Agents SDK 里，Handoff 与 Agent、Tracing 一起构成最核心的三类原语。

## 来源引用

- [摘要：OpenAI Agents SDK：三个原语，搭出你的多 Agent 系统](summaries/摘要：OpenAI Agents SDK：三个原语，搭出你的多 Agent 系统.md)（[原文](https://x.com/_vmlops/status/2045533747857240290)）

## 关联概念

- [OpenAI Agents SDK](entities/OpenAI Agents SDK.md)

- [Agent Traces](concepts/Agent Traces.md)

- [会话记忆](concepts/会话记忆.md)
