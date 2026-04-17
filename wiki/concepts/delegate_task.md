---
title: delegate_task
type: concept
tags:
- Agent 编排
status: 草稿
confidence: high
last_compiled: '2026-04-13'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/25bc606477f74b46b112e25781c0581c
notion_id: 25bc6064-77f7-4b46-b112-e25781c0581c
---

## 定义

delegate_task 是 Hermes 体系里的同步委派机制。父 Agent 把任务拆给子 Agent 后会阻塞等待结果返回，子 Agent 只回传精炼 summary，而不会把完整推理过程注入父上下文。

## 关键要点

- 采用“总包—分包”式同步调用，父 Agent 在等待期间无法继续推进其他子任务协调

- 子 Agent 具备独立历史、独立工作目录与受限工具集，强调隔离和 token 效率

- 适合多个互不相关、可并行拆分且不需要中途干预的执行型子任务

- 当前实现的短板是缺少显式超时控制，容易在慢速模型或长任务上阻塞过久

## 来源引用

- [摘要：同步阻塞 vs 异步编排：Hermes Delegate 与 OpenClaw 多 Agent 机制深度实战对比](summaries/摘要：同步阻塞 vs 异步编排：Hermes Delegate 与 OpenClaw 多 Agent 机制深度实战对比.md)

## 关联概念

- [Hermes Agent](entities/Hermes Agent.md)

- [OpenClaw](entities/OpenClaw.md)

- [Subagents 并行](concepts/Subagents 并行.md)
