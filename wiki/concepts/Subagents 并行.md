---
title: Subagents 并行
type: concept
tags:
- Agent 协作模式
- 多Agent协作
- OpenClaw
status: 审核中
confidence: medium
last_compiled: '2026-05-01'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/48ff78c527b046edb6e5cee2ce5f5382
notion_id: 48ff78c5-27b0-46ed-b6e5-cee2ce5f5382
---

## 定义

Subagents 并行是 Claude Cowork 中的一种多任务执行模式，允许主 Agent 将独立子任务分配给多个子代理（Subagents）同时执行，从而将串行处理时间压缩为并行处理时间。

## 关键要点

- 典型场景：评估 4 个供应商 → 4 个子代理同时跑，40 分钟→10 分钟

- 被认为是 Cowork 最被低估的隐藏功能

- 适合任务之间相互独立、无依赖关系的批量处理场景

- 与 OpenClaw 的多 Agent 编排模式相似

- 与 BMAD Method 的 Party Mode（多 Agent 同时工作互相 review）理念相通

## 来源引用

- [摘要：What is an Agent Harness](summaries/摘要：What is an Agent Harness.md)（[原文](https://x.com/aparnadhinak/status/2046980769747533830)）

- [摘要：这样用 Opus 4.7，才能发挥实力](summaries/摘要：这样用 Opus 4.7，才能发挥实力.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzkzNDQxOTU2MQ%3D%3D&mid=2247515662&idx=1&sn=bfcc64cdceb913aef59f697c1ecbfa8d&chksm=c3914681eabbc4c3c559e95297d8d5b85aebabf0c4c93a5d517e6784d086e7b7ff3aa9abee9e#rd)）

- [摘要：同步阻塞 vs 异步编排：Hermes Delegate 与 OpenClaw 多 Agent 机制深度实战对比](summaries/摘要：同步阻塞 vs 异步编排：Hermes Delegate 与 OpenClaw 多 Agent 机制深度实战对比.md)（[原文](https://x.com/servasyy_ai/status/2042951017462169812)，servasyy_ai，2026-04）

- [摘要：让Claude cowork强100倍的17个习惯](summaries/摘要：让Claude cowork强100倍的17个习惯.md)（向量空性，2026-03-03）

- [摘要：Claude Subagents vs Agent Teams：别过早引入多智能体，复杂度需要被赚到](summaries/摘要：Claude Subagents vs Agent Teams：别过早引入多智能体，复杂度需要被赚到.md)（[原文](https://x.com/akshay_pachaar/status/2033456347354996815)，akshay_pachaar，2026-01）

- [摘要：MiniMax M2.7 × Hermes Agent：开启自我进化的 Agent 工作流](summaries/摘要：MiniMax M2.7 × Hermes Agent：开启自我进化的 Agent 工作流.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzE5MTA3NzcxMQ%3D%3D&mid=2247488335&idx=1&sn=ece0fb7411d313acd1c583c84b748538)，微信，2026-03）

- [摘要：Using Claude Code: Session Management & 1M Context](summaries/摘要：Using Claude Code- Session Management & 1M Context.md)（[原文](https://x.com/trq212/status/2044548257058328723)，trq212，2026-04）

- [摘要：说实话，这才是Anthropic今年最有价值的更新啊，没有之一！！！](summaries/摘要：说实话，这才是Anthropic今年最有价值的更新啊，没有之一！！！.md)（[原文](https://x.com/AYi_AInotes/status/2044625894556230013)，AYi_AInotes，2026-04）

- [摘要：Single-agent AI coding is a nightmare for engineers](summaries/摘要：Single-agent AI coding is a nightmare for engineers.md)（[原文](https://x.com/MilksandMatcha/status/2044863551186309460)）

- [摘要：Ollama 一键启动 Hermes Agent：免费、本地、会自我进化的 AI 私人助手](summaries/摘要：Ollama 一键启动 Hermes Agent：免费、本地、会自我进化的 AI 私人助手.md)（[原文](https://x.com/Saboo_Shubham_/status/2045692123887050816)）

- [摘要：ziggy-llm](summaries/摘要：ziggy-llm.md)（[原文](https://x.com/zxytim/status/2046255419178500408)）

- [摘要：Cursor 3 /multitask 异步子代理并行执行](summaries/摘要：Cursor 3 -multitask 异步子代理并行执行.md)（[原文](https://x.com/cursor_ai/status/2047764651363180839)）

- [摘要：Claude Code's Limits Are Generous. The Problem Is Your Harness.](summaries/摘要：Claude Code's Limits Are Generous. The Problem Is Your Harness.md)（[原文](https://x.com/PawelHuryn/status/2048170309396926577)）

- [摘要：The harness as the context manager](summaries/摘要：The harness as the context manager.md)（[原文](https://x.com/tonygentilcore/status/2049482833111232694)）

## 关联概念

- [OpenClaw](entities/OpenClaw.md)

- [Hermes Agent](entities/Hermes Agent.md)

- [delegate_task](concepts/delegate_task.md)

- [Steer 机制](concepts/Steer 机制.md)

- [异步事件驱动编排](concepts/异步事件驱动编排.md)

- [Claude Code](entities/Claude Code.md)

- [Claude Code 上下文管理](concepts/Claude Code 上下文管理.md)

- [Context Rot](concepts/Context Rot.md)

- [Context Compaction](concepts/Context Compaction.md)

- [Rewind](concepts/Rewind.md)

- [上下文隔离](concepts/上下文隔离.md)

- [阶段式并行执行](concepts/阶段式并行执行.md)

- [Codex Spark](entities/Codex Spark.md)
