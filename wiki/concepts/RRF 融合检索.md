---
title: RRF 融合检索
type: concept
tags:
- 知识管理
- 记忆系统
status: 草稿
confidence: high
last_compiled: '2026-04-16'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/edf249abea904e438f2c333132ed10c7
notion_id: edf249ab-ea90-4e43-8f2c-333132ed10c7
---

## 定义

RRF 融合检索是一种把多路召回结果进行统一排序的检索融合方法。它不要求各路检索分数可直接比较，而是基于各自排序位置进行加权合并，适合将关键词检索、向量检索、图谱检索等异构通道组合为一个稳定的最终结果集。

## 核心要点

- **多路召回统一融合**：适合同时整合 BM25、向量检索、知识图谱游走等不同检索路径

- **排序优先于原始分数**：核心依据是各结果在各通道中的名次，而不是不同系统不可直接比较的原始分值

- **对知识系统友好**：当知识条目既有文本相似性，也有结构关系时，RRF 能减少单一路径带来的偏差

- **适合持续演进的 Wiki**：随着来源、概念与实体不断增加，RRF 可以作为编译式知识库中的统一检索层

## 关联概念

- [agentmemory](entities/agentmemory.md)

- [持久化跨会话记忆](concepts/持久化跨会话记忆.md)

- [GBrain](entities/GBrain.md)

- [pgvector](concepts/pgvector.md)

- [意图分类器](concepts/意图分类器.md)

- [Karpathy LLM Wiki 方法论](concepts/Karpathy LLM Wiki 方法论.md)

- [MemPalace](entities/MemPalace.md)

- [llm-wiki](entities/llm-wiki.md)

## 来源引用

- [摘要：local-first AI assistant built for personal AI sovereignty](summaries/摘要：local-first AI assistant built for personal AI sovereignty.md)（[原文](https://x.com/ghumare64/status/2045291112454402194)）

- [原文链接](https://mp.weixin.qq.com/s?__biz=MzkxNzY0OTA4Mg%3D%3D&mid=2247493206&idx=1&sn=7080809308368860641fd4df6601bef9&chksm=c0a8ea2ad24191e6e6e084a08eacab4b318f12dd484d75fe35bb554e96c6e9906e407e998911#rd)｜《Karpathy 提出了 LLM Wiki，我用 Rust 把它造出来了，还打通了 MemPalace 知识图谱》｜源文章：Karpathy 提出了 LLM Wiki，我用 Rust 把它造出来了，还打通了 MemPalace 知识图谱

- [原文链接](https://x.com/AlphaSignalAI/status/2044461541232148986)｜《How GBrain Works, and How to Actually Wire It Into Your Agents》｜来源条目：[摘要：How GBrain Works, and How to Actually Wire It Into Your Agents](summaries/摘要：How GBrain Works, and How to Actually Wire It Into Your Agents.md)
