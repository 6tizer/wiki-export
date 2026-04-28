---
title: 子 Agent 派生
type: concept
tags:
- Agent 协作模式
- 多Agent协作
- OpenClaw
status: 审核中
confidence: high
last_compiled: '2026-04-28'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/9b461ffd38fa4b1081a2810ae21f8b71
notion_id: 9b461ffd-38fa-4b10-81a2-810ae21f8b71
---

## 定义

子 Agent 派生（Sub-Agent Spawning）是 OpenClaw 2026.2.17 版本引入的能力：用户可**直接在对话界面中动态创建子 Agent**，无需编写配置文件，让子 Agent 并行处理不同子任务。

## 工作原理

- 主 Agent 在任务执行中途将工作交接给一个或多个子 Agent

- 配合 1M 上下文窗口，子 Agent 之间的"交接文档"可以无限长，不丢失上下文细节

- 支持并行调度：一条指令可拆分为多个并行子任务同时处理

## 意义

- 使复杂、长流程任务从理论变为现实

- 无需代码写死流程或复杂 DAG 工具链

- 实现个人 AI Agent 的"团队协作"模式

## 来源引用

- [摘要：OpenClaw 2026.2.17：1M 上下文 + 子 Agent 催生的个人 AI 新范式](summaries/摘要：OpenClaw 2026.2.17：1M 上下文 + 子 Agent 催生的个人 AI 新范式.md)

- [摘要：OpenClaw 多角色 Telegram 群聊：一个 Gateway 跑产品经理、工程师、QA 的实战指南](summaries/摘要：OpenClaw 多角色 Telegram 群聊：一个 Gateway 跑产品经理、工程师、QA 的实战指南.md)

- [摘要：GBrain Minions：用 Postgres 任务队列，把多 Agent 系统从玩具拉到生产级](summaries/摘要：GBrain Minions：用 Postgres 任务队列，把多 Agent 系统从玩具拉到生产级.md)（[原文](https://x.com/AYi_AInotes/status/2045825582600958461)）

## 关联概念

- [Telegram 群组路由](concepts/Telegram 群组路由.md)

- [OpenClaw](entities/OpenClaw.md)

- [Minions](concepts/Minions.md)

- [Postgres 任务队列](concepts/Postgres 任务队列.md)
