---
title: 摘要：Hermes Agent 深度技术解析：架构、演进与 OpenClaw 的差异化对比
type: summary
tags:
- Agent 框架
- OpenClaw
status: 已审核
confidence: high
last_compiled: '2026-04-15'
source_tags: ''
source_article_url: https://www.notion.so/343701074b68811eb712f29062aa8c8b
notion_url: https://www.notion.so/11500aee3c28461fbe0d25f6391b0d2d
notion_id: 11500aee-3c28-461f-be0d-25f6391b0d2d
---

## 一句话摘要

这篇文章将 Hermes Agent 与 OpenClaw 放在同一坐标系中对比，指出前者更偏向模型中心的自进化闭环，后者更偏向系统中心的多平台执行与安全控制。

## 关键洞察

- Hermes Agent 的核心竞争力在于推理引擎、分层记忆和 GEPA 自进化闭环，强调 Agent 会随着使用持续优化。

- OpenClaw 的优势在于 Gateway、多端接入、文件化记忆和显式审批机制，强调可控、可审计与本地优先。

- 两者的技能扩展路线不同，Hermes 更依赖 MCP 协议与动态技能加载，OpenClaw 更依赖 [SKILL.md](http://skill.md/) + 脚本的声明式封装。

- 在记忆设计上，Hermes 倾向 Honcho / 向量检索式长期记忆，OpenClaw 倾向 [MEMORY.md](http://memory.md/) 一类文件化记忆，分别代表检索效率与可解释性的两条路线。

- 从选型角度看，Hermes 更适合研究型、自进化和复杂工具链任务，OpenClaw 更适合多端个人助理、内容工作流和高权限但需强治理的日常场景。

## 提取的概念

- [Hermes Agent](entities/Hermes Agent.md)

- [OpenClaw](entities/OpenClaw.md)

- [MCP 协议](concepts/MCP 协议.md)

- [Honcho](entities/Honcho.md)

- [GEPA](concepts/GEPA.md)

- [ClawShell](entities/ClawShell.md)

## 原始文章信息

- 作者：AIer 笔记

- 来源：微信

- 发布时间：2026-04-15 10:11

- 原文链接：[查看原文](https://mp.weixin.qq.com/s?__biz=MzE5ODM0MDIyNg%3D%3D&mid=2247484011&idx=1&sn=588c8c9f5f8a8e56cb1d32c5ba91947a&chksm=976d338b09e0fcd9565bdfc1728262bd18a93f1408aecb26a19ba94a31968423d172955f1a51#rd)

## 个人评注

这篇对比很适合放进 Tizer 的 Agent 方法论知识层：Hermes 提供了“模型如何自我优化”的研究视角，OpenClaw 提供了“如何把 Agent 变成长期可控执行系统”的工程视角。对 HITL、OpenClaw 内容管线和后续的多 Agent 编排设计来说，这篇文章相当于一张高密度的选型地图。
