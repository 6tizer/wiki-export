---
title: Mediator 层
type: concept
tags: []
status: 审核中
confidence: medium
last_compiled: '2026-04-20'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/dab0edc74cc34520b248d33423b7628c
notion_id: dab0edc7-4cc3-4520-b248-d33423b7628c
---

## 定义

Mediator 层是位于 Agent 核心与外部能力模块之间的治理层，负责控制系统如何调用外部能力，以及外部状态如何安全地流回主循环。

## 关键要点

- 它通常承载沙箱、可观测性、压缩、评估、审批回路与子 Agent 编排等治理能力

- 它的价值不在于新增知识，而在于约束知识、技能与工具如何被调用和回流

- 把 mediator 单独抽象出来，可以让 Harness 设计从“能不能接上”升级为“如何被治理”

## 关联概念

- [Agent Harness](concepts/Agent Harness.md)

- [Agent Skills](concepts/Agent Skills.md)

- [记忆分层架构](concepts/记忆分层架构.md)

- [Sandbox Agents](concepts/Sandbox Agents.md)

- [Evals](concepts/Evals.md)

- [Agent 协议层](concepts/Agent 协议层.md)

## 来源引用

- [摘要：Memory](summaries/摘要：Memory.md)（[原文](https://x.com/akshay_pachaar/status/2045510648474530263)）
