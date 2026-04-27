---
title: pgvector
type: concept
tags:
- RAG/检索
status: 审核中
confidence: high
last_compiled: '2026-04-11'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/07396a4401cf4c839be29ffc004f0318
notion_id: 07396a44-01cf-4c83-9be2-9ffc004f0318
---

## 定义

pgvector 是 PostgreSQL 的开源向量扩展，支持在关系数据库中存储和检索向量嵌入（vector embeddings），从而在传统 SQL 能力基础上叠加语义相似度搜索。它是大规模 AI 应用记忆系统的重要基础设施组件。

## 核心能力

- **向量存储**：在 Postgres 表中直接存储高维嵌入向量（如 OpenAI text-embedding-3-large 输出的 1536 维向量）

- **HNSW 索引**：Hierarchical Navigable Small World 近似最近邻索引，支持大规模向量的高效余弦相似度搜索

- **与 pg_trgm 组合**：结合 PostgreSQL 的全文检索（tsvector / ts_rank）和模糊匹配，实现关键词 + 向量的混合检索

- **RRF 融合**：Reciprocal Rank Fusion，将向量检索结果与关键词检索结果融合排序，兼顾精确匹配和语义召回

## 关联概念

- [GBrain](entities/GBrain.md)

- [PGLite](entities/PGLite.md)

- [RRF 融合检索](concepts/RRF 融合检索.md)

- [意图分类器](concepts/意图分类器.md)

## 在 GBrain 中的应用

GBrain 在文件数量超过 1000 时引入 Postgres + pgvector 作为检索层：

- 每个 Markdown 页面被切块（chunk）后生成嵌入，存入 `content_chunks` 表

- 查询时同时走 `tsvector` 关键词索引和 HNSW 向量索引，用 RRF 分数融合

- Supabase Pro（$25/月，8GB）为推荐托管方案

## 来源引用

- [GBrain README](https://github.com/garrytan/gbrain) — Garry Tan 的生产级 Agent 记忆系统

- [原文链接](https://x.com/AlphaSignalAI/status/2044461541232148986)｜《How GBrain Works, and How to Actually Wire It Into Your Agents》｜来源条目：[摘要：How GBrain Works, and How to Actually Wire It Into Your Agents](summaries/摘要：How GBrain Works, and How to Actually Wire It Into Your Agents.md)
