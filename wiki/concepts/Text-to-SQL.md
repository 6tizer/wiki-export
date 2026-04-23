---
title: Text-to-SQL
type: concept
tags:
- 开发工具
- LLM
status: 草稿
confidence: high
last_compiled: '2026-04-23'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/8d41606cf064429da24834ccb9f66797
notion_id: 8d41606c-f064-429d-a248-34ccb9f66797
---

## 定义

Text-to-SQL 是把自然语言问题转换为结构化 SQL 查询的技术范式，用于让用户用日常语言访问数据库。

## 关键要点

- 它通常依赖模型理解用户意图、数据库 schema 与字段语义。

- 实际效果不仅取决于模型能力，也强烈依赖 schema 召回、执行反馈与错误纠正机制。

- 在企业数据库中，复杂 join、桥接表与多跳关系往往是准确率下降的主要来源。

- 因此，Text-to-SQL 不只是“生成 SQL”，也是“构建正确查询上下文”的系统问题。

## 来源引用

- [摘要：QueryWeaver：用图遍历解决 Text-to-SQL 的 Bridge Table 缺失问题](summaries/摘要：QueryWeaver：用图遍历解决 Text-to-SQL 的 Bridge Table 缺失问题.md)
