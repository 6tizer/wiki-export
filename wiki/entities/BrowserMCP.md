---
title: BrowserMCP
type: entity
tags:
- 浏览器自动化
- MCP 协议
status: 草稿
confidence: medium
last_compiled: '2026-05-02'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/69236b2058e645c5a8979da165e5b159
notion_id: 69236b20-58e6-45c5-a897-9da165e5b159
---

## 定义

BrowserMCP 是官方推出的一款基于 MCP 协议的浏览器集成工具。它可以直接连接用户当前正在使用的浏览器实例，将页面内容、DOM 结构和可操作能力暴露给 AI，使 AI 能够在不重新启动浏览器的情况下，基于当前浏览器上下文继续操作。

**别名**：browsermcp

## 关键要点

- **当前上下文友好**：不需要重新拉起浏览器或重跑自动化流程，直接读取用户当前浏览器状态

- **基于 MCP 协议**：通过 MCP 协议将浏览器能力暴露给 AI Agent

- **DOM 理解自然**：对 DOM 结构的理解和操作比传统方案更自然

- **能力尚有限制**：目前不支持文件选择等部分操作，覆盖场景还不完整

- **适合调试场景**：对日常写代码、排查问题、调试前端页面特别方便

## 关联概念

- Chrome DevTools Protocol（底层浏览器控制协议）

- browser-use（面向 AI Agent 的浏览器操作封装）

- Midscene（视觉驱动的 UI 自动化框架）

- Playwright（DOM 自动化框架）

## 来源引用

- [摘要：一文彻底了解浏览器自动化，cdp、playwright、browser-user、midscene、browsermcp](summaries/摘要：一文彻底了解浏览器自动化，cdp、playwright、browser-user、midscene、browsermcp.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzU5ODg1NDk1Ng%3D%3D&mid=2247484662&idx=1&sn=86710f5235fc8287ed0fdf470145617d&chksm=ffb825b8a302ea2f0bb235145fc1d6b62eb3c0ad603642f1d2e993302656ef5c5996f49a76c5#rd)）
