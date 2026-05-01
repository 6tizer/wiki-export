---
title: Join Path Discovery
type: concept
tags:
- 知识管理
- 商业/生态
- 推理优化
status: 审核中
confidence: medium
last_compiled: '2026-04-23'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/0939c7eccd244710bf93d410b087001e
notion_id: 0939c7ec-cd24-4710-bf93-d410b087001e
---

## 定义

Join Path Discovery 指在多个数据表之间自动识别可连通查询路径的过程，目标是找到从起点表到目标表所需经过的中间表与连接关系。

## 关键要点

- 它关注的是数据库结构连通性，而不是表名之间的语义相似度。

- 在多跳查询中，系统需要把桥接表一并找出，才能构造出可执行且有结果的 SQL。

- 该能力特别适合 schema 规模大、外键链路长的企业数据库。

- 图遍历是一种常见实现方式，因为它天然适合表达节点、边与路径搜索。

## 来源引用

- [摘要：QueryWeaver：用图遍历解决 Text-to-SQL 的 Bridge Table 缺失问题](summaries/摘要：QueryWeaver：用图遍历解决 Text-to-SQL 的 Bridge Table 缺失问题.md)
