---
title: delta-based accounting
type: concept
tags:
- 加密资产
- 链上协议
status: 草稿
confidence: medium
last_compiled: '2026-04-26'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/828263d7c4ae40bd897fd80adab51ebc
notion_id: 828263d7-c4ae-40bd-897f-d80adab51ebc
---

### 定义

delta-based accounting 是一种通过结算前后余额增量来确认本次真实收付数量的记账方式，用来避免把 exchange 账户原本就存在的余额误计入当前撮合结果。

### 关键要点

- 在 maker settlement 前后记录 `balanceBefore` 与 `balanceAfter`

- 用余额变化量而不是绝对余额计算本次实际收到的资产

- 相比直接读取账户余额，更能避免历史残留余额污染结算结果

- 在复杂批量结算路径中，这种记账方式能提升结算稳健性

### 来源引用

- [摘要：polymarket ctf exchange v2 分析](summaries/摘要：polymarket ctf exchange v2 分析.md)｜2026-04-14｜[原文](https://x.com/love_u_4ever/status/2043960259245641785)｜[源页面](https://www.notion.so/343701074b6881069cc0d77b18ffe67b)
