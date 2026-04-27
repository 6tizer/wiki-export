---
title: TradingView MCP Bridge
type: entity
tags:
- Agent 技能
- Coding Agent
status: 审核中
confidence: medium
last_compiled: '2026-04-27'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/8fe8c2b16ae54741858dd0dcbded9eac
notion_id: 8fe8c2b1-6ae5-4741-858d-d0dcbded9eac
---

## 定义

TradingView MCP Bridge 是一个把 [Claude Code](entities/Claude Code.md) 与本地运行的 TradingView Desktop 连接起来的 MCP 服务器，通过 Chrome DevTools Protocol 读取图表状态、执行界面操作，并把这些能力暴露为可调用工具。

## 关键要点

- 以本地桌面应用为宿主，不直接连接 TradingView 官方 API，而是通过本机调试端口与桌面客户端通信

- 既支持图表读取，也支持界面控制、指标管理、截图、预警管理、回放练习和 Pine Script 相关操作

- 典型定位不是自动交易机器人，而是让 AI 在交易研究场景中充当“读图 + 操作 + 辅助开发”的个人助手

- 依赖前提明确，包括 Node.js 18+、TradingView Desktop、有效订阅，以及用户手动开启远程调试端口

- 稳定性受 TradingView Desktop 内部实现变化影响，存在版本漂移和维护风险

## 来源引用

- [原文链接](https://x.com/milesdeutscher/status/2044536031991763414)｜[摘要：How to Connect Claude to TradingView (FULL GUIDE)](summaries/摘要：How to Connect Claude to TradingView (FULL GUIDE).md)｜源文章：Claude × TradingView：用 MCP 把 AI 变成你的专属交易桌面助手

- [摘要：Build Your First TradingView Indicator with Claude (Full Guide)](summaries/摘要：Build Your First TradingView Indicator with Claude (Full Guide).md)（[原文](https://x.com/KoroushAK/status/2046950514743529688)）

## 关联概念

- [MCP 协议](concepts/MCP 协议.md)

- [Chrome DevTools Protocol](concepts/Chrome DevTools Protocol.md)

- [Claude Code](entities/Claude Code.md)

- [Pine Script](concepts/Pine Script.md)

- [Open Interest](concepts/Open Interest.md)

- [ZCT Momentum Filter](concepts/ZCT Momentum Filter.md)
