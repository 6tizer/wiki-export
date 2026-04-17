---
title: OCR
type: concept
tags:
- 开发工具
- LLM
status: 草稿
confidence: medium
last_compiled: '2026-04-13'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/7a5a323e4cee41958a0cd0589bf560b8
notion_id: 7a5a323e-4cee-4195-8a0c-d0589bf560b8
---

## 定义

**OCR** 是 *Optical Character Recognition* 的缩写，指把扫描件、截图、照片等图像中的文字识别为可检索、可编辑文本的技术。

## 核心要点

- 在文档预处理链路里，OCR 常用于补足扫描版 PDF、图片文档和无文字层文件的可读性

- 许多文档转 Markdown 工具对原生文本型文档效果较好，但遇到扫描件时通常需要额外 OCR 能力配合

- OCR 质量会直接影响后续的切分、检索、摘要与知识提炼质量

- 对 RAG 而言，OCR 不是终点，而是让原始资料进入可计算状态的前置步骤

## 关联概念

- [RAG](concepts/RAG.md)

- [文档转 Markdown](concepts/文档转 Markdown.md)

- [MarkItDown](entities/MarkItDown.md)

## 来源引用

- [原文链接](https://x.com/AI_jacksaku/status/2042880330160316846)｜《加粗》｜来源条目：MarkItDown：微软开源的文件转 Markdown 神器，RAG 数据预处理的新标配
