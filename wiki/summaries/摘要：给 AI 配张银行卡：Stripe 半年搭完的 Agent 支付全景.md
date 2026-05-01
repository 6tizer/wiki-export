---
title: 摘要：给 AI 配张银行卡：Stripe 半年搭完的 Agent 支付全景
type: summary
tags:
- 商业/生态
- MCP 协议
- OpenClaw
status: 已审核
confidence: high
last_compiled: '2026-04-11'
source_tags: Agent, 行业观察
source_article_url: ''
notion_url: https://www.notion.so/Tizer/bf53abfae1bb4014af9f8a2da133b8cd
notion_id: bf53abfa-e1bb-4014-af9f-8a2da133b8cd
---

## 一句话摘要

Stripe 在半年内推出六层 Agent 支付基础设施（ACP、SPT、ACS、x402、MPP、Toolkit），覆盖「AI 帮人买东西」和「机器给机器付钱」两大场景，给 Agent 配一张银行卡已成现实。

## 关键洞察

- **六层架构**：ACP（交易协议）、SPT（支付令牌）、ACS（商家套件）、x402（链上微支付）、MPP（统一机器支付协议）、Toolkit/MCP

- **两个场景分离**：「AI 帮人买东西」需要用户确认，「机器给机器付钱」完全自主无人介入

- **ACP 协议开放**：OpenAI+Stripe 联合发布，Apache 2.0，Shopify 100万+商家已接入

- **SPT 安全令牌**：锁定商家+金额+过期时间，卡号不暴露给 Agent 或商家

- **x402 微支付**：HTTP 402 状态码，USDC 链上按次付费，最低 0.001 美元，7x24 即时结算

- **虚拟卡**：Stripe Issuing 让 Agent 创建一次性虚拟 Visa 卡，用完即销毁

## 提取的概念

- ACP 协议

- x402 协议

- SPT 支付令牌

## 原始文章信息

- **作者**: 赛博禅心

- **来源**: 微信公众号

- **发布时间**: 2026-03-27

## 个人评注

Agent 支付基础设施的成熟意味着 OpenClaw 可以自主完成购买操作，对自动化内容采购、API 调用付费等场景有价值。
