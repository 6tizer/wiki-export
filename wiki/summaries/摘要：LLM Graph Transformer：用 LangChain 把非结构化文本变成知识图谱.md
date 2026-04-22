---
title: 摘要：LLM Graph Transformer：用 LangChain 把非结构化文本变成知识图谱
type: summary
tags:
- LLM
status: 已审核
confidence: high
last_compiled: '2026-04-11'
source_tags: LLM, Agent
source_article_url: ''
notion_url: https://www.notion.so/fff4efc7872f4313890ea288450cfbfa
notion_id: fff4efc7-872f-4313-890e-a288450cfbfa
---

## 一句话摘要

LLM Graph Transformer 将非结构化文本自动抽取成「节点 + 关系」的图结构并存入 Neo4j，是在已有 LangChain 项目中添加知识图谱增强 RAG 的最低摩擦选择。

## 关键洞察

- **双模式运行**：工具调用模式（推荐，支持属性提取）vs Prompt 模式（兼容不支持 Function Calling 的模型）

- **实体去重是最大痛点**：同一实体因描述不同成为不同节点，需开发者自行处理

- **Schema 约束至关重要**：通过 `allowed_nodes` 和 `allowed_relationships` 避免模型自由发挥

- **与 Microsoft GraphRAG 的差异**：LLM Graph Transformer 是轻量集成工具；GraphRAG 是企业级全流程方案

- **作者背景**：Tomaz Bratanic 是 Neo4j Graph ML 研究员，《Graph Algorithms for Data Science》作者

## 提取的概念

[LLM Graph Transformer](concepts/LLM Graph Transformer.md) · [LangChain](entities/LangChain.md)

## 原始文章信息

- **作者**：LangChain

- **来源**：X 书签

- **发布时间**：2025-01-13

- **链接**：[https://medium.com/towards-data-science/building-knowledge-graphs-with-llm-graph-transformer-a91045c49b59](https://medium.com/towards-data-science/building-knowledge-graphs-with-llm-graph-transformer-a91045c49b59)

## 个人评注

对于 Tizer 的知识管理工作流，如需将文章和概念间的关系都结构化存入图数据库，这个工具层值得关注。与当前的 Wiki 知识库构建通道很相近。
