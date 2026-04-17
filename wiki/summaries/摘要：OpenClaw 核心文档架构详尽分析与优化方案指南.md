---
title: 摘要：OpenClaw 核心文档架构详尽分析与优化方案指南
type: summary
tags:
- OpenClaw
- Agent 编排
status: 已审核
confidence: high
last_compiled: '2026-04-16'
source_tags: ''
source_article_url: https://www.notion.so/344701074b68800fa2e2cd6aedf0218c
notion_url: https://www.notion.so/013959376ee64aef9a418064d58e39b7
notion_id: 01395937-6ee6-4aef-9a41-8064d58e39b7
---

## 一句话摘要

这篇文章系统拆解了 OpenClaw 以 Markdown 工作区文件驱动 Agent 的核心架构，梳理官方 7 个主文件与 3 种社区优化版本，并把稳定性、自进化与 token 成本之间的取舍讲清楚。

## 关键洞察

- OpenClaw 的核心不是单一 prompt，而是把人格、规则、用户上下文与长期记忆拆进一组可读、可审计、可版本化的 Markdown 文件。

- 官方推荐的基础分层是 [SOUL.md](http://soul.md/)、[IDENTITY.md](http://identity.md/)、[AGENTS.md](http://agents.md/)、[USER.md](http://user.md/)、[TOOLS.md](http://tools.md/)、[MEMORY.md](http://memory.md/)、[HEARTBEAT.md](http://heartbeat.md/)，再配合 memory/ 日志文件夹形成长期运行结构。

- 社区最常见的轻量升级路径，是把表达风格从 [SOUL.md](http://soul.md/) 拆到 [STYLE.md](http://style.md/)，以降低身份漂移并提升输出一致性。

- 面向长期运行的进化方案，会把反思结果沉淀到 [EVOLUTION.md](http://evolution.md/)，并通过人工确认维持受控自进化。

- 当 Agent 进入高频或多 Agent 场景时，核心优化方向会转向按需加载、语义检索和记忆压缩，以降低 token 开销并提升可扩展性。

## 提取的概念

- [OpenClaw](entities/OpenClaw.md)

- [SOUL.md](concepts/SOUL.md.md)

- [IDENTITY.md](concepts/IDENTITY.md.md)

- [AGENTS.md](concepts/AGENTS.md.md)

- [TOOLS.md](concepts/TOOLS.md.md)

- [MEMORY.md](concepts/MEMORY.md.md)

- [HEARTBEAT.md](concepts/HEARTBEAT.md.md)

- [STYLE.md](concepts/STYLE.md.md)

- [EVOLUTION.md](concepts/EVOLUTION.md.md)

- [文件即大脑](concepts/文件即大脑.md)

- [受控自进化](concepts/受控自进化.md)

## 原始文章信息

- 作者：未知

- 来源：X书签

- 发布时间：未知

- 原文链接：未提供

- 源文章：OpenClaw：用 Markdown 文件定义 AI Agent 大脑的「文件即代理」框架深度解析

## 个人评注

这篇材料和 Tizer 当前的工作流高度相关，尤其适合沉淀到 OpenClaw、内容工厂、HITL 协作与长期记忆治理这几条主线里。它的价值不只是介绍文件名，而是提供了一套把 Agent 从“临时 prompt”升级为“可维护工作系统”的分层方法，这对后续做稳定编排、记忆压缩和多 Agent 协作都很有参考价值。
