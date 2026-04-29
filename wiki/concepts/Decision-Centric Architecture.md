---
title: Decision-Centric Architecture
type: concept
tags:
- Harness 工程
- AI 产品
status: 草稿
confidence: high
last_compiled: '2026-04-29'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/cf8ea5cb97064e8bba3d90c0f08efed8
notion_id: cf8ea5cb-9706-4e8b-ba3d-90c0f08efed8
---

## 定义

Decision-Centric Architecture（以决策为中心的架构）是一种企业软件设计范式，主张现代企业架构的核心应围绕「决策」而非「数据」来组织。它将每个操作决策分解为四个组成要素——数据（Data）、逻辑（Logic）、行动（Action）和安全（Security）——并将它们整合到一个统一的、可被人类和 AI Agent 共同使用的协作基础中。

## 关键要点

- 传统数据架构的局限：只建模数据流转和存储，无法捕获决策推理过程和执行结果，限制了 AI 的学习和嵌入

- 传统分析架构的局限：计算结果脱离操作现实（disconnected from operations），无法直接驱动行动

- 四要素模型：Data（决策所需信息）、Logic（评估决策的启发式和计算过程）、Action（决策的编排和执行）、Security（合规保障）

- 关键转变：从「分析系统」到「操作系统」——不仅产生洞察，还直接闭合行动回路

- 代表实现：Palantir Ontology 是目前最成熟的 Decision-Centric Architecture 实践

- 与 Agent 时代的关系：当 AI Agent 需要在企业环境中自主推理和行动时，Decision-Centric Architecture 提供了治理框架和工具接口

## 关联概念

- [Palantir Ontology](entities/Palantir Ontology.md)

- [Decision Lineage](concepts/Decision Lineage.md)

- [Ontology Scenario](concepts/Ontology Scenario.md)

## 来源引用

- [摘要：Connecting Agents to Decisions](summaries/摘要：Connecting Agents to Decisions.md)（[原文](https://x.com/PalantirTech/status/2049136883528011954)）
