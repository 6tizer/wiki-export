---
title: WebFetch
type: concept
tags:
- Agent 技能
- Coding Agent
status: 审核中
confidence: medium
last_compiled: '2026-04-18'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/47ab7af8f8d04abe93fb5257c9f0a7d7
notion_id: 47ab7af8-f8d0-4abe-93fb-5257c9f0a7d7
---

## 定义

WebFetch 是 Claude Code 中面向网页内容获取的工具，职责是先拿到目标网页内容，再把结果交给模型理解与后续处理。

## 关键要点

- 它与 WebSearch 不同：前者偏网页抓取，后者偏联网搜索

- 文章案例中本地 Fetch 已拿到网页内容，但后端 Coding Plan 仍返回 403

- 这说明问题未必出在抓取动作本身，而可能出在模型服务是否支持对应调用链

## 来源引用

- [摘要：各家Coding Plan为啥不兼容Claude WebSearch格式](summaries/摘要：各家Coding Plan为啥不兼容Claude WebSearch格式.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzkyOTY1NzMzNg%3D%3D&mid=2247489376&idx=1&sn=722c4f2ba5f82432e7abff79079f8bef&chksm=c3cb3b3b7b865b2b1cf89b3ea79ebe2a03d32fb1e8749f2f334e444c518356d58f2af2b2561f#rd)）

- [摘要：OpenClaw 烧 Token 的真相：最贵的不是写代码，而是 web fetch](summaries/摘要：OpenClaw 烧 Token 的真相：最贵的不是写代码，而是 web fetch.md)

## 关联概念

- [Claude Code](entities/Claude Code.md)

- [Anthropic API](entities/Anthropic API.md)

- [WebSearch](concepts/WebSearch.md)

- [GLM-5.1](entities/GLM-5.1.md)

- [OpenClaw](entities/OpenClaw.md)
