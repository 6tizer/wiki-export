---
title: Parallel Search API
type: entity
tags:
- 知识管理
- RAG/检索
- Agent 协作模式
status: 审核中
confidence: medium
last_compiled: '2026-04-23'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/7e5775e3c6d3471e8d2fded7772eec55
notion_id: 7e5775e3-c6d3-471e-8d2f-ded7772eec55
---

## 定义

Parallel Search API 是 mimeo 在资料发现阶段调用的外部检索能力，用来跨多种意图桶收集候选来源，为后续蒸馏与聚类提供原始语料。

## 关键要点

- 在 mimeo 的流程里，它承担“先找全资料”的入口角色。

- 检索范围覆盖文章、访谈、播客、论文、书籍、演讲等多类来源。

- 它与后续的 LLM 蒸馏、聚类和引文校验串联，构成从发现到结构化生成的前半段流水线。

- 这类 Search API 体现了 Agent 工程里“先发现上下文，再生成行为文件”的两阶段模式。

## 来源引用

- [摘要：New from K-Dense: mimeo.](summaries/摘要：New from K-Dense- mimeo.md)（[原文](https://x.com/k_dense_ai/status/2047020939590992051)）

## 关联概念

- [mimeo](entities/mimeo.md)

- [OpenRouter](entities/OpenRouter.md)
