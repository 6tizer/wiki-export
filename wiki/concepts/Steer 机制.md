---
title: Steer 机制
type: concept
tags:
- Agent 编排
status: 审核中
confidence: high
last_compiled: '2026-04-13'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/8c9bfd22d3894fe4a587a2eb3e0ffc82
notion_id: 8c9bfd22-d389-4fe4-a587-a2eb3e0ffc82
---

## 定义

Steer 机制是指父 Agent 在子 Agent 运行过程中持续发送引导消息、动态修正执行方向的能力。它让多 Agent 协作不再是一次性委派，而是可被实时干预的持续编排。

## 关键要点

- 允许父 Agent 在不中断子任务的前提下追加意图、纠偏或缩细任务范围

- 适合长流程、探索性强或用户中途经常插入新要求的任务环境

- 与纯阻塞式委派相比，Steer 机制把“执行”升级成“可调度的运行中流程”

- 需要配合限流、消息长度控制和状态管理，避免父子 Agent 之间通信失控

## 来源引用

- [摘要：同步阻塞 vs 异步编排：Hermes Delegate 与 OpenClaw 多 Agent 机制深度实战对比](summaries/摘要：同步阻塞 vs 异步编排：Hermes Delegate 与 OpenClaw 多 Agent 机制深度实战对比.md)

## 关联概念

- [OpenClaw](entities/OpenClaw.md)

- [Subagents 并行](concepts/Subagents 并行.md)

- [Hermes Agent](entities/Hermes Agent.md)
