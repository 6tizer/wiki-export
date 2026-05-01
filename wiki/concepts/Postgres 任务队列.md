---
title: Postgres 任务队列
type: concept
tags:
- Harness 工程
- 链上协议
- Agent 安全
status: 审核中
confidence: high
last_compiled: '2026-04-20'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/f492523da9a049bb95b4ad2e621280d6
notion_id: f492523d-a9a0-49bb-95b4-ad2e621280d6
---

## 定义

Postgres 任务队列是一种把任务状态、重试信息、执行进度与调度元数据直接持久化到 Postgres 的后台执行模式，适合需要可靠恢复和可观测性的自动化流程。

## 关键要点

- 把任务从易失的会话进程中解耦，降低断线、重启和超时带来的状态丢失风险

- 相比额外部署独立队列基础设施，更适合已有 Postgres 的轻量 Agent 系统

- 能与重试、暂停、恢复、依赖关系和进度日志结合，形成可运维的执行层

- 特别适合 API 拉取、数据同步、批处理导入等确定性后台任务

## 来源引用

- [摘要：GBrain Minions：用 Postgres 任务队列，把多 Agent 系统从玩具拉到生产级](summaries/摘要：GBrain Minions：用 Postgres 任务队列，把多 Agent 系统从玩具拉到生产级.md)（[原文](https://x.com/AYi_AInotes/status/2045825582600958461)）

## 关联概念

- [GBrain](entities/GBrain.md)

- [任务 DAG 调度](concepts/任务 DAG 调度.md)

- [子 Agent 派生](concepts/子 Agent 派生.md)
