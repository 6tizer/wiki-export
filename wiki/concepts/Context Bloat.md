---
title: Context Bloat
type: concept
tags: []
status: 审核中
confidence: medium
last_compiled: '2026-04-27'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/4f32c3a33da14f8587a5ed3f679dcffa
notion_id: 4f32c3a3-3da1-4f85-87a5-ed3f679dcffa
---

## 定义

Context Bloat 指 Agent 在执行任务时，被过多技能描述、规则说明、工具清单或中间状态占满上下文窗口，导致选择变慢、判断变差、路由失真。

## 关键要点

- 常见诱因是技能拆分过细、resolver 过长，以及把大量本可按需加载的说明一次性塞进上下文。

- 直接后果包括误选 skill、误调用工具、分支判断混乱，以及执行延迟上升。

- 它不是单纯的 token 变多，而是无关上下文占比过高，稀释了真正有用的信号。

- 常见缓解方法包括合并相邻 skills、参数化分支、缩短 resolver，并把更多决策交给按需加载机制。

## 来源引用

- [摘要：skills](summaries/摘要：skills.md)（[原文](https://x.com/garrytan/status/2047183884266402275)）

- [摘要：Exa now reduces input tokens for web agents by 96%](summaries/摘要：Exa now reduces input tokens for web agents by 96%.md)（[原文](https://x.com/ExaAILabs/status/2047402544260116517)）

## 关联概念

- [Thin Harness, Fat Skills](concepts/Thin Harness, Fat Skills.md)

- [Resolver](concepts/Resolver.md)

- [Skill Graph](concepts/Skill Graph.md)
