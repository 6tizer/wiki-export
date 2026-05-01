---
title: CLOB API
type: concept
tags:
- 量化交易
- 商业/生态
- Agent 协作模式
status: 审核中
confidence: medium
last_compiled: '2026-04-23'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/bcc817ee42434cf0b737d1cfd5ffcfe3
notion_id: bcc817ee-4243-4cf0-b737-d1cfd5ffcfe3
---

## 定义

CLOB API 指面向中央限价订单簿（Central Limit Order Book）的程序化接口，允许策略系统读取订单簿、提交委托、取消订单并管理执行状态。

## 关键要点

- 是量化交易与做市系统连接交易场所的核心执行接口

- 对延迟、签名、订单状态管理和风控都有较高要求

- 在 Polymarket 场景里，它连接的是预测市场订单簿而不是传统交易所撮合界面

## 来源引用

- [摘要：28 tools under the hood of bot that made $1M on Polymarket](summaries/摘要：28 tools under the hood of bot that made $1M on Polymarket.md)（[原文](https://x.com/antpalkin/status/2046654122892403188)）
