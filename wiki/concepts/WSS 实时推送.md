---
title: WSS 实时推送
type: concept
tags:
- 开发工具
- 工作流
status: 审核中
confidence: medium
last_compiled: '2026-04-11'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/f3cc5b9243b44d8b91073b33b3f3141d
notion_id: f3cc5b92-43b4-4d8b-9107-3b33b3f3141d
---

## 定义

WSS 实时推送指基于 WebSocket Secure 的服务端主动消息推送机制，用来替代定时轮询获取新数据。

## 关键要点

- 新事件出现时由服务端主动推送，显著降低轮询带来的延迟与 token 成本

- 特别适合需要低时延响应的新闻流、行情流与事件触发场景

- 在 Agent 系统里，它常被用来把“被动提问”改成“主动订阅”

## 来源引用

- [原文链接](https://x.com/cryptoxiao/status/2031321597513228389)｜《6551 OpenClaw MCP V2：用 WSS 实时推送取代轮询，加密情报订阅最低 1.9U》｜来源条目：6551 OpenClaw MCP V2：用 WSS 实时推送取代轮询，加密情报订阅最低 1.9U
