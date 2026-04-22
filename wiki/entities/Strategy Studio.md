---
title: Strategy Studio
type: entity
tags:
- Crypto/DeFi
- 开发工具
status: 草稿
confidence: medium
last_compiled: '2026-04-16'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/b0bc34175be849809fcc9b3da2399233
notion_id: b0bc3417-5be8-4980-9fcc-9b3da2399233
---

### 定义

Strategy Studio 是 Minara 用来重建、逐笔对齐并重跑公开 TradingView 策略的测试平台，用于验证策略在真实交易费用下是否仍然成立。

### 关键要点

- 支持把公开 PineScript 策略重建到统一测试环境。

- 用相同资金、手续费、仓位和日期范围对齐 TradingView 原始回测。

- 可分别在零费率与真实费率下重跑回测，用来分离策略逻辑与执行成本。

- 文中的策略修复案例，都是围绕这一测试平台展开。

### 来源引用

- [We found 21 money-printers after backtesting 236 TradingView strategies](https://x.com/minara/status/2044432012002635843) · @minara · 2026/04/15 · 回测 236 个 TradingView 策略后，我们找到了 21 个真正能赚钱的

### 关联概念

- 逐笔复制验证

- 双费率回测

- 交易频率成本侵蚀
