---
title: Agent 技能市场
type: concept
tags:
- Agent 协作模式
- 链上协议
status: 草稿
confidence: medium
last_compiled: '2026-04-29'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/af224f2a4c534ec385a845cfcf147a07
notion_id: af224f2a-4c53-4ec3-85a8-45cfcf147a07
---

## 定义

Agent 技能市场是一种让 AI Agent 在链上公开注册、展示并交易自身能力的市场范式。Agent 将自己擅长的技能（skill）挂牌出售，其他 Agent 可以发现并购买这些技能服务，每次调用的质量由协议自动评分，结算在链上完成，不合格的服务自动退款。

## 技术特点

- **技能注册与发现**：Agent 通过 SkillRegistry 合约注册技能，每个技能对应一个 ERC-20 RunToken（通过 CREATE2 部署），用于结算

- **链上质量评分**：每次调用（session）的交付结果、格式、延迟等由协议自动评估并打分 pass/fail

- **信誉系统**：基于成功率、评分、完成任务数和 attestation 历史构建复合信誉分，排行榜完全基于链上数据

- **链上 attestation**：所有评估结果通过 BAS（BNB Attestation Service）等服务在链上存证，不可撤销

- **自动退款机制**：当提供方通过率低于阈值（如 80%），买方自动获得退款

- **身份与托管标准**：使用 ERC-8004（身份注册）和 ERC-8183（托管会话）等标准

## 意义

Agent 技能市场是 Agent 经济走向真正「分工协作」的基础设施——Agent 不再需要全能，而是可以通过市场找到互补能力并为之付费，形成专业化分工的 Agent 生态。

## 来源引用

- [摘要：BNB Hack: US College Edition winners are in!](summaries/摘要：BNB Hack- US College Edition winners are in!.md)（[原文](https://x.com/BNBChainDevs/status/2049458833391853569)）

## 关联概念

- [链上信用评分](concepts/链上信用评分.md)

- [x402 协议](concepts/x402 协议.md)
