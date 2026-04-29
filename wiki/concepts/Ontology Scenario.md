---
title: Ontology Scenario
type: concept
tags:
- Harness 工程
- Agent 安全
status: 草稿
confidence: medium
last_compiled: '2026-04-29'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/e8150d728b344aa88f6b685fd8523493
notion_id: e8150d72-8b34-4aa8-8f6b-685fd8523493
---

## 定义

Ontology Scenario（本体场景/沙盒场景）是 Palantir Ontology 中的一种安全决策探索机制。它将提议的变更打包为 Ontology 的一个沙盒子集（sandboxed subset），使团队和 AI Agent 能够在不影响生产数据的前提下，安全地探索、分析和比较不同决策方案的后果。

## 关键要点

- 核心作用：在 commit 决策之前提供安全的「what-if」探索空间

- Agent 可以像人类一样使用 Scenario 框架：将推荐方案 stage 为场景，交给人类做最终审核

- 场景受到与数据和逻辑相同的细粒度访问控制约束

- 支持批量暂存和审核变更

- 是 Human-in-the-Loop（HITL）模式在企业决策场景中的具体实现

- 与模拟/仿真的关系：Scenario 不是独立的仿真引擎，而是在真实 Ontology 数据之上创建的受控分支

## 关联概念

- [Palantir Ontology](entities/Palantir Ontology.md)

- [Decision-Centric Architecture](concepts/Decision-Centric Architecture.md)

- [Decision Lineage](concepts/Decision Lineage.md)

## 来源引用

- [摘要：Connecting Agents to Decisions](summaries/摘要：Connecting Agents to Decisions.md)（[原文](https://x.com/PalantirTech/status/2049136883528011954)）
