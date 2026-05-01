---
title: 摘要：上手实测小红书评论爬取分析｜开源项目MediaCrawler+NotebookLM洞察选品机会
type: summary
tags:
- 社交媒体
- 浏览器自动化
- 内容自动化
status: 已审核
confidence: high
last_compiled: '2026-04-15'
source_tags: ''
source_article_url: https://www.notion.so/343701074b6881d091f1e72b3da9f948
notion_url: https://www.notion.so/Tizer/8534452a28244bc999489e06f3580037
notion_id: 8534452a-2824-4bc9-9948-9e06f3580037
---

### 一句话摘要

这篇文章展示了如何用 MediaCrawler 抓取小红书评论，再用 NotebookLM 总结痛点与机会，把评论数据转成可执行的选品洞察流程。

### 关键洞察

- MediaCrawler 负责从小红书抓取帖子与评论，为后续分析提供原始数据。

- NotebookLM 可以把评论数据快速转成摘要、问答、PPT、信息图等洞察输出。

- 以“苏式绿豆汤”为例，评论暴露出豆子不够熟、配料品质一般、卫生问题等真实痛点。

- 这套流程的核心价值，不是单纯爬数据，而是把用户反馈转成选品和改进方向。

- 当数据需求放大时，需要结合代理池与 CDP 模式控制风控与封禁风险。

### 提取的概念

- [MediaCrawler](entities/MediaCrawler.md)

- [NotebookLM](entities/NotebookLM.md)

- [MCP 协议](concepts/MCP 协议.md)

- [CDP 直连](concepts/CDP 直连.md)

- [代理池](concepts/代理池.md)

- [评论驱动选品](concepts/评论驱动选品.md)

### 原始文章信息

- 作者：AI Startups

- 来源：微信

- 发布时间：2026-04-15 23:33

- 原文链接：[查看原文](https://mp.weixin.qq.com/s?__biz=MzE5ODAwODU4Mw%3D%3D&mid=2247488491&idx=1&sn=d8956b196055794081700b920e951cbd&chksm=9794196c6e4419b94a1e1d6ba4dbf929b9b30dd49537839c1c3180ef6219f4455d55bf79eeae#rd)

- 源页面：上手实测小红书评论爬取分析｜开源项目MediaCrawler+NotebookLM洞察选品机会

### 个人评注

这类“采集 → 总结 → 洞察”的链路很适合 Tizer 的内容 pipeline。前端先抓取真实用户反馈，中间层用 LLM 做归纳与表达，后端再把稳定概念沉淀进 Wiki，形成可复用的选题、方法与工具资产。
