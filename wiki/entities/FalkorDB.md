---
title: FalkorDB
type: entity
tags:
- 开发工具
- 知识管理
status: 审核中
confidence: high
last_compiled: '2026-04-23'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/3a06b823f7534fa8a5e6b4703c19b874
notion_id: 3a06b823-f753-4fa8-a5e6-b4703c19b874
---

## 定义

FalkorDB 是一个面向复杂关系查询与 GraphRAG 场景的开源图数据库产品，主打用稀疏矩阵表示图连接，并以线性代数方式执行多跳图查询。

## 关键要点

- 它把图数据库定位为 Wiki 之上的“关系层”，用于回答跨实体、跨时间、多跳连接的问题。

- 官方强调其底层基于稀疏邻接矩阵与 GraphBLAS 思路，以提升深层遍历性能。

- 它同时提供向量搜索能力，试图把图查询与语义检索合并进同一系统。

- 运行方式偏工程化：可通过 Docker 部署，并可用 Cypher 及多语言客户端接入。

## 来源引用

- [摘要：queryable Property Graph database to leverage sparse matrices](summaries/摘要：queryable Property Graph database to leverage sparse matrices.md)（[原文](https://x.com/akshay_pachaar/status/2047220248081015110)）

## 关联概念

- [Karpathy LLM Wiki 方法论](concepts/Karpathy LLM Wiki 方法论.md)

- [GraphRAG](concepts/GraphRAG.md)

- [Property Graph](concepts/Property Graph.md)

- [稀疏矩阵图表示](concepts/稀疏矩阵图表示.md)
