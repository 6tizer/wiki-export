---
title: Native Messaging
type: concept
tags:
- 浏览器自动化
status: 草稿
confidence: medium
last_compiled: '2026-04-28'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/67a3699f4efa48bcb818d7fee5a8c6b1
notion_id: 67a3699f-4efa-48bc-b818-d7fee5a8c6b1
---

## 定义

Native Messaging 是 Chrome 浏览器提供的一种 API 机制，允许 Chrome Extension 与用户本地安装的原生应用程序进行双向通信。扩展通过 `chrome.runtime.connectNative()` 或 `chrome.runtime.sendNativeMessage()` 向注册的本地 Host 进程发送消息，Host 通过 stdin/stdout 交换 JSON 数据。

## 关键要点

- **通信模型**：Chrome Extension ↔ Native Host，使用 stdin/stdout 传输 JSON 消息，每条消息前有 4 字节长度头

- **安全边界**：Host 必须在操作系统中注册 manifest（macOS: `~/Library/Application Support/...`，Windows: 注册表），且 manifest 中声明允许的 Extension ID

- **与 CDP 的区别**：Native Messaging 是 Extension→本地进程的通道；Chrome DevTools Protocol (CDP) 是调试协议，用于控制浏览器标签页。byob 同时使用两者——Native Messaging 做 Extension↔Bridge 通信，CDP 做页面操控

- **典型应用**：密码管理器、本地文件系统访问、AI Agent 浏览器控制（如 byob）

- **局限**：Chrome 必须完全重启才能加载新注册的 Native Messaging Host

## 关联概念

- Chrome DevTools Protocol

- byob

- MCP 协议

## 来源引用

- [摘要：Bring Your Own Browser](summaries/摘要：Bring Your Own Browser.md)（[原文](https://x.com/xzdejz/status/2047924864418501111)）
