---
title: byob
type: entity
tags:
- 浏览器自动化
- MCP 协议
- CLI 工具
status: 草稿
confidence: high
last_compiled: '2026-04-28'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/82355333f3b149aea79ca91ad04ba9e5
notion_id: 82355333-f3b1-49ae-a79c-a91ad04ba9e5
---

## 定义

byob（Bring Your Own Browser）是一个本地 MCP Server，让 AI 编程工具（Claude Code、Cursor、Cline、Windsurf 等）直接控制用户**已登录的真实 Chrome 浏览器**，无需 headless 模式或手动复制 Cookie。

别名：Bring Your Own Browser

## 关键要点

- **核心价值**：复用用户已有的浏览器登录态，AI Agent 可直接访问 Twitter、Gmail、Notion 等已登录页面

- **技术架构**：AI tool → byob-mcp (stdio) → byob-bridge (Unix socket) → Chrome Extension (Native Messaging) → Chrome DevTools Protocol

- **安全设计**：完全本地运行，默认屏蔽 chrome:// 等危险 URL，无数据外泄

- **丰富工具集**：支持 30+ 浏览器操作工具（读取、截图、点击、输入、Cookie 导出、PDF 打印等）

- **技术栈**：TypeScript、Chrome Extension MV3、Bun、Native Messaging

## 档案信息

- **GitHub**：[wxtsky/byob](https://github.com/wxtsky/byob)

- **Stars**：90（截至 2026-04-27）

- **License**：MIT

- **语言**：TypeScript

- **创建时间**：2026-04-25

- **作者**：@xzdejz（北北）

## 关联概念

- Native Messaging

- Chrome DevTools Protocol

- MCP 协议

## 来源引用

- [摘要：Bring Your Own Browser](summaries/摘要：Bring Your Own Browser.md)（[原文](https://x.com/xzdejz/status/2047924864418501111)）
