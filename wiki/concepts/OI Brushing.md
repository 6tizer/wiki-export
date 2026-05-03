---
title: OI Brushing
type: concept
tags:
- 量化交易
status: 草稿
confidence: high
last_compiled: '2026-05-03'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/99ec419f1e5a41cb835c117e091ade91
notion_id: 99ec419f-1e5a-41cb-835c-117e091ade91
---

## 定义

OI Brushing（刷持仓量）是一种订单簿层面的微观操纵手法，做市商通过在期货市场中刻意制造虚假的未平仓合约量（Open Interest），配合 TWAP/冰山单吃单、bid-ask 失衡等策略，制造市场活跃假象并为后续挤仓或清算瀑布创造条件。

## 关键要点

- **核心机制**：通过多钱包协调在期货市场刷出高 OI，让市场看起来流动性充足、参与者众多

- **配套手法**：TWAP/冰山单隐蔽吃单、bid-ask 失衡持续 >0.4、跨交易所价格操纵

- **目的**：为挤仓创造条件——高 OI 意味着更多空头仓位可被清算

- **跨交易所联动**：利用 Aster 等小交易所拉动 Binance mark price，触发主战场的清算

- **检测指标**：OI 异常增长但缺乏对应的链上真实交易量、订单簿事件激增

## 来源引用

- [摘要：我只想说一句，这文章太tm牛逼了！](summaries/摘要：我只想说一句，这文章太tm牛逼了！.md)（[原文](https://x.com/0xKevin00/status/2050478908462805171)）
