---
title: '摘要：Sub-Agents vs Agent Teams: The Architecture Decision That Changes Everything'
type: summary
tags:
- Agent 协作模式
- 多Agent协作
status: 已审核
confidence: high
last_compiled: '2026-04-30'
source_tags: ''
source_article_url: https://www.notion.so/352701074b6881058d04e084677be954
notion_url: https://www.notion.so/Tizer/4871b93423bd46edbf5dfd7b61cb95d5
notion_id: 4871b934-23bd-46ed-bf5d-fd7b61cb95d5
---

## 一句话摘要

多 Agent 系统架构的核心决策不是「要不要用多个 Agent」，而是「按上下文边界还是按角色来拆分」——Sub-Agent 适合可隔离的独立任务，Agent Teams 适合强依赖的协作任务。

## 关键洞察

- **Sub-Agent = 隔离式委派**：每个 sub-agent 拥有独立系统提示、受限工具集和隔离上下文，只返回最终输出而非中间推理过程；sub-agent 之间不能通信，也不能生成新 agent，一切通过父节点流转

- **Agent Teams = 协作式通信**：包含 lead agent（分配+综合）和 teammates（执行），共享任务层跟踪进度和依赖，支持实时上下文共享和 peer-to-peer 通信

- **角色拆分是常见错误**：按 planner/developer/tester 拆分导致每次 handoff 丢失上下文，质量逐级衰减；正确方法是按「信息依赖关系」拆分（上下文边界分解）

- **五种关键编排模式**：Prompt Chaining（顺序链式）、Routing（路由分发）、Parallelization（并行执行）、Orchestrator-Worker（委派调度）、Evaluator-Optimizer（生成+精炼）

- **不要过度设计**：如果 agent 之间强依赖、协调开销过高、或任务本身简单，单 Agent 就够了；先简单再按需加复杂度

## 提取的概念

- [上下文边界分解](concepts/上下文边界分解.md)（本文核心原则：Design around context boundaries, not roles）

- [Sub agent 上下文隔离](concepts/Sub agent 上下文隔离.md)（Sub-Agent 的隔离式执行模式）

- [Agent Team](concepts/Agent Team.md)（协作式多 Agent 团队编排）

- [Orchestrator 模式](concepts/Orchestrator 模式.md)（Orchestrator-Worker 委派调度模式）

- [Claude Agent SDK](entities/Claude Agent SDK.md)（文中代码示例使用的 Anthropic Agent 开发工具包）

## 原始文章信息

- **作者**：@NainsiDwiv50980

- **来源**：X书签

- **发布日期**：2026-04-29

- **原文链接**：[原文](https://x.com/NainsiDwiv50980/status/2049529787300090344)

## 个人评注

本文对 Tizer 的 Harness Engineering 工作流有直接指导意义：OpenClaw 在设计多 Agent 编排时，应优先按上下文边界而非角色标签拆分。Sub-Agent 模式天然适合 content pipeline 中的独立子任务（如检索、摘要），而 Agent Teams 更适合需要持续共享状态的协作场景（如 HITL 审核流水线）。「先简单后复杂」的原则也与 OpenClaw 的渐进式架构策略一致。
