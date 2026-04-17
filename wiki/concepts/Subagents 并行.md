---
title: Subagents 并行
type: concept
tags:
- Agent 编排
status: 审核中
confidence: medium
last_compiled: '2026-04-14'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/48ff78c527b046edb6e5cee2ce5f5382
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

- [原文链接](https://x.com/servasyy_ai/status/2042951017462169812)｜《同步阻塞 vs 异步编排：Hermes Delegate 与 OpenClaw 多 Agent 机制深度实战对比》｜来源条目：[摘要：同步阻塞 vs 异步编排：Hermes Delegate 与 OpenClaw 多 Agent 机制深度实战对比](summaries/摘要：同步阻塞 vs 异步编排：Hermes Delegate 与 OpenClaw 多 Agent 机制深度实战对比.md)

- 《让Claude cowork强100倍的17个习惯》（向量空性，2026-03-03）— 将 Subagents 并行列为第十个核心习惯

- [原文链接](https://x.com/akshay_pachaar/status/2033456347354996815)｜《Claude Subagents vs Agent Teams：别过早引入多智能体，复杂度需要被赚到》｜来源条目：[摘要：Claude Subagents vs Agent Teams：别过早引入多智能体，复杂度需要被赚到](summaries/摘要：Claude Subagents vs Agent Teams：别过早引入多智能体，复杂度需要被赚到.md)

- [原文链接](https://mp.weixin.qq.com/s?__biz=MzE5MTA3NzcxMQ%3D%3D&mid=2247488335&idx=1&sn=ece0fb7411d313acd1c583c84b748538&chksm=971ff5041a501710ae6c94e032c8f8d009fe38dd0edd9fbf16d3d392baedc9c670020c3bf213#rd)｜《MiniMax M2.7 × Hermes Agent：开启自我进化的 Agent 工作流》｜来源条目：[摘要：MiniMax M2.7 × Hermes Agent：开启自我进化的 Agent 工作流](summaries/摘要：MiniMax M2.7 × Hermes Agent：开启自我进化的 Agent 工作流.md)

- [原文链接](https://x.com/trq212/status/2044548257058328723)｜《Using Claude Code: Session Management & 1M Context》｜来源条目：[摘要：Using Claude Code: Session Management & 1M Context](summaries/摘要：Using Claude Code- Session Management & 1M Context.md)

- [原文链接](https://x.com/AYi_AInotes/status/2044625894556230013)｜《说实话，这才是Anthropic今年最有价值的更新啊，没有之一！！！》｜来源条目：[摘要：说实话，这才是Anthropic今年最有价值的更新啊，没有之一！！！](summaries/摘要：说实话，这才是Anthropic今年最有价值的更新啊，没有之一！！！.md)

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
