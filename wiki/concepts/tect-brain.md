---
title: tect-brain
type: concept
tags:
- 开发工具
status: 草稿
confidence: high
last_compiled: '2026-04-11'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/034e43597f8a478d8d91aadb7a78ca29
notion_id: 034e4359-7f8a-478d-8d91-aadb7a78ca29
---

**定义**：tect-brain 是一个用 Rust 实现的 AI 技术情报分析系统，通过多源交叉验证（五个情报源）分析技术趋势，并支持通过 MCP 协议对外提供情报服务。

**关键特性**

- 五源交叉验证：包括 GitHub Trending、多个专业情报源的交叉分析

- 独立调度机制：情报采集与分析可在后台自主运行

- MCP 服务器：外部 AI 应用可直接调用 tect-brain 的情报能力

- 终端仪表盘：将不同来源的情报展示在一个交互界面

- 定位为「自我进化情报系统」，具备预测校准能力

**来源引用**

- [摘要：Rust 实现的 tect-brain 大更新：增加了 GitHub Trending & mcp 能力，交互体验大幅上升](summaries/摘要：Rust 实现的 tect-brain 大更新：增加了 GitHub Trending & mcp 能力，交互体验大幅上升.md)
