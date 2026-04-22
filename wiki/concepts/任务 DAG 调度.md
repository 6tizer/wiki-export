---
title: 任务 DAG 调度
type: concept
tags:
- Agent 编排
status: 审核中
confidence: high
last_compiled: '2026-04-12'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/bf5cabcf77114f07bd30242feea30853
notion_id: bf5cabcf-7711-4f07-bd30-242feea30853
---

## 定义

任务 DAG 调度是把复杂目标拆成带依赖关系的任务图，再按前置条件解锁并行执行的一种多智能体编排方式。

## 关键要点

- 适合处理可分解、可并发的复杂任务链

- 相比线性对话式协作，更容易做失败隔离与依赖追踪

- 是多智能体系统从聊天协商走向工程调度的重要结构化能力

## 来源引用

- Open-Multi-Agent：从 Claude Code 源码泄露中诞生的 TypeScript 多智能体框架（[原文](https://x.com/berryxia/status/2040556372887302229)）

- [摘要：GBrain Minions：用 Postgres 任务队列，把多 Agent 系统从玩具拉到生产级](summaries/摘要：GBrain Minions：用 Postgres 任务队列，把多 Agent 系统从玩具拉到生产级.md)（[原文](https://x.com/AYi_AInotes/status/2045825582600958461)）

## 关联概念

- [Minions](concepts/Minions.md)

- [Postgres 任务队列](concepts/Postgres 任务队列.md)

- [子 Agent 派生](concepts/子 Agent 派生.md)
