---
title: CTF Collateral Adapter
type: concept
tags:
- 加密资产
- 稳定币
- 链上协议
- 商业/生态
status: 草稿
confidence: medium
last_compiled: '2026-04-26'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/1867d67f7e694d14b0bd09a4c6ff3003
notion_id: 1867d67f-7e69-4d14-b0bd-09a4c6ff3003
---

### 定义

CTF Collateral Adapter 是 Polymarket V2 中把 `pUSD` 接回 legacy `ConditionalTokens` 体系的适配层。它负责在 wrapped collateral 与旧有 CTF 头寸之间做转换。

### 关键要点

- 在 `splitPosition` 路径中把 `pUSD` unwrap 成 `USDC.e` 后再调用 legacy `ConditionalTokens`

- 在 `mergePositions` 与 `redeemPositions` 路径中再把回收的 `USDC.e` wrap 成 `pUSD`

- 说明 V2 并未替换底层 CTF，而是在其上增加统一资产层与兼容层

- 这是 V2 从“单体 exchange”转向“wrapped collateral + adapter + exchange”架构的核心部件之一

### 来源引用

- [摘要：polymarket ctf exchange v2 分析](summaries/摘要：polymarket ctf exchange v2 分析.md)｜2026-04-14｜[原文](https://x.com/love_u_4ever/status/2043960259245641785)｜[源页面](https://www.notion.so/343701074b6881069cc0d77b18ffe67b)
