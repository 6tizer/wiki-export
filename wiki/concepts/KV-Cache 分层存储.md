---
title: KV-Cache 分层存储
type: concept
tags:
- 推理优化
- 模型部署
- AI 设计
status: 审核中
confidence: medium
last_compiled: '2026-04-20'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/0cd5da67324743cb89e557eb4327f775
notion_id: 0cd5da67-3247-43cb-89e5-57eb4327f775
---

## 定义

KV-Cache 分层存储是指把大模型推理过程中产生的 Key/Value 缓存按性能和成本分布到不同存储或节点层级中，以降低时延、提升资源利用率并控制推理成本。

## 关键要点

- 它是推理时代的重要系统优化手段，尤其影响长上下文和多轮交互场景。

- 当缓存不再与计算完全共置时，网络搬运效率会直接影响推理时延。

- 分层设计通常服务于更低成本和更高整体吞吐，而不是单点极致性能。

- 在文章语境中，它被视为“全栈为 Token 服务”的存储层证据。

## 来源引用

- [摘要：为了Token，阿里云竟然出了一个TPN？](summaries/摘要：为了Token，阿里云竟然出了一个TPN？.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzU1OTEwNDkwNw%3D%3D&mid=2247492725&idx=1&sn=05da9c55729b14a97d8fcbec7cadd3e2&chksm=fd6c11ebba90a0d90aec3ff46f46b00aea99a3b1e55e81bd81355a80b9e0f62dd360b6371d40#rd)）
