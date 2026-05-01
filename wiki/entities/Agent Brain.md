---
title: Agent Brain
type: entity
tags:
- RAG/检索
- 长期记忆
status: 草稿
confidence: medium
last_compiled: '2026-04-27'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/3e5ec2c78a6348e0b528935fc4cefb85
notion_id: 3e5ec2c7-8a63-48e0-b528-935fc4cefb85
---

## 定义

Agent Brain 是一个基于 Neo4j 的混合 GraphRAG 联想记忆系统，为 AI Agent 提供类大脑的主动回忆能力。项目开源于 [SirJipeto/agent-brain](https://github.com/SirJipeto/agent-brain)，MIT 许可。

## 关键要点

- **混合检索**：结合向量搜索（语义相似度）、图遍历（多跳推理）、激活扩散（从种子概念涟漪式回忆）

- **主动记忆**：每条消息触发后台检索，相关记忆自动排队注入上下文

- **记忆固化**：自动将旧对话记忆按主题聚类、压缩为摘要节点并归档

- **关系衰减**：定期削弱陈旧连接，修剪权重低于阈值的关系

- **零 LLM 实体提取**：使用 spaCy NER 自动分类实体

- 支持多种嵌入后端：sentence-transformers（本地）、OpenAI、Ollama

- 框架无关：可与 Agent Zero、LangChain、Claude Code 等集成

- 提供便捷函数（observe/get_context/respond）和 BrainAgent 封装

## 技术架构

```javascript
Agent → Observer Framework → [Consolidator + Neo4j Graph + Decay Engine]
```

- Observer 层：实体提取、图遍历（depth=3）、相关性评估（6 因子评分）、冷却/去重

- Neo4j 存储节点：Memory、Entity、Fact、Concept + Vector

- 支持 FastAPI REST API 和 LangChain Tool 集成

## 来源引用

- [摘要：hybrid GraphRAG memory system](summaries/摘要：hybrid GraphRAG memory system.md)（[原文](https://x.com/garrytan/status/2048503081911128119)）
