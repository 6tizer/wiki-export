---
title: 摘要：QueryWeaver：用图遍历解决 Text-to-SQL 的 Bridge Table 缺失问题
type: summary
tags:
- 开发工具
- LLM
status: 已审核
confidence: medium
last_compiled: '2026-04-23'
source_tags: LLM, Agent, 开源, GitHub
source_article_url: https://www.notion.so/34b701074b688155861dc1a631df677f
notion_url: https://www.notion.so/4f1dc9e34b37492da2c1fccd9fcc6f0d
notion_id: 4f1dc9e3-4b37-492d-a2c1-fccd9fcc6f0d
---

## 一句话摘要

这条推文的核心观点是：企业级 Text-to-SQL 失败的根源常常不在模型或提示词，而在于 schema retrieval 无法找全连接查询所需的桥接表；QueryWeaver 通过把数据库 schema 表示为图并沿 join path 做结构遍历来解决这个问题。

## 关键洞察

- 向量检索擅长找语义相近的表，但容易漏掉语义不相近、却在结构上必不可少的桥接表。

- 在复杂企业数据库里，SQL 即使语法正确，也可能因为缺少中间连接链路而返回 0 行结果。

- 将表视为节点、外键视为边后，可以按结构发现 join path，把多跳链路上的表一并召回。

- QueryWeaver 的价值不在于“更会写 SQL”，而在于先把查询上下文里的 schema 取全。

- 该案例说明 Text-to-SQL 的关键瓶颈之一是检索/建模数据库结构，而不是单纯调 prompt。

## 提取的概念

- [QueryWeaver](entities/QueryWeaver.md)

- [Schema Retrieval](concepts/Schema Retrieval.md)

- [Text-to-SQL](concepts/Text-to-SQL.md)

- [Join Path Discovery](concepts/Join Path Discovery.md)

## 原始文章信息

- 作者：@_avichawla

- 来源：X书签

- 发布时间：2026-04-22

- 原文链接：[https://x.com/_avichawla/status/2046853138871885947](https://x.com/_avichawla/status/2046853138871885947)

- 源文章页面：QueryWeaver：用图遍历解决 Text-to-SQL 的 Bridge Table 缺失问题

## 个人评注

如果后续要给 Tizer 的内容库、运营库或知识 Wiki 做自然语言查询层，这条思路很有参考价值：仅靠语义召回容易漏掉真正决定结果是否可连通的中间表或中间实体；先把结构链路补齐，再交给模型生成 SQL 或查询计划，会比一味堆 prompt 更稳。
