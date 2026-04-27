---
title: 摘要：Bring Your Own Browser
type: summary
tags:
- 浏览器自动化
- MCP 协议
status: 已审核
confidence: high
last_compiled: '2026-04-27'
source_tags: ''
source_article_url: https://www.notion.so/34f701074b68811a9e99cd0665d6de8a
notion_url: https://www.notion.so/Tizer/1f94d77bb7c446d99e3632756cfadb41
notion_id: 1f94d77b-b7c4-46d9-9e36-32756cfadb41
---

## 一句话摘要

byob 是一个开源本地 MCP Server，通过 Chrome Extension + Native Messaging + CDP 让 AI Agent 直接复用用户已登录的真实 Chrome 浏览器，免去 headless 模拟和 Cookie 复制。

## 关键洞察

- **浏览器会话复用**：核心创新在于让 AI Agent 直接使用用户已有的登录态，省去反爬和模拟登录的成本，可直接操作 Twitter、Gmail、Notion 等已认证页面

- **四层本地架构**：AI tool → byob-mcp (stdio) → byob-bridge (Unix socket) → Chrome Extension (Native Messaging) → Chrome DevTools Protocol，全链路本地运行，隐私安全

- **丰富工具集**：提供 30+ 浏览器操作工具（读取、截图、点击、输入、Cookie 导出、网络录制、PDF 打印等），覆盖绝大多数 Agent 浏览器交互场景

- **安全边界设计**：默认屏蔽 `chrome://` 等敏感 URL，支持 URL 黑名单，`browser_eval` 默认关闭，需显式开启

- **社区反馈**：回复线程中多人提到类似方案（opencli、CDP 直连、油猴脚本交互），但 byob 将其封装为通用 MCP 标准接口，兼容 Claude Code / Cursor / Cline 等主流 AI 工具

## 提取的概念

- [byob](entities/byob.md)

- [Native Messaging](concepts/Native Messaging.md)

- [Chrome DevTools Protocol](concepts/Chrome DevTools Protocol.md)

- [MCP 协议](concepts/MCP 协议.md)

## 原始文章信息

- **作者**：@xzdejz（北北）

- **来源**：X 书签

- **发布时间**：2026-04-25

- **原文链接**：[原推文](https://x.com/xzdejz/status/2047924864418501111)

- **GitHub**：[wxtsky/byob](https://github.com/wxtsky/byob)（90★，MIT，TypeScript）

## 个人评注

byob 的思路与 OpenClaw 的浏览器控制需求高度相关——如果 OpenClaw 的 Agent 需要访问已认证的 Web 服务（如交易所后台、社交媒体），byob 提供了一种零配置的本地方案。其 MCP 标准化接口设计也契合 Tizer 的 Harness 工程理念：将浏览器能力封装为标准化 Skill，供不同 Agent 调用。值得关注其安全边界设计是否足够应对多 Agent 并发场景。
