---
title: Scrapling
type: entity
tags:
- 浏览器自动化
- OpenClaw
status: 草稿
confidence: high
last_compiled: '2026-04-17'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/33ef30407be44ad49826a814dabb87c5
notion_id: 33ef3040-7be4-4ad4-9826-a814dabb87c5
---

**定义**：Scrapling 是一个专为现代反爬环境设计的 Python 爬虫框架，解决了传统爬虫的三大痛点：网站改版导致选择器失效、Cloudflare 等反爬机制、动态页面抓取困难。

**三层抓取模式**

- **Fetcher**：普通静态网页，类似 parsel/scrapy 语法

- **DynamicFetcher**：浏览器驱动，针对 JS 渲染的网站

- **StealthyFetcher**：反反爬抓取，伪装浏览器、模拟真实 TLS 指纹，可绕过部分 Cloudflare 防护

**核心创新：Adaptive Parsing（自适应解析）**

记录 DOM 元素特征，当网站改版后依据历史特征重新匹配元素，解决传统爬虫最大痛点——网站改版导致选择器全部失效。

```python
# 保存元素特征
products = page.css(".product", auto_save=True)
# 网站改版后自动重新匹配
products = page.css(".product", adaptive=True)
```

**与 OpenClaw 集成**

将 Scrapling 封装为 OpenClaw Skill 后，AI Agent 可自主抓取任意网页。理想组合：OpenClaw + Scrapling + RAG = 自动抓取 → 入库 → 向量化 → 知识问答

**来源引用**

- [摘要：OpenClaw 最强 Skill：让 AI 自动爬完整个互联网](summaries/摘要：OpenClaw 最强 Skill：让 AI 自动爬完整个互联网.md)
