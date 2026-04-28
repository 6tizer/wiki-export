---
title: check-resolvable
type: concept
tags:
- Agent 编排
- Coding Agent
status: 审核中
confidence: medium
last_compiled: '2026-04-20'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/1dc4db4f6f6847da9b82995aff5d5d3d
notion_id: 1dc4db4f-6f68-47da-9b82-995aff5d5d3d
---

## 定义

check-resolvable 是一种面向 Agent 系统的元技能 / 审计机制，用来检查某个 skill、流程或代码路径，是否真的能从 resolver 出发被用户请求命中并执行。

## 关键要点

- 它关注的不是技能是否存在，而是技能是否 **可达**

- 可以沿着 `AGENTS.md → skill file → code path` 逐层检查调用链是否连通

- 能发现“系统已经具备能力，但 resolver 没登记触发条件”的暗能力问题

- 适合作为定期巡检工具，提前暴露路由断裂，而不是等用户在关键时刻踩坑

## 关联概念

- [Resolver](concepts/Resolver.md)

- [Thin Harness, Fat Skills](concepts/Thin Harness, Fat Skills.md)

- [Trigger Evals](concepts/Trigger Evals.md)

- [Skillify](concepts/Skillify.md)

## 来源引用

- [摘要：Resolvers: The Routing Table for Intelligence](summaries/摘要：Resolvers- The Routing Table for Intelligence.md)（[原文](https://x.com/garrytan/status/2044479509874020852)）

- [摘要：How to really stop your agents from making the same mistakes](summaries/摘要：How to really stop your agents from making the same mistakes.md)（[原文](https://x.com/garrytan/status/2046876981711769720)）
