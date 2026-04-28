---
title: pUSD
type: entity
tags:
- 稳定币
- 加密资产
- 链上协议
status: 审核中
confidence: medium
last_compiled: '2026-04-26'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/2e0978fc8b2d4b0b82bf430e8b4cc675
notion_id: 2e0978fc-8b2d-4b0b-82bf-430e8b4cc675
---

### 定义

pUSD 是 Polymarket V2 引入的 wrapped collateral，用来统一承接 `USDC` 与 `USDC.e` 等 underlying asset，并作为 exchange 与 adapter 层之间的标准资产表示。

### 关键要点

- 通过 `CollateralToken` 抽象统一抵押品表示

- 支持 wrap / unwrap，由受控入口和角色权限管理

- 让 legacy `ConditionalTokens` 与 `NegRisk` 路径可以经由 adapter 接入，而不要求 exchange 直接处理多种底层资产

- 提升流动性统一性，但也把权限、升级面与系统风险集中到更少的关键组件

### 来源引用

- [摘要：polymarket ctf exchange v2 分析](summaries/摘要：polymarket ctf exchange v2 分析.md)（2026-04-14，[原文](https://x.com/love_u_4ever/status/2043960259245641785)，[源页面](https://www.notion.so/343701074b6881069cc0d77b18ffe67b)）
