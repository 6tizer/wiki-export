---
title: preapprove 机制
type: concept
tags:
- 链上协议
- 加密资产
status: 审核中
confidence: medium
last_compiled: '2026-04-27'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/dc0d5252eb3d4d2b921f8bd6a2276451
notion_id: dc0d5252-eb3d-4d2b-921f-8bd6a2276451
---

### 定义

preapprove 机制是指 operator 先验证订单签名并把结果缓存到链上，后续撮合时可在空签名条件下直接按 `orderHash` 检查预授权状态，从而降低重复验签成本。

### 关键要点

- 入口函数是 `preapproveOrder(order)`

- 后续 `matchOrders` 遇到空签名时，只需检查该订单是否已被 preapproved

- 主要收益是减少 `ECDSA.recover` 或 `EIP-1271` 重复校验带来的 gas 与 calldata 成本

- 它不会锁定资金，也不保证 maker 余额、allowance 或执行成功

### 来源引用

- [摘要：polymarket ctf exchange v2 分析](summaries/摘要：polymarket ctf exchange v2 分析.md)｜2026-04-14｜[原文](https://x.com/love_u_4ever/status/2043960259245641785)｜[源页面](https://www.notion.so/343701074b6881069cc0d77b18ffe67b)
