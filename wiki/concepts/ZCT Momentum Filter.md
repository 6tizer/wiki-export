---
title: ZCT Momentum Filter
type: concept
tags:
- Crypto/DeFi
- 开发工具
status: 审核中
confidence: medium
last_compiled: '2026-04-23'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/74d134438a734900bdea66fbe200d09b
notion_id: 74d13443-8a73-4900-bdea-66fbe200d09b
---

## 定义

ZCT Momentum Filter 是文中演示构建的 Pine Script 指标，通过对当前品种的 Open Interest 及其 60/240 周期 EMA 进行可视化，帮助交易者快速区分突破、下行和震荡反转环境。

## 关键要点

- 核心输入是当前 symbol 的 `_OI` 数据，并乘以 close 转成美元计价 OI

- 指标在独立面板中绘制 OI 主线、快慢 EMA，并用红绿填充显示二者关系

- 设计强调“one prompt, one change”的增量构建方式，适合让 AI 与人类共同验证每一步

- 指标本身不是自动交易系统，而是帮助识别动量是否持续、是否适合追趋势或做区间反转

## 来源引用

- [摘要：Build Your First TradingView Indicator with Claude (Full Guide)](summaries/摘要：Build Your First TradingView Indicator with Claude (Full Guide).md)（[原文](https://x.com/KoroushAK/status/2046950514743529688)）

## 关联概念

- [Pine Script](concepts/Pine Script.md)

- [TradingView MCP Bridge](entities/TradingView MCP Bridge.md)

- [Claude Code](entities/Claude Code.md)
