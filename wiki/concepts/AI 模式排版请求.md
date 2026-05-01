---
title: AI 模式排版请求
type: concept
tags: []
status: 审核中
confidence: medium
last_compiled: '2026-04-20'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/edd2150f668548f88fc37ad8ad64b77f
notion_id: edd2150f-6685-48f8-8fc3-7ad8ad64b77f
---

## 定义

AI 模式排版请求，是指工具先把 Markdown 文章结构解析成一份适合外部大模型继续处理的 request / prompt，而不是立即在本地生成最终 HTML。

## 关键要点

- 先生成结构化排版请求，再交给 Claude Code 等环境继续完成视觉排版

- 与直接 API 转换相比，它更强调样式灵活性与外部模型接力能力

- 适合品牌内容、重要文章或需要更强视觉风格控制的场景

- 本质上是一种“工具负责准备上下文，模型负责最后一段生成”的协作模式

## 使用场景

- 需要更丰富的公众号视觉样式

- 想在 Coding Agent 环境中继续自动化排版

- 希望把主题、prompt 与模型能力组合进同一条内容生产链路

## 关联概念

- [md2wechat](entities/md2wechat.md)

- [Markdown 转公众号工作流](concepts/Markdown 转公众号工作流.md)

## 来源引用

- [摘要：用 Markdown 写公众号文章，像发朋友圈一样简单](summaries/摘要：用 Markdown 写公众号文章，像发朋友圈一样简单.md)（[原文](https://x.com/seekjourney/status/2045056409457549784)）
