---
title: LLM Graph Transformer
type: concept
tags:
- LLM
status: 草稿
confidence: high
last_compiled: '2026-04-11'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/6449d112806e4d3ca67bca93875e0919
notion_id: 6449d112-806e-4d3c-a67b-ca93875e0919
---

## 定义

LLM Graph Transformer 是 LangChain 实验性包（langchain-experimental）中的模块，能将非结构化文本自动抽取成「节点（实体）+ 关系（边）」的图结构，并存入图数据库（主要是 Neo4j）。用于构建知识图谱和 GraphRAG 应用。主要贡献者为 Tomaz Bratanic（Neo4j Graph ML & GenAI 研究员）。

**GitHub**：langchain-ai/langchain-experimental | License: MIT | 由 LangChain 官方维护

## 双模式运行

1. **工具调用模式（推荐）**：利用 Function Calling 直接输出格式化图数据，支持属性提取

1. **Prompt 模式（兼容）**：Few-shot 引导，适用不支持 Function Calling 的模型

## 典型用法

```python
from langchain_experimental.graph_transformers import LLMGraphTransformer

llm_transformer = LLMGraphTransformer(
    llm=ChatOpenAI(model="gpt-4o"),
    allowed_nodes=["Person", "Organization"],
    allowed_relationships=["WORKS_FOR"]
)
graph_documents = llm_transformer.convert_to_graph_documents(documents)
graph.add_graph_documents(graph_documents)
```

## 已知问题

- **实体去重问题**：同一实体因描述不同形成不同节点，需自行处理

- **模块路径变更**：版本升级后导入路径有变

## 与同类方案对比

- vs Microsoft GraphRAG：后者社区聚合+层级摘要，适合大规模语料

- vs LlamaIndex KG：与 LlamaIndex 索引深度集成

- vs Neo4j LLM Graph Builder：提供图形化 UI，适合非开发者

## 来源引用

- LLM Graph Transformer：用 LangChain 把非结构化文本变成知识图谱
