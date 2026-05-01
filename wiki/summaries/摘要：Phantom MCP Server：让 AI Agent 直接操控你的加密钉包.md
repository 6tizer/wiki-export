---
title: 摘要：Phantom MCP Server：让 AI Agent 直接操控你的加密钉包
type: summary
tags:
- 加密资产
- MCP 协议
- OpenClaw
status: 已审核
confidence: high
last_compiled: '2026-04-11'
source_tags: Agent, OpenClaw, 自动化
source_article_url: ''
notion_url: https://www.notion.so/Tizer/2d448245e778471795340ac95156e8b7
notion_id: 2d448245-e778-4717-9534-0ac95156e8b7
---

## 一句话摘要

Phantom 正式推出 MCP Server，将钉包功能封装成 AI 可调用的标准工具接口，让 AI Agent 可以直接完成转账、签名和代币兑换——钉包正在从“签名确认工具”演化为“Agent 执行层”。

## 关键洞察

- **5 个核心工具**：`get_wallet_addresses`、`sign_transaction`、`transfer_tokens`、`buy_token`、`sign_message`——覆盖 Solana/ETH/BTC/Sui 四链

- **Phantom 的背书**：2000 万用户、$30 亿美元估值、Paradigm/Sequoia/a16z 投资，不是个人周末项目

- **严重安全警示**：Phantom 官方明确标注「手动 —— 請务必使用专门测试账户，测试账户中不应存放重要资产」

- **提示注入风险**：`transfer_tokens` 和 `buy_token` 两个工具一旦执行就立即提交，被躻导攻击后可能造成资产转移

- **MCP 协议意义**：AnthropicAnthropic 2024 年底推出 MCP 标准，Phantom MCP Server 是将其应用到 Web3 钉包的首批成熟实践

## 提取的概念

OpenClaw

## 原始文章信息

- **作者**：@phantom

- **来源**：X 书签

- **链接**：[https://x.com/phantom/status/2023866789860675625](https://x.com/phantom/status/2023866789860675625)

## 个人评注

这篇文章展示了 AI Agent + Web3 钉包的重要趨势。对于 Tizer 理解 MCP 协议如何将 AI 能力延伸到 Web3 领域有直接参考价值，但安全风险需要优先评估。
