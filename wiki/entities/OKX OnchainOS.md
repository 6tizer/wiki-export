---
title: OKX OnchainOS
type: entity
tags:
- Crypto/DeFi
status: 审核中
confidence: medium
last_compiled: '2026-04-27'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/fd4bc1239c104c8aa462b8a8fb930a10
notion_id: fd4bc123-9c10-4c8a-a462-b8a8fb930a10
---

## 定义

OKX OnchainOS 是 OKX Wallet 打造的**链上开发平台**，将钱包、DEX 交易、行情数据、链上支付、DApp 连接等能力打包成 AI Agent 可直接调用的工具——以 **Skills（技能包）** 和 **MCP Server** 两种形式对外提供。

## 核心亮点

- **Agentic Wallet**：私钥生成与签名全程在 TEE 中完成，AI Agent 可通过自然语言驱动链上交易

- 覆盖 **60+ 主流公链**，**500+ DEX 流动性来源**

- 13 个技能模块：包括钱包鉴权、DEX 聚合、实时价格、聪明钱/KOL/巨鲸信号追踪、Meme 土狗扫描、安全扫描、DeFi 投资、x402 协议支付等

- 用 **Rust** 编写，注重性能与安全性

## 接入方式

- Skills（推荐）：`npx skills add okx/onchainos-skills`，支持 Claude Code、Cursor、OpenClaw 等主流 Agent

- MCP Server：在 Agent 中添加 MCP Server，名称 `onchainos-mcp`

## 同类方案对比

| 方案 | 定位 | 特点 |

| --- | --- | --- |

| OKX OnchainOS | 交易所背书的链上 AI 基础设施 | TEE 钱包安全、500+ DEX 流动性、官方维护 |

| GOAT SDK | 最大开源 Agentic Finance 工具包 | 200+ 工具，支持任意 Agent 框架 |

| Binance Skills Hub | 中心化交易所+链上数据 | 包括 CEX 现货/合约执行 |

## 来源引用

- 摘要：OKX OnchainOS 接入 OpenClaw：五步让 AI Agent 自主执行链上交易

- 摘要：OKX OnchainOS Signal：让 AI Agent 替你盯住聪明钱、KOL 和巨鲸的每一笔买入

- [原文链接](https://x.com/oooooyoung/status/2033381962673766468)｜《AI 打狗时代来了？用 OKX OnchainOS + OpenClaw 让 Agent 替你链上自动交易》｜来源条目：[摘要：AI 打狗时代来了？用 OKX OnchainOS + OpenClaw 让 Agent 替你链上自动交易](summaries/摘要：AI 打狗时代来了？用 OKX OnchainOS + OpenClaw 让 Agent 替你链上自动交易.md)

## 关联概念

- [OnchainOS Signal](concepts/OnchainOS Signal.md)

- [聪明钱信号](concepts/聪明钱信号.md)

- 《OKX OnchainOS Signal：让 AI Agent 替你盯住聪明钱、KOL 和巨鲸的每一笔买入》（OKX中文，2026-03-06）— 补充其 Signal 能力如何把链上监控压缩为结构化买入信号
