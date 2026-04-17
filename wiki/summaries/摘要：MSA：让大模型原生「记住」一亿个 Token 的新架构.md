---
title: 摘要：MSA：让大模型原生「记住」一亿个 Token 的新架构
type: summary
tags:
- LLM
- 记忆系统
status: 已审核
confidence: high
last_compiled: '2026-04-11'
source_tags: LLM, Agent
source_article_url: https://www.notion.so/335701074b68814ebfb8f27216bbfe45
notion_url: https://www.notion.so/57ab667874e1432d9087ec30ee8a0150
notion_id: 57ab6678-74e1-432d-9087-ec30ee8a0150
---

### 一句话摘要

MSA 试图把超长上下文记忆从外挂式检索升级为模型内部能力，用稀疏路由与分层推理把 1 亿 token 记忆窗口变成可训练、可推理的架构路线。

### 关键洞察

- MSA 的核心不是单纯扩窗，而是让模型自己学会“该看哪些记忆块”。

- Document-wise RoPE 解决了多文档长序列中的位置外推问题，是超长上下文成立的关键配件。

- Memory Parallel 把超长记忆的工程成本压到有限 GPU 可承受的范围内。

- Memory Interleaving 让跨文档多跳推理成为架构内能力，而不是额外拼装的检索流程。

### 提取的概念

- [MSA](concepts/MSA.md)

- [Document-wise RoPE](concepts/Document-wise RoPE.md)

- [Memory Parallel](concepts/Memory Parallel.md)

- [Memory Interleaving](concepts/Memory Interleaving.md)

### 原始文章信息

- 作者：@elliotchen100（艾略特）

- 来源：X书签

- 发布时间：2026-03-22

- 链接：[原文链接](https://x.com/elliotchen100/status/2034479369855590660)

### 个人评注

如果 Tizer 后续继续做知识 Wiki、Agent 记忆和内容编译管线，MSA 这类“原生记忆”路线值得持续跟踪。它代表未来记忆系统不一定只靠 RAG 拼接，而可能直接成为模型架构的一部分。
