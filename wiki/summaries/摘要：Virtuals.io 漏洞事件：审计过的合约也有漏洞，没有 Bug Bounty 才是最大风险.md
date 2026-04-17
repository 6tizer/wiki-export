---
title: 摘要：Virtuals.io 漏洞事件：审计过的合约也有漏洞，没有 Bug Bounty 才是最大风险
type: summary
tags:
- Crypto/DeFi
status: 已审核
confidence: high
last_compiled: '2026-04-11'
source_tags: 网络安全, 漏洞, DeFi, Solana
source_article_url: ''
notion_url: https://www.notion.so/c8c6133936e84b3fb683415e0a5bfa3a
notion_id: c8c61339-36e8-4b3f-b683-415e0a5bfa3a
---

**一句话摘要**：安全研究员 Jinu 在 Virtuals Protocol 发现合约地址可预测导致预先占位的阻断攻击漏洞，项目方无谁小隹且关闭反馈渠道，促使其公开披露，事后建立上限 20 万美元的 Bug Bounty 项目。

**关键洞察**

- 漏洞技术：AgentToken.sol 工具合约地址可预测，攻击者可提前在 Uniswap V2 占位，导致发射流程失败

- 修复思路：CREATE2 + 随机 salt 让合约地址无法被提前计算

- 核心教训：审计是起点而非终点，生产环境需要持续的 Bug Bounty

- Virtuals 此前经过 PeckShield 两轮审计仍未发现该漏洞

- Bug Bounty 生态：Immunefi 在 Web3 赛道几乎是默认选项，已保护超过 1900 亿美元用户资产

**提取的概念**：Virtuals Protocol、Bug Bounty、智能合约安全

**原始文章信息**

- 作者：@lj1nu (jinu)

- 来源：X书签

- 发布时间：2025-01-03

- 链接：[https://x.com/lj1nu/status/1875021257210736870](https://x.com/lj1nu/status/1875021257210736870)

**个人评注**：本事件警示：即使经过审计，没有 Bug Bounty 的项目就无法建立责任吐露格局。
