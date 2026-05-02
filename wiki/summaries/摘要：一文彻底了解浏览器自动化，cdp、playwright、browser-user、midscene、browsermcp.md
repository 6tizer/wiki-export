---
title: 摘要：一文彻底了解浏览器自动化，cdp、playwright、browser-user、midscene、browsermcp
type: summary
tags:
- 浏览器自动化
- 内容自动化
status: 已审核
confidence: high
last_compiled: '2026-05-02'
source_tags: ''
source_article_url: https://www.notion.so/354701074b688154b4f9cf9e38f7861c
notion_url: https://www.notion.so/Tizer/96b144ae33464c558c6c727a6cc85a26
notion_id: 96b144ae-3346-4c55-8c6c-727a6cc85a26
---

## 一句话摘要

本文从底层到上层系统梳理了浏览器自动化技术栈：Chromium → CDP → cdp-use → Puppeteer/Playwright → browser-use → Midscene/BrowserMCP，帮助读者理解各层级工具的定位、适用场景和互补关系。

## 关键洞察

- **浏览器自动化是一条分层技术链**：最底层是 Chromium 浏览器底座，对外暴露 CDP 协议，之上依次是 Puppeteer/Playwright 工程化封装、browser-use 面向 AI Agent 的工作流封装，再到 Midscene 视觉路线和 BrowserMCP 当前上下文路线

- **browser-use 解决的是「AI 该怎么操作浏览器」的问题**：它不替代 Playwright，而是在其上包了一层适合 Agent 逐步调用的 CLI 工作流（open → state → click → input → screenshot）

- **Shadow DOM 是 DOM 自动化的硬伤**：视频号后台使用 wujie 的 Shadow DOM 结构，传统 DOM 选择器无法稳定抓取，需要 Midscene 这种视觉驱动方案来补位

- **Midscene 的代价明确**：更慢（多一层视觉理解）、有模型成本、稳定性依赖视觉理解而非精确选择器，适合作为复杂页面的补位方案而非通用替代

- **BrowserMCP 实现了「接管当前浏览器」的场景**：不需要重新拉起浏览器进程，直接基于用户当前浏览器上下文操作，但能力尚有限制

- **browser-use 的登录态复用机制**：通过克隆 Chrome profile 到临时目录，复用已有的 cookies 和登录态数据，解决了自动化中的身份问题

## 提取的概念

- [Chrome DevTools Protocol](concepts/Chrome DevTools Protocol.md)

- [Puppeteer](entities/Puppeteer.md)

- [Playwright Skill](concepts/Playwright Skill.md)

- [Browser Use](entities/Browser Use.md)

- [Midscene](entities/Midscene.md)

- [BrowserMCP](entities/BrowserMCP.md)

## 原始文章信息

- **作者**：周某人随笔

- **来源**：微信公众号

- **发布时间**：2026-04-14

- **原文链接**：[一文彻底了解浏览器自动化](https://mp.weixin.qq.com/s?__biz=MzU5ODg1NDk1Ng%3D%3D&mid=2247484662&idx=1&sn=86710f5235fc8287ed0fdf470145617d&chksm=ffb825b8a302ea2f0bb235145fc1d6b62eb3c0ad603642f1d2e993302656ef5c5996f49a76c5#rd)

## 个人评注

这篇文章对浏览器自动化技术栈的分层梳理非常清晰，与 Tizer 的内容自动化流水线直接相关。特别是 browser-use + Midscene 的组合方案——用 browser-use 处理标准页面的自动发布，遇到 Shadow DOM 等复杂结构时切换到 Midscene 视觉方案——这种分层策略可以直接应用到 OpenClaw 的多平台内容分发 Skill 中。BrowserMCP 的「接管当前浏览器」模式也值得关注，未来可能成为日常开发调试中 AI 辅助的标准入口。
