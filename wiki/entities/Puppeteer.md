---
title: Puppeteer
type: entity
tags:
- 浏览器自动化
status: 草稿
confidence: medium
last_compiled: '2026-05-02'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/da31e992562b4114a2307e021d7c3694
notion_id: da31e992-562b-4114-a230-7e021d7c3694
---

## 定义

Puppeteer 是 Google 开发的 Node.js 浏览器自动化库，提供对 Chromium 浏览器的高层 API 控制。它基于 Chrome DevTools Protocol (CDP) 构建，是最早流行的浏览器自动化框架之一，许多开发者通过它第一次接触浏览器自动化。

## 关键要点

- **Google 出品**：与 Chrome/Chromium 生态关系密切

- **基于 CDP**：底层通过 Chrome DevTools Protocol 控制浏览器

- **比 Playwright 更早**：是浏览器自动化领域的先驱框架

- **功能完备但不如 Playwright 系统**：等待机制、多上下文、多标签等能力相对 Playwright 不够完整

- **适合入门**：API 设计直观，适合初学者了解浏览器自动化

## 与 Playwright 的对比

- Puppeteer 和 Chrome/Chromium 绑定更紧密

- Playwright 在等待机制、多上下文、多标签支持上更系统化

- 新项目倾向选择 Playwright，但 Puppeteer 在 Chrome 生态中仍有大量使用

## 关联概念

- Chrome DevTools Protocol（底层协议）

- Playwright（同层竞品，更完整的自动化框架）

- browser-use（面向 AI Agent 的上层封装）

## 来源引用

- [摘要：一文彻底了解浏览器自动化，cdp、playwright、browser-user、midscene、browsermcp](summaries/摘要：一文彻底了解浏览器自动化，cdp、playwright、browser-user、midscene、browsermcp.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzU5ODg1NDk1Ng%3D%3D&mid=2247484662&idx=1&sn=86710f5235fc8287ed0fdf470145617d&chksm=ffb825b8a302ea2f0bb235145fc1d6b62eb3c0ad603642f1d2e993302656ef5c5996f49a76c5#rd)）
