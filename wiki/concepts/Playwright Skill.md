---
title: Playwright Skill
type: concept
tags:
- 浏览器自动化
status: 审核中
confidence: medium
last_compiled: '2026-04-18'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/9a0f362cf3a74b00b062347fc2ad4b18
notion_id: 9a0f362c-f3a7-4b00-b062-347fc2ad4b18
---

## 定义

Playwright Skill 是 OpenClaw 的一个浏览器自动化技能，通过集成 Playwright 库让 AI Agent 能够驱动真实浏览器执行点击、滚动、等待 JS 渲染等操作，用自然语言描述需求即可实时生成和调试爬虫脚本。

## 关键要点

- 解决传统 HTTP 请求无法抓取 SPA/动态网页的痛点（JS 异步加载数据不在初始 HTML 中）

- 用户用自然语言描述需求 → Agent 自动分析页面结构 → 实时生成 Playwright 脚本 → 自动调试迭代

- 支持多 Tab 切换、懒加载滚动、持久化 Chrome Profile 等高级操作

- 相比 n8n + Apify/Bright Data 方案，无需预写脚本、无需三方付费服务

- 不需要懂编程，只需要会说话

## 来源引用

- [摘要：OpenClaw + Playwright：几乎能爬任意网页了](summaries/摘要：OpenClaw + Playwright：几乎能爬任意网页了.md)（Alex AI自动化，2026-02-27）— 用 MWC 议程抓取为案例，对比 n8n 方案展示 Playwright Skill 的优势

- [摘要：Chrome DevTools MCP：让 AI 助手直接操控你正在用的浏览器](summaries/摘要：Chrome DevTools MCP：让 AI 助手直接操控你正在用的浏览器.md)（X书签，2026-03-16）— 作为"新开隔离实例"路线的典型对照方案
