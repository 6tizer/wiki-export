---
title: 摘要：Memory
type: summary
tags:
- 知识管理
- 长期记忆
- Harness 工程
status: 已审核
confidence: medium
last_compiled: '2026-04-20'
source_tags: Agent, LLM, 记忆, skills
source_article_url: https://www.notion.so/348701074b688155b28aee5aec4ee581
notion_url: https://www.notion.so/Tizer/bbf2a9d5f4ea4c6293327e2ebebfd8c4
notion_id: bbf2a9d5-f4ea-4c62-9332-7e2ebebfd8c4
---

## 一句话摘要

这篇文章提出了一种“薄模型、厚 Harness”的 Agent 架构观：把真正决定能力上限的部分外置到记忆、技能、协议与治理层，再由 Harness 在运行时统一编排。

## 关键洞察

- 模型本身不再被视为完整 Agent，而更像是执行推理的核心组件；真正的系统能力来自模型外部的结构化组合。

- **Memory** 负责承载不应塞进权重或上下文窗口的状态，包括工作记忆、语义知识、情景经验与个性化记忆。

- **Skills** 负责沉淀程序性知识，把操作流程、决策启发式与约束条件封装成可复用能力，而不是每次都临时提示。

- **Protocols** 负责定义 Agent 与用户、其他 Agent、工具之间的交互契约，让系统协作从“能对话”升级为“可治理”。

- **Mediator 层** 负责沙箱、观测、压缩、评估、审批回路与子 Agent 编排，决定外部能力如何被安全调用，以及状态如何回流。

- 这套框架真正给出的不是固定答案，而是一套判断问题：当出现一个新能力时，应该把它放进记忆、技能、协议，还是治理层。

## 提取的概念

- [Agent Harness](concepts/Agent Harness.md)

- [记忆分层架构](concepts/记忆分层架构.md)

- [Agent Skills](concepts/Agent Skills.md)

- [Agent 协议层](concepts/Agent 协议层.md)

- [Mediator 层](concepts/Mediator 层.md)

## 原始文章信息

- 作者：@akshay_pachaar

- 来源：X书签

- 发布时间：2026-04-18

- 原文链接：[https://x.com/akshay_pachaar/status/2045510648474530263](https://x.com/akshay_pachaar/status/2045510648474530263)

- 源文章页：薄模型、厚 Harness：重新理解 LLM Agent 的真正架构

## 个人评注

这篇短文对 Tizer 当前的知识编译工作流很有启发：模型不应同时承担长期记忆、流程规则、协作接口和治理职责，而应把这些能力拆成可维护、可审计、可复用的外部层。对 Wiki Compiler 来说，这也说明“语义知识写入协议”本身就是 Harness 设计的一部分——真正有复利的资产，不是一次回答，而是被持续整理进 Wiki 的结构化记忆。
