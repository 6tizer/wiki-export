---
title: operator 驱动撮合
type: concept
tags:
- Crypto/DeFi
status: 草稿
confidence: medium
last_compiled: '2026-04-15'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/601dc4768cf84546a3c88f88636b99e3
notion_id: 601dc476-8cf8-4546-a3c8-8f88636b99e3
---

### 定义

operator 驱动撮合指的是：订单本身只保留更轻量的意图表达，而撮合时机、路径、费用实现和批量执行方式更多由 operator 在执行阶段决定。这意味着系统的控制重心从订单字段转向 operator 与协议级控制面。

### 关键要点

- V2 核心只保留统一的 `matchOrders` 撮合入口

- fee 从订单内声明费率转为执行时传入 fee amount，并受协议级上限约束

- `pauseTrading`、`pauseUser`、`setFeeReceiver` 等函数让运维与风控控制面更强

- 提升扩展性和执行效率，但也把更多正确性与公平性责任转移到 operator 与链下 pipeline

### 来源引用

- 《polymarket ctf exchange v2 分析》｜2026-04-14｜[原文](https://x.com/love_u_4ever/status/2043960259245641785)｜[源页面](https://www.notion.so/343701074b6881069cc0d77b18ffe67b)
