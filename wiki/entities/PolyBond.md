---
title: PolyBond
type: entity
tags:
- 量化交易
- AI 产品
status: 草稿
confidence: medium
last_compiled: '2026-04-27'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/5d9c4e9025ad4941b55c8afa1e65f7ef
notion_id: 5d9c4e90-25ad-4941-b55c-8afa1e65f7ef
---

## 定义

PolyBond 是由 @0xJeff 使用 Claude + Hermes Agent 构建的个人预测市场仪表盘，用于从多个数据源聚合交易机会。

## 核心功能

- 聚合鲸鱼/聪明钱信号（sharp/whale signals）

- 检测潜在内幕人士大额押注

- 追踪 LLM 预测器（来自 predictionarena）

- 整合多平台机会（SN6 Numinous、Manifold 等）

- 目标：成为发现高确定性预测市场机会的一站式工具，替代 DeFi 收益

## 技术架构

- **构建端**（Builder）：Claude 负责前端仪表盘搭建，速度快、界面美观

- **运营端**（Operator）：Hermes Agent 作为预测市场分析师，每日早间及每隔数小时扫描数据源，推送简报

- 用户可要求 Hermes 展开详细分析

## 关联概念

- [Builder-Operator 模式](concepts/Builder-Operator 模式.md)

- [Hermes Agent](entities/Hermes Agent.md)

- [Claude Code](entities/Claude Code.md)

## 来源引用

- [摘要：1 Month with Hermes - I've been using Hermes wrong all along](summaries/摘要：1 Month with Hermes - I've been using Hermes wrong all along.md)（[原文](https://x.com/0xJeff/status/2048678335950311860)）
