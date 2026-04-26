---
title: ATR 追踪止损
type: concept
tags:
- 量化交易
status: 草稿
confidence: medium
last_compiled: '2026-04-16'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/926d25fa24df4562a137823571d6585e
notion_id: 926d25fa-24df-4562-a137-823571d6585e
---

### 定义

ATR 追踪止损，是一种用平均真实波幅来动态设定初始止损和跟踪止损距离的风险控制方法，让止损尺度随波动率变化而调整。

### 关键要点

- 文中多个策略修复案例都把固定止损改为 ATR 初始止损加 ATR trailing stop。

- 这样可以避免在高波动环境中过早被噪音扫出，也能在趋势延续时逐步锁定利润。

- 该方法的价值不在提高胜率本身，而在改善回撤和盈亏结构。

- 它是文章里最反复出现的结构性优化手段之一。

### 来源引用

- [We found 21 money-printers after backtesting 236 TradingView strategies](https://x.com/minara/status/2044432012002635843) · @minara · 2026/04/15 · 回测 236 个 TradingView 策略后，我们找到了 21 个真正能赚钱的

### 关联概念

- 交易频率成本侵蚀

- 双费率回测

- Strategy Studio
