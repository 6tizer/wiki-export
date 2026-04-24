---
title: MarkItDown
type: entity
tags:
- 开发工具
- LLM
status: 审核中
confidence: high
last_compiled: '2026-04-13'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/c3da0bbab2ee444883822b50f46e8012
notion_id: c3da0bba-b2ee-4448-8382-2b50f46e8012
---

## 定义

**MarkItDown** 是微软开源的 Python 文档转换工具，核心用途是把 PDF、Word、PPT、Excel、图片、音频等异构输入统一转换为更适合 LLM 与 RAG 管道消费的 Markdown 文本。

## 核心要点

- 官方定位是 *给 LLM 与文本分析管道做预处理*，重点在保留标题、列表、表格、链接等结构，而不是追求人类阅读场景下的完美还原

- 仓库由微软维护，采用 MIT 许可，可免费使用与商用

- 支持命令行、Python 调用、可选依赖与插件扩展，适合作为文档清洗链路中的标准化入口

- 对扫描件、复杂版式、OCR 等场景并非天然完美，往往仍需插件或额外能力补足

## 关联概念

- [RAG](concepts/RAG.md)

- [文档转 Markdown](concepts/文档转 Markdown.md)

## 来源引用

- [原文链接](https://x.com/AI_jacksaku/status/2042880330160316846)｜《加粗》｜来源条目：MarkItDown：微软开源的文件转 Markdown 神器，RAG 数据预处理的新标配
