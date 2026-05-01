---
title: Dokobot
type: entity
tags:
- 浏览器自动化
- MCP 协议
- CLI 工具
status: 审核中
confidence: medium
last_compiled: '2026-04-17'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/a0a0f7642645446b9539bd71169b5b49
notion_id: a0a0f764-2645-446b-9539-bd71169b5b49
---

## 定义

Dokobot 是一款通过 Chrome 扩展或 CLI 接管本地 Chrome 的浏览器自动化工具，能够让 OpenClaw、ClaudeCode 等支持 MCP 或 Skills 的 Agent 直接复用用户本地登录态，执行网页访问、数据抓取和页面交互。

## 关键要点

- **本地浏览器接管**：不依赖单独对接站点 API，而是借用用户正在使用的 Chrome 环境完成访问与操作

- **能力覆盖完整**：支持页面导航、DOM/HTML/文本提取、点击输入、表单提交、滚动、截图与录制

- **双接入形态**：Chrome 扩展偏只读与安全优先，CLI 版本提供更完整的浏览器控制能力

- **典型场景**：适合公众号、飞书文档、小红书、知乎、CSDN 等需要真实浏览器上下文的网站采集与轻量自动化

- **安全边界**：核心卖点是登录态、Cookie 和权限留在本地，但密钥分发与高权限网页操作仍需要人工审慎授权

## 来源引用

- [原文链接](https://mp.weixin.qq.com/s/2k5S5UlZKqACLr8g1Mb2eQ)｜源文章：真香！这可能是openclaw抓取任何网页的终极解决方案了

## 关联概念

- [OpenClaw](entities/OpenClaw.md)

- [MCP 协议](concepts/MCP 协议.md)

- [浏览器登录态复用](concepts/浏览器登录态复用.md)
