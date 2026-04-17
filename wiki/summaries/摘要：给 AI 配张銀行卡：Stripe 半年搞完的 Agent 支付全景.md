---
title: 摘要：给 AI 配张銀行卡：Stripe 半年搞完的 Agent 支付全景
type: summary
tags:
- 商业/生态
status: 已审核
confidence: high
last_compiled: '2026-04-11'
source_tags: Agent, LLM, 自动化
source_article_url: ''
notion_url: https://www.notion.so/c5761d5885b8414db01b1b57397e39f3
notion_id: c5761d58-85b8-414d-b01b-1b57397e39f3
---

**一句话摘衑**：Stripe 半年内推出六层 Agent 支付基础设施，覆盖“帮人买东西”和“机器给机器付錢”两个核心场景，给 AI Agent 加一张銀行卡已是两分钟跨通的现实。

**关键洞察**

- 六层架构：**ACP**（AI 与商家交易协议）+ **SPT**（安全支付令牌）+ **ACS**（商家低代码接入）+ **x402**（链上稳定币按次付费）+ **MPP**（统一机器支付协议）+ **Agent Toolkit/MCP**

- 两个场景：“帮人买东西” vs “机器给机器付錢”——完全不同的交易流程

- x402：利用 HTTP 402 状态码，支持低至 0.001 美元的微支付，即时结算，7×24 小时

- Agent Toolkit 让 Agent 可直接通过 MCP 创建一次性虚拟 Visa 卡，锁定金额和商家，用完即销毁

- Stripe 判断：2026 年 95%的 AI 平台驱动电商交易仍将在商家自己的网站上完成

**提取的概念**

- ACP 协议（Agentic Commerce Protocol，AI 与商家统一交易接口协议）

- x402（基于 HTTP 402 的机器对机器微支付协议）

**原始文章信息**

- 作者：赛博禦心 | 来源：微信公众号 | 发布时间：2026-03-27

- 链接：[https://mp.weixin.qq.com/s?__biz=MzkzNDQxOTU2MQ==&mid=2247514678](https://mp.weixin.qq.com/s?__biz=MzkzNDQxOTU2MQ%3D%3D&mid=2247514678)

**个人评注**

对 Tizer 有長期参考价值：如果未来 OpenClaw 要自主调用外部服务并付费， Stripe Agent Toolkit 提供了完整的支付基础设施支持。
