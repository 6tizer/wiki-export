---
title: 摘要：How to Connect Claude to TradingView (FULL GUIDE)
type: summary
tags:
- 量化交易
- MCP 协议
- 浏览器自动化
status: 已审核
confidence: medium
last_compiled: '2026-04-16'
source_tags: ''
source_article_url: https://www.notion.so/344701074b68811fbe87d10a3e4f49dd
notion_url: https://www.notion.so/Tizer/d6e747cb7c04466aa9722d3cb3aa680e
notion_id: d6e747cb-7c04-466a-a972-2d3cb3aa680e
---

### 一句话摘要

这篇文章介绍了如何把 [Claude Code](entities/Claude Code.md) 通过 [TradingView MCP Bridge](entities/TradingView MCP Bridge.md) 接入 TradingView Desktop，让 AI 能直接读取图表数据、操作界面，并辅助完成技术分析、预警管理和 Pine Script 开发。

### 关键洞察

- 文章的核心价值不是“自动交易”，而是把 TradingView 变成可被 AI 读取和操作的研究终端

- 这套方案的关键桥梁是 [MCP 协议](concepts/MCP 协议.md)，而底层连接能力则依赖 [Chrome DevTools Protocol](concepts/Chrome DevTools Protocol.md)

- 与单纯看截图不同，作者强调 Claude 读取的是图表底层数值和界面状态，因此更适合做研究、指标调试和工作流自动化

- 实际使用门槛并不低，依赖 Node.js、桌面端、付费订阅、远程调试端口和多轮权限确认，离“5 分钟无脑接入”仍有距离

- 更高杠杆的场景包括批量扫描观察列表、生成研究报告、辅助开发 [Pine Script](concepts/Pine Script.md)，而不是替人完成每一个微小界面操作

### 提取的概念

- [TradingView MCP Bridge](entities/TradingView MCP Bridge.md)

- [MCP 协议](concepts/MCP 协议.md)

- [Chrome DevTools Protocol](concepts/Chrome DevTools Protocol.md)

- [Claude Code](entities/Claude Code.md)

- [Pine Script](concepts/Pine Script.md)

### 原始文章信息

- 作者：@milesdeutscher

- 来源：X书签

- 发布时间：2026-04-15

- 原文链接：[https://x.com/milesdeutscher/status/2044536031991763414](https://x.com/milesdeutscher/status/2044536031991763414)

### 个人评注

这类条目对 Tizer 的工作流有两层启发：一层是把现成桌面软件通过 MCP 或 CDP 包装成 Agent 可调用能力，进入内容管线与研究自动化；另一层是提醒我们区分“能接上”与“能稳定跑”，在 HITL 场景里应把它视为高杠杆研究助手，而不是完全自治执行器。
