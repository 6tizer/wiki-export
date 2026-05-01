---
title: Minions
type: concept
tags:
- OpenClaw
status: 审核中
confidence: high
last_compiled: '2026-04-20'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/5d7a3932d5f4403e84f35134dc613e99
notion_id: 5d7a3932-d5f4-403e-84f3-5134dc613e99
---

## 定义

Minions 是 GBrain v0.11 内置的任务执行机制，本质上是面向确定性后台任务的 Postgres 原生队列层，用来替代容易超时和失联的子 Agent spawn。

## 关键要点

- 任务元数据与进度状态持久化到 Postgres / PGLite，支持崩溃后恢复与断点续跑

- 支持暂停、恢复、取消、inbox 干预与结构化进度追踪，降低长流程自动化的不确定性

- 可承载父子 DAG 依赖关系，让多步任务从黑盒会话变成可调度的工程流程

- 最适合 API 抓取、解析、同步、批量导入等不需要模型判断的确定性工作

## 来源引用

- [摘要：GBrain Minions：用 Postgres 任务队列，把多 Agent 系统从玩具拉到生产级](summaries/摘要：GBrain Minions：用 Postgres 任务队列，把多 Agent 系统从玩具拉到生产级.md)（[原文](https://x.com/AYi_AInotes/status/2045825582600958461)）

## 关联概念

- [GBrain](entities/GBrain.md)

- [Hermes Agent](entities/Hermes Agent.md)

- [Postgres 任务队列](concepts/Postgres 任务队列.md)

- [任务 DAG 调度](concepts/任务 DAG 调度.md)

- [子 Agent 派生](concepts/子 Agent 派生.md)
