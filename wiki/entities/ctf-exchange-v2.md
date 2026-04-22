---
title: ctf-exchange-v2
type: entity
tags:
- Crypto/DeFi
status: 草稿
confidence: medium
last_compiled: '2026-04-15'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/40af4be5048740b5889a6fb841cea8c7
notion_id: 40af4be5-0487-40b5-889a-6fb841cea8c7
---

### 定义

ctf-exchange-v2 是 Polymarket 在 V2 中重写的 CTF 交易协议核心。它不再只是 V1 的小版本升级，而是围绕 **统一抵押品、adapter 兼容层、operator 执行控制与批量结算优化** 进行的系统级重构。

### 关键要点

- 用 `pUSD` 统一 exchange 层处理的 collateral 表达

- 删除 `NonceManager` 与 `Registry`，减少基于 nonce 的统一失效和静态 token 注册依赖

- 新 `Order` 结构移除 `taker`、`expiration`、`nonce`、`feeRateBps`，改由更轻量的订单结构配合协议级控制面执行

- 将结算路径拆分为 `COMPLEMENTARY`、`MINT`、`MERGE`，并通过 batch settlement 降低多 maker 场景 gas

### 来源引用

- 《polymarket ctf exchange v2 分析》｜2026-04-14｜[原文](https://x.com/love_u_4ever/status/2043960259245641785)｜[源页面](https://www.notion.so/343701074b6881069cc0d77b18ffe67b)
