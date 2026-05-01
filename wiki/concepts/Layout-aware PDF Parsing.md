---
title: Layout-aware PDF Parsing
type: concept
tags:
- 知识管理
- RAG/检索
- Agent 协作模式
status: 审核中
confidence: high
last_compiled: '2026-04-23'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/8191ab70b3f240bd81c7fd5ea7f32ab9
notion_id: 8191ab70-b3f2-40bd-81c7-fd5ea7f32ab9
---

## 定义

Layout-aware PDF Parsing 是一种在解析 PDF 时显式保留页面空间布局、列结构、表格对齐关系和视觉分区的处理思路。

## 关键要点

- 与纯文本提取不同，它重视内容在页面中的相对位置。

- 对多栏文档、财报表格、复杂排版材料尤其重要。

- 这类能力通常是下游检索、抽取和 Agent 理解文档结构的基础层。

- LiteParse 用网格投影方法实现了这一路线的轻量化版本。

## 来源引用

- [摘要：fast and light](summaries/摘要：fast and light.md)（[原文](https://x.com/jerryjliu0/status/2047041129326194882)）
