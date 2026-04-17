---
title: 摘要：polymarket ctf exchange v2 分析
type: summary
tags:
- Crypto/DeFi
status: 已审核
confidence: high
last_compiled: '2026-04-15'
source_tags: ''
source_article_url: https://www.notion.so/343701074b6881069cc0d77b18ffe67b
notion_url: https://www.notion.so/c7ed378881044615a369f7d55d908fea
notion_id: c7ed3788-8104-4615-a369-f7d55d908fea
---

### 一句话摘要

Polymarket 的 `ctf-exchange-v2` 不是对 V1 的小修小补，而是一次围绕 **operator 驱动执行、统一 collateral、adapter 兼容层与批量结算优化** 展开的协议级重构。

### 关键洞察

- V2 把系统从“单体 exchange 合约”重组为“exchange + `pUSD` + adapter”的分层架构，协议边界明显外扩。

- 新版 `Order` 删除 `nonce`、`expiration`、`feeRateBps` 等字段，说明执行控制正在从订单本身转向 operator 与协议级控制面。

- `preapprove` 把签名校验缓存为链上状态，主要优化的是重复撮合时的 gas 和 calldata，而不是成交保证。

- 删除 `NonceManager` 后，V2 缓解了通过 bump nonce 恶意让订单失效的问题，但 non-custodial 模型下的余额与 allowance 变化仍可能导致执行失败。

- `COMPLEMENTARY`、`MINT`、`MERGE` 三类结算路径加上 batched settlement 与 delta-based accounting，体现了 V2 对生产级撮合效率与结算稳健性的重视。

### 提取的概念

- [ctf-exchange-v2](entities/ctf-exchange-v2.md)

- [pUSD](entities/pUSD.md)

- [preapprove 机制](concepts/preapprove 机制.md)

- [operator 驱动撮合](concepts/operator 驱动撮合.md)

- [CTF Collateral Adapter](concepts/CTF Collateral Adapter.md)

- [delta-based accounting](concepts/delta-based accounting.md)

### 原始文章信息

- 作者：@love_u_4ever

- 来源：X书签

- 发布时间：2026-04-14

- 链接：[https://x.com/love_u_4ever/status/2043960259245641785](https://x.com/love_u_4ever/status/2043960259245641785)

### 个人评注

这篇分析对 Tizer 的启发不只是理解 Polymarket 的合约升级，更重要的是识别一种常见的系统演化路径：**把原先写死在对象里的规则，逐步上移到执行层与控制层**。这和 HITL、Agent orchestration、内容流水线里的“意图层 / 执行层分离”非常相似。若后续要沉淀为 OpenClaw 或工作流知识，可以重点追踪 operator 权限边界、执行可验证性，以及 preapprove 是否会演化为隐性优先级通道。
