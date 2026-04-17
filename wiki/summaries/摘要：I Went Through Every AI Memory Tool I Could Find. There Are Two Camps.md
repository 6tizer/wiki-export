---
title: 摘要：I Went Through Every AI Memory Tool I Could Find. There Are Two Camps.
type: summary
tags:
- 记忆系统
- Agent 编排
status: 已审核
confidence: high
last_compiled: '2026-04-17'
source_tags: ''
source_article_url: https://www.notion.so/345701074b6881099729e0d75ab49d4b
notion_url: https://www.notion.so/59e3c338638f44dcbbc7f17b64f918a1
notion_id: 59e3c338-638f-44dc-bbc7-f17b64f918a1
---

## 一句话摘要

这篇长文把 AI 记忆工具清晰划分为“记忆后端”和“上下文基底”两大阵营，并指出真正适合 24/7 持续运行 Agent 的，不是做事实召回的 memory backend，而是能让上下文跨会话持续复利的 context substrate。

## 关键洞察

- “记忆后端”范式的核心循环是提取、存储、检索，优化目标是**召回**，代表问题是“AI 该记住什么”。

- “上下文基底”范式的核心循环是读取上下文、在上下文中工作、再把新状态写回，优化目标是**复利**，代表问题是“AI 应该在什么上下文里工作”。

- Camp 1 工具在基准、接入成本和事实检索上已经非常成熟，但难以直接承载跨项目、跨阶段的长期状态演化。

- Camp 2 更强调文件、知识图或上下文容器作为第一性载体，人和 Agent 都能直接阅读、编辑、纠偏，因此更适合多会话、长期运行的 Agent 系统。

- 作者进一步判断，行业语言会从“memory”转向“context engineering”，因为严肃的 Agent 基础设施正在从“记住事实”转向“经营上下文”。

## 提取的概念

- [记忆后端](concepts/记忆后端.md)

- [上下文基底](concepts/上下文基底.md)

- [Context Engineering](concepts/Context Engineering.md)

- [Mem0](entities/Mem0.md)

- [MemPalace](entities/MemPalace.md)

- [OpenClaw](entities/OpenClaw.md)

- [ALIVE](entities/ALIVE.md)

## 原始文章信息

- 作者：@witcheer

- 来源：X书签

- 发布时间：2026-04-15

- 原文链接：[https://x.com/witcheer/status/2044456778843238689](https://x.com/witcheer/status/2044456778843238689)

## 个人评注

这篇文章对 Tizer 当前的 Agent 内容管线很有启发：如果目标是做一次性的摘要分发，记忆后端已经足够；但如果要把 OpenClaw、HITL 审核、内容工厂和知识沉淀接成持续演化的系统，就必须把“上下文如何累积、如何回写、如何被下一轮工作直接复用”当成核心设计对象。
