---
title: Schema Retrieval
type: concept
tags:
- 知识管理
- RAG/检索
- 上下文管理
status: 审核中
confidence: medium
last_compiled: '2026-04-23'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/66e19fb1dae644068dd3aedf77590711
notion_id: 66e19fb1-dae6-4406-8dd3-aedf77590711
---

## 定义

Schema Retrieval 指在 Text-to-SQL 或数据库问答流程中，从完整数据库 schema 中找出与当前问题相关的数据表、字段与关系结构的过程。

## 关键要点

- 这是自然语言到 SQL 生成之前的关键上下文构建步骤。

- 如果召回不完整，模型即使生成语法正确的 SQL，也可能查不到正确结果。

- 传统做法常依赖语义检索，但对桥接表、多跳关系和弱语义命名的结构并不稳定。

- 更可靠的做法通常需要结合数据库结构信息，而不只看文本相似度。

## 来源引用

- [摘要：QueryWeaver：用图遍历解决 Text-to-SQL 的 Bridge Table 缺失问题](summaries/摘要：QueryWeaver：用图遍历解决 Text-to-SQL 的 Bridge Table 缺失问题.md)
