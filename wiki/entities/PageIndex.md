---
title: PageIndex
type: entity
tags:
- RAG/检索
- CLI 工具
status: 草稿
confidence: medium
last_compiled: '2026-04-30'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/815da826949f4b81aaf2192cf091b867
notion_id: 815da826-949f-4b81-aaf2-192cf091b867
---

## 定义

PageIndex 是 VectifyAI 开发的无向量（vectorless）长文档检索引擎，通过树状索引结构实现对长文档和复杂文档的精确检索，无需向量数据库。是 OpenKB 的底层检索技术。

## 关键要点

- 采用树状索引（Tree Indexing）替代传统向量检索，实现无向量数据库的长文档处理

- 支持原生多模态——不仅检索文本，还能理解图表、表格和图片

- 为 OpenKB 提供底层检索能力，支持推理式检索（Reasoning-based Retrieval）

- GitHub 仓库：VectifyAI/PageIndex

## 关联概念

- [OpenKB](entities/OpenKB.md)

- [Nowledge Mem](entities/Nowledge Mem.md)

## 来源引用

- [摘要：Nowledge Mem 0.8：LLM Wiki](summaries/摘要：Nowledge Mem 0.8：LLM Wiki.md)（[原文](https://x.com/wey_gu/status/2049720331850625229)）
