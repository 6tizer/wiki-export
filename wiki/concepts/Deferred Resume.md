---
title: Deferred Resume
type: concept
tags:
- Harness 工程
status: 草稿
confidence: medium
last_compiled: '2026-04-27'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/93c6b7779f1c4e6ea857d32d3062d319
notion_id: 93c6b777-9f1c-4e6e-a857-d32d3062d319
---

## 定义

Deferred Resume（延迟恢复）是一种 Agent 自调度模式：Agent 可以主动请求 harness 在 N 分钟后重新触发当前对话循环，而不是滥用 bash sleep 等阻塞命令。本质上是「定时任务在特定时间唤醒」的语法糖，让 Agent 能自主管理其生命周期。

## 关键要点

- 解决了 Agent 长时间等待时滥用 `sleep` 命令的问题

- Agent 触发 deferred resume 后可以释放资源，N 分钟后由调度引擎重新唤醒

- 属于 Agent Lifecycle Management 的一部分，与定时任务、队列跟进并列

- 调度引擎同时暴露给 Agent 和用户，Agent 可以自己创建：

  1. 定期执行的任务（recurring）

  1. 指定时间执行（future）

  1. 排队跟进（followup）

  1. 延迟恢复（deferred resume）

- 该模式使 Agent 从被动执行者变为能管理自身运行节奏的主动参与者

## 来源引用

- [摘要：Personal Agent](summaries/摘要：Personal Agent.md)（[原文](https://x.com/trashpandaemoji/status/2048026069375029267)）
