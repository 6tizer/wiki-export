---
title: 文档转 Markdown
type: concept
tags:
- 知识管理
status: 审核中
confidence: medium
last_compiled: '2026-04-13'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/deb2d5099aba4047978fa1f5841150eb
notion_id: deb2d509-9aba-4047-978f-a1f5841150eb
---

## 定义

**文档转 Markdown** 是一种文档预处理思路，即先把 PDF、Word、PPT、表格或网页等异构内容转换为结构较清晰的 Markdown，再交给 LLM、RAG 或知识库流程继续处理。

## 核心要点

- Markdown 兼具接近纯文本与保留结构两种特性，适合作为统一中间表示

- 这种转换能降低后续切分、检索、摘要与引用链路的清洗成本

- 转换后的效果取决于源文档质量，复杂表格、多栏版式、扫描件通常仍是难点

- 在知识库或内容流水线中，这一层常常决定后续自动化效果上限

## 关联概念

- [RAG](concepts/RAG.md)

## 来源引用

- [原文链接](https://x.com/AI_jacksaku/status/2042880330160316846)｜《加粗》｜来源条目：MarkItDown：微软开源的文件转 Markdown 神器，RAG 数据预处理的新标配
