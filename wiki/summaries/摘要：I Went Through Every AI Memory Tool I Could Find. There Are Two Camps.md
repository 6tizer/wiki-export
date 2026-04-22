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
source_article_url: https://www.notion.so/345701074b6881c3b50bc941bb5a2d4e
notion_url: https://www.notion.so/3745620d18dc4b65a623159dbd40fd62
notion_id: 3745620d-18dc-4b65-a623-159dbd40fd62
---

## 一句话摘要

这篇文章把 AI 记忆工具清晰划分为两大范式：以事实提取与检索为核心的“记忆后端”，以及以结构化、可持续累积的工作上下文为核心的“上下文基底”，并判断后者会成为长期运行 Agent 的主流基础设施。

## 关键洞察

- “记忆后端”解决的是**召回**问题，即系统如何从历史对话中提取、存储并找回事实，代表性产品包括 Mem0、MemPalace 和 Honcho。

- “上下文基底”解决的是**复利**问题，即 Agent 如何在结构化上下文中持续工作、写回、整理，并让系统随时间不断变得更强。

- Camp 1 的主流实现多依赖向量库、图数据库或混合检索，适合偏好记忆、事实回忆和会话延续，但通常不擅长表达跨项目的长期状态演化。

- Camp 2 更强调 Markdown 文件、知识图谱、上下文容器等人类可读的载体，让人和 Agent 都能直接检查、修正、继承上下文。

- 作者认为 Zep 从“memory”转向“context engineering”的表述变化，是行业语言正在转向上下文基底的重要信号。

- OpenClaw 的 Dreaming、TrustGraph 的 Context Cores、MemSearch 的 file-native 设计，都体现出“上下文本身就是记忆”的共同趋势。

- ALIVE 被作者作为正在实践的方向提出，强调 file-native、agent-agnostic、零基础设施依赖，试图把长期上下文做成可迁移、可复用的底层基底。

## 提取的概念

- [记忆后端](concepts/记忆后端.md)

- [上下文基底](concepts/上下文基底.md)

- [Context Engineering](concepts/Context Engineering.md)

- [Dreaming 记忆机制](concepts/Dreaming 记忆机制.md)

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

这篇文章对 Tizer 当前的知识编译与内容流水线很有参考价值。若目标只是让 Agent 记住用户偏好、历史事实或短期线索，记忆后端已经足够；但如果目标是让 OpenClaw 一类长期运行的 Agent 在多项目、多轮协作、HITL 审核和内容工厂场景中持续积累上下文，那么更值得优先建设的是可读、可审计、可人工修正的上下文基底。
