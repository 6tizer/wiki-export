---
title: RAG
type: concept
tags:
- LLM
- 记忆系统
status: 审核中
confidence: medium
last_compiled: '2026-04-18'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/263d46a08f2e4695aa041c9ccdd5cf01
notion_id: 263d46a0-8f2e-4695-aa04-1c9ccdd5cf01
---

## 定义

**RAG（Retrieval-Augmented Generation，检索增强生成）** 是一种将信息检索与大语言模型生成相结合的技术范式。在回答问题或生成内容时，先从外部知识库中检索相关文档片段，再将其作为上下文提供给 LLM 进行生成，从而提高回答的准确性和时效性。

## 核心要点

- 通常依赖向量数据库存储文档嵌入，通过语义相似度进行检索

- 解决 LLM 知识截止日期和幻觉问题

- 适用于大规模知识库场景（通常 1000+ 篇文档）

- Karpathy 指出：小规模知识库（1000 篇以下）不需要 RAG，维护好 [index.md](http://index.md/) 索引文件即可

- 替代方案包括：全文索引 + LLM 钻取、结构化 Wiki + 索引导航

## 来源引用

- [摘要：Karpathy LLM Wiki 个人知识库方法论](summaries/摘要：Karpathy LLM Wiki 个人知识库方法论.md)（来源：微信 / Alphana和大船的AI工作区）——讨论 RAG 的适用边界，提出小规模场景下的替代方案

- [原文链接](https://x.com/AYi_AInotes/status/2043033290014147063)｜[摘要：LangChain创始人Harrison Chase这篇，直接点透了现在所有AI Agent的核心问题。](summaries/摘要：LangChain创始人Harrison Chase这篇，直接点透了现在所有AI Agent的核心问题。.md)

- [摘要：加粗](summaries/摘要：加粗.md)（[原文](https://x.com/AI_jacksaku/status/2042880330160316846)，来源条目）
