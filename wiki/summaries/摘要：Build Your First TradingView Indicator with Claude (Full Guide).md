---
title: 摘要：Build Your First TradingView Indicator with Claude (Full Guide)
type: summary
tags: []
status: 已审核
confidence: high
last_compiled: '2026-04-23'
source_tags: ''
source_article_url: https://www.notion.so/34b701074b6881948cfcd44724ddd4df
notion_url: https://www.notion.so/Tizer/a7a340a8ee194d14a6566bf9a786e329
notion_id: a7a340a8-ee19-4d14-a656-6bf9a786e329
---

## 一句话摘要

这篇文章展示了如何把 [Claude Code](entities/Claude Code.md) 连接到 TradingView 桌面端，并用分步骤提示词快速构建一个基于 [Open Interest](concepts/Open Interest.md) 的 [ZCT Momentum Filter](concepts/ZCT Momentum Filter.md) 指标。

## 关键洞察

- 真正有价值的不是“Claude 能连上 TradingView”，而是把连接、脚本生成、编译验证和保存脚本串成一条可重复的工作流。

- 文中采用“一次一个改动”的增量构建方式，先连通环境，再逐步添加 OI 主线、EMA、颜色填充和参数面板，降低了 AI 生成代码时的调试成本。

- 这个指标把未平仓量与快慢均线结合起来，用来区分突破延续、下跌延续与震荡反转三种交易环境，而不是直接给出买卖点。

- 作者反复强调会话态和人工保存的重要性：MCP 注入是 session-only，真正长期可用还需要用户手动保存到 TradingView 账户。

- 从工作流视角看，这是一种把自然语言需求转成可执行交易研究工具的范例，适合复制到其他指标和研究脚本的开发上。

## 提取的概念

- [Claude Code](entities/Claude Code.md)

- [TradingView MCP Bridge](entities/TradingView MCP Bridge.md)

- [Pine Script](concepts/Pine Script.md)

- [Open Interest](concepts/Open Interest.md)

- [ZCT Momentum Filter](concepts/ZCT Momentum Filter.md)

## 原始文章信息

- 作者：@KoroushAK

- 来源：X书签

- 发布时间：2026-04-22

- 原文链接：[Build Your First TradingView Indicator with Claude (Full Guide)](https://x.com/KoroushAK/status/2046950514743529688)

- 源文章页面：用 Claude Code 给 TradingView 写指标：从零到 OI 动量过滤器全流程

## 个人评注

这篇内容对 Tizer 的价值不在“做交易指标”本身，而在于它验证了一个很强的模式：让 AI 编程 Agent 直接接管垂直软件的操作层，再通过增量提示词把领域知识沉淀成可保存、可复用的资产。对 OpenClaw、HITL 和内容流水线来说，这种“工具接入 + 小步验证 + 最终固化”的结构非常值得复用。
