---
title: Claude Code Monitor 工具
type: concept
tags:
- Coding Agent
- Agent 技能
status: 审核中
confidence: medium
last_compiled: '2026-04-13'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/864e70c129b040b9a0bb9b46e1d7fb7a
notion_id: 864e70c1-29b0-40b9-a0bb-9b46e1d7fb7a
---

## 定义

Claude Code Monitor 工具是一种面向长时任务的后台监控机制。它可以启动如 `tail`、`watch` 等轻量脚本，持续观察外部状态，并在出现关键事件时再把结果推送回 Claude Code。

## 关键要点

- 通过事件触发代替固定轮询，让 Agent 在无事发生时保持静默

- 可监控 error、CI 失败、PR 新评论等真实外部信号

- 适合日志、构建、部署等需要持续观测但不适合高频轮询的任务

- 与动态循环结合后，可把 Claude Code 的长任务执行方式从定时器式检查升级为事件驱动式唤醒

## 来源引用

- [摘要：Claude Code 动态循环（Dynamic Looping）来了！](summaries/摘要：Claude Code 动态循环（Dynamic Looping）来了！.md)

## 关联概念

- [Claude Code](entities/Claude Code.md)

- [Claude Code Agent 循环](concepts/Claude Code Agent 循环.md)

- [异步事件驱动编排](concepts/异步事件驱动编排.md)
