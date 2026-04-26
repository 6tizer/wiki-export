---
title: WebSearch
type: concept
tags:
- RAG/检索
- 浏览器自动化
- AI 产品
status: 审核中
confidence: high
last_compiled: '2026-04-18'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/a09ae1fec9774a078efebaefe34495dd
notion_id: a09ae1fe-c977-4a07-8efe-baefe34495dd
---

## 定义

WebSearch 是 Claude / Anthropic 体系中的内置联网搜索工具，用于把搜索能力直接作为模型工具调用的一部分暴露给客户端。

## 关键要点

- 在 Claude Code 中，WebSearch 会以 tools 形式直接发送给后端模型服务

- Anthropic 的内置搜索工具不要求像自定义工具那样显式传入 `input_schema`

- 如果兼容层把它当成普通自定义工具解析，就可能触发 422 之类的 schema 错误

## 来源引用

- [摘要：各家Coding Plan为啥不兼容Claude WebSearch格式](summaries/摘要：各家Coding Plan为啥不兼容Claude WebSearch格式.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzkyOTY1NzMzNg%3D%3D&mid=2247489376&idx=1&sn=722c4f2ba5f82432e7abff79079f8bef&chksm=c3cb3b3b7b865b2b1cf89b3ea79ebe2a03d32fb1e8749f2f334e444c518356d58f2af2b2561f#rd)）

## 关联概念

- [Claude Code](entities/Claude Code.md)

- [Anthropic API](entities/Anthropic API.md)

- [WebFetch](concepts/WebFetch.md)

- [GLM-5.1](entities/GLM-5.1.md)

- [OpenClaw](entities/OpenClaw.md)
