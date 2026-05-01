---
title: Claude Code 动态循环
type: concept
tags: []
status: 审核中
confidence: medium
last_compiled: '2026-04-13'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/dfa2256ce1164cbcb9a9d2fb183827b9
notion_id: dfa2256c-e116-4cbc-b9a9-d2fb183827b9
---

## 定义

Claude Code 动态循环是 Claude Code 对 `/loop` 能力的一种增强执行模式。在不显式指定轮询间隔时，系统会根据任务所处阶段动态决定下一次检查时间，并在合适场景下直接转向事件驱动监控。

## 关键要点

- 不再依赖固定间隔轮询，而是根据任务进展进行动态调度

- 可结合 Monitor 工具，在后台挂起轻量监控脚本，只在真正发生事件时再唤醒 Agent

- 能明显减少无效等待与空转调用，降低长时任务的 token 消耗

- 适合 CI/CD 检查、日志巡检、部署观察等需要持续关注但并不需要高频输出的场景

## 来源引用

- [摘要：Claude Code 动态循环（Dynamic Looping）来了！](summaries/摘要：Claude Code 动态循环（Dynamic Looping）来了！.md)

## 关联概念

- [Claude Code](entities/Claude Code.md)

- [Claude Code Agent 循环](concepts/Claude Code Agent 循环.md)

- [异步事件驱动编排](concepts/异步事件驱动编排.md)
