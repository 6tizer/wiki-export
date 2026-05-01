---
title: 摘要：skills
type: summary
tags:
- 上下文管理
- Harness 工程
status: 已审核
confidence: medium
last_compiled: '2026-04-23'
source_tags: ''
source_article_url: https://www.notion.so/34b701074b68813abdb2d9b34c028a0a
notion_url: https://www.notion.so/Tizer/6d21a25fc52740f895ed3b4c20330c5d
notion_id: 6d21a25f-c527-40f8-95ed-3b4c20330c5d
---

**一句话摘要**

这条围绕 skills 的讨论认为，相比把能力拆成大量彼此依赖的小技能，给 Agent 配置更少但更胖、可参数化的 skills，往往更能缩短 resolver、减少 context bloat，并提升整体执行稳定性。

## 关键洞察

- 相邻 skills 应优先被 DRY 合并成一个更大的能力块，再通过参数或模式切换处理分支。

- resolver 越短，Agent 在选择技能和工具时承受的上下文噪声通常越小。

- 当技能链条过深时，错误路由、工具误选和延迟都会明显上升。

- 很多关于 skill graph 的争论，本质上是在讨论 workflow、harness 与上下文管理的边界应该如何划分。

- 社区并没有完全共识，但多数经验都指向：技能颗粒度设计必须和上下文成本一起权衡。

## 提取的概念

- [Thin Harness, Fat Skills](concepts/Thin Harness, Fat Skills.md)

- [Resolver](concepts/Resolver.md)

- [Context Bloat](concepts/Context Bloat.md)

- [Skill Graph](concepts/Skill Graph.md)

## 原始文章信息

- 作者：@garrytan

- 来源：X书签

- 发布时间：2026-04-23

- 链接：[原文](https://x.com/garrytan/status/2047183884266402275)

## 个人评注

对 Tizer 来说，这条讨论的启发在于：内容与 Agent 流水线不该机械追求“更多原子技能”，而应把稳定重复的相邻动作收敛为参数化能力，再让 harness、workflow 与 HITL 去承担调度、校验和边界控制。
