---
title: QueryWeaver
type: entity
tags:
- 知识管理
- AI 产品
- 代码生成
status: 审核中
confidence: medium
last_compiled: '2026-04-23'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/f915e9e560184239812ff82aab230e9b
notion_id: f915e9e5-6018-4239-812f-f82aab230e9b
---

## 定义

QueryWeaver 是一个面向 Text-to-SQL 场景的开源工具，核心思路是把数据库 schema 建模为图，而不是仅把表结构当作可向量检索的文本片段。

## 关键要点

- 将数据表视为节点、外键关系视为边。

- 在收到自然语言查询后，先沿结构链路查找完整 join path，再把所需表交给模型生成 SQL。

- 重点解决企业级复杂数据库中“语义相关表能找到，但中间桥接表找不到”的问题。

- 适合多跳连接、多表关联、结构复杂的数据库查询场景。

## 来源引用

- [摘要：QueryWeaver：用图遍历解决 Text-to-SQL 的 Bridge Table 缺失问题](summaries/摘要：QueryWeaver：用图遍历解决 Text-to-SQL 的 Bridge Table 缺失问题.md)
