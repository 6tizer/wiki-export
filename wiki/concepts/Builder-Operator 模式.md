---
title: Builder-Operator 模式
type: concept
tags:
- Agent 协作模式
- Harness 工程
status: 草稿
confidence: medium
last_compiled: '2026-04-27'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/dedf81d62ee4458e8ad0503c25424f2d
notion_id: dedf81d6-2ee4-458e-8ad0-503c25424f2d
---

## 定义

Builder-Operator 模式是一种 AI 工具角色分工策略：将 AI Agent 按使用场景拆分为两类角色——**Builder**（构建者）负责一次性创建任务（如搭建仪表盘、网站、文档），**Operator**（运营者）负责持续性自动化任务（如定时报告、数据分析、个性化提醒）。

该模式由 @0xJeff 在使用 Hermes Agent 一个月后总结提出：Claude 适合做 Builder（生成速度快、UI 美观、内置产品化工具），Hermes 适合做 Operator（持久记忆 + 自学习循环 + 跨会话上下文保持）。

## 核心要点

- **Builder 特征**：一次性构建任务、注重输出质量和美观度、适合有产品化 UI 的工具（Claude Artifacts、Codex）

- **Operator 特征**：持续性自动化任务、注重记忆持久性和个性化学习、适合有 persistent memory 的 Agent（Hermes）

- **分工原则**：不要让 Operator 做构建，也不要让 Builder 做运营——各取所长

- **典型组合**：Claude（Builder）+ Hermes（Operator），Codex（Builder）+ Hermes（Operator）

## 适用场景

- 个人数据仪表盘：Claude 构建前端，Hermes 定时分析数据并推送报告

- 投资/交易工作流：Claude 搭建监控面板，Hermes 每日扫描并汇报关键信号

- 知识管理：Claude 生成模板和结构，Hermes 持续整理和更新内容

## 关联概念

- [Hermes Agent](entities/Hermes Agent.md)

- [PolyBond](entities/PolyBond.md)

- [Hermes Agent Self-Evolution](entities/Hermes Agent Self-Evolution.md)

- [Claude Code](entities/Claude Code.md)

## 来源引用

- [摘要：1 Month with Hermes - I've been using Hermes wrong all along](summaries/摘要：1 Month with Hermes - I've been using Hermes wrong all along.md)（[原文](https://x.com/0xJeff/status/2048678335950311860)）
