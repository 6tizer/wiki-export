---
title: 摘要：5 Agent Design patterns for Long-running AI Agents
type: summary
tags: []
status: 已审核
confidence: high
last_compiled: '2026-04-23'
source_tags: ''
source_article_url: https://www.notion.so/34b701074b6881fd8549e1e7a1f8218f
notion_url: https://www.notion.so/Tizer/f8b5a2644e6b4285840ce73918d81905
notion_id: f8b5a264-4e6b-4285-840c-e73918d81905
---

## 一句话摘要

Google 将长时运行智能体的核心问题拆成 5 个可复用设计模式：断点续跑、委托审批、分层记忆、环境式处理与舰队编排，并用 Agent Runtime 等基础设施把多天级任务从 demo 推向生产。

## 关键洞察

- 多天级 agent 的核心不是 prompt，而是持久状态、容错与恢复能力。

- 人在环审批的关键不是发 webhook，而是“原地暂停 / 原地恢复”，从而保留完整上下文。

- 长期记忆必须被治理，否则会出现 memory drift、越权访问和跨流程污染。

- 背景型 agent 需要把策略从 agent 代码里外置到治理层，避免每次改规则都重部署。

- 多 agent 系统更接近分布式系统，协调者 / 专家分工、独立发布与隔离运行是生产关键。

## 提取的概念

- [Checkpoint-and-Resume](concepts/Checkpoint-and-Resume.md)

- [Delegated Approval](concepts/Delegated Approval.md)

- [Memory-Layered Context](concepts/Memory-Layered Context.md)

- [Ambient Processing](concepts/Ambient Processing.md)

- [Fleet Orchestration](concepts/Fleet Orchestration.md)

- [Agent Runtime](concepts/Agent Runtime.md)

- [Agent Gateway](concepts/Agent Gateway.md)

## 原始文章信息

- 作者：@GoogleCloudTech / @addyosmani / @Saboo_Shubham_

- 来源：X书签

- 发布时间：2026-04-22

- 原文链接：[5 Agent Design patterns for Long-running AI Agents](https://x.com/GoogleCloudTech/status/2046989964077146490)

## 个人评注

这篇文章对 Tizer 的启发是：真正决定 agent 能否进入内容流水线或 HITL 业务环节的，不是一次回答有多聪明，而是能否稳定跨天运行、在审批点暂停、保留记忆并被统一治理。它也提醒我们把“记忆、权限、策略、编排”视作基础设施层，而不是散落在 prompt 里的技巧。
