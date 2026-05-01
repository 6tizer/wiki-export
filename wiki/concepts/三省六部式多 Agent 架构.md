---
title: 三省六部式多 Agent 架构
type: concept
tags:
- 多Agent协作
- Agent 协作模式
- 上下文管理
status: 审核中
confidence: high
last_compiled: '2026-04-15'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/8935535883d9452e9869ef89e65195cb
notion_id: 89355358-83d9-452e-9869-ef89e65195cb
---

## 定义

三省六部式多 Agent 架构，是一种把多个 Agent 模拟成人类组织中的 PM、架构师、开发、测试等岗位，并通过文档交接来串联任务的流水线式设计范式。

## 关键要点

- 它的优势是**直观、易讲述、易演示**，因此很容易在社区传播

- 它的问题在于把人类组织的分工逻辑，误当成了 LLM 系统的最优协作方式

- 角色边界会限制跨界推理，让 Agent 更容易“只做分内事”

- 信息在交接过程中会被压缩成结论，导致局部正确但整体漂移

- 它更像一种展示友好的组织隐喻，而不是适合复杂生产任务的工程架构

## 关联概念

- [Context Engineering](concepts/Context Engineering.md)

- [Orchestrator 模式](concepts/Orchestrator 模式.md)

- [Compaction](concepts/Compaction.md)

- [Agent Skills](concepts/Agent Skills.md)

## 来源引用

- [原文链接](https://x.com/sujingshen/status/2043898494818410731)｜源文章：三省六部幻觉：为什么「虚拟公司」式多 Agent 架构在工程上走不通
