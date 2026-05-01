---
title: 摘要：All Platforms, One Memory
type: summary
tags:
- 长期记忆
- RAG/检索
- 链上协议
status: 已审核
confidence: high
last_compiled: '2026-04-16'
source_tags: ''
source_article_url: https://www.notion.so/344701074b6881c79b97c8aba9abdf11
notion_url: https://www.notion.so/Tizer/0dc95d8924ae4ec7bbe309a06cd6a75b
notion_id: 0dc95d89-24ae-4ec7-bbe3-09a06cd6a75b
---

## 一句话摘要

Cognee 认为 Agent 记忆系统不该只会持续摄取信息，还应根据真实检索流量动态强化高价值路径、衰减低价值连接，让记忆图谱随使用过程自我进化。

## 关键洞察

- 真正有用的长期记忆不仅要会“记住”，还要会“忘记”，否则旧节点和无用连接会不断堆积，拖慢检索并增加噪声。

- 是否值得保留一段记忆，不应只看是否被写入过，更应看它在真实任务中是否被持续调用、是否帮助产生了有效回答。

- Cognee 用 `memify()` 对图谱做 RL 启发式优化，根据检索流量强化有效边、衰减闲置边，并从重复使用模式里推断新的连接。

- 这种机制让 Agent 的记忆从“静态存储知识”转向“根据使用学习什么更重要”，更适合长期运行的支持、协作和知识型 Agent。

- 在工程实现上，Cognee 默认采用 SQLite + LanceDB + Kuzu 的嵌入式栈，并支持生产环境切换到 Postgres、Qdrant 或 Neo4j。

## 提取的概念

- [Cognee](entities/Cognee.md)

- [memify](concepts/memify.md)

- [智能遗忘](concepts/智能遗忘.md)

## 原始文章信息

- 作者：@akshay_pachaar

- 来源：X书签

- 发布时间：2026-04-16

- 链接：[原文推文](https://x.com/akshay_pachaar/status/2044699731277078785)

## 个人评注

这篇内容对 Tizer 的知识工作流有直接启发：如果后续要把 OpenClaw、内容流水线、HITL 反馈和历史操作沉淀成长期记忆，重点不只是“多存”，而是建立基于调用频率、结果质量和任务上下文的记忆衰减与重排机制。这样才能避免 Wiki、记忆层和工作流日志越来越重，却越来越难被高质量召回。
