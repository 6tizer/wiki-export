---
title: Thought Signatures
type: concept
tags:
- LLM
- 记忆系统
status: 草稿
confidence: medium
last_compiled: '2026-04-15'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/117e32afaa164fa483111bc003a0ccea
notion_id: 117e32af-aa16-4fa4-8311-1bc003a0ccea
---

## 定义

Thought Signatures 是 Google 在长上下文推理场景中提出的一种机制，用于保留推理链中的关键节点，降低长 session 中出现 reasoning drift 的风险。

## 关键要点

- 它关注的不是简单保留全部上下文，而是保留对后续推理最关键的思考锚点

- 它适用于超长上下文下的一致性维护，而不是角色分工式的任务传递

- 它体现了长任务系统更需要**推理连续性机制**，而不是岗位化编排

## 关联概念

- [Context Engineering](concepts/Context Engineering.md)

- [Compaction](concepts/Compaction.md)

- [Orchestrator 模式](concepts/Orchestrator 模式.md)

## 来源引用

- [原文链接](https://x.com/sujingshen/status/2043898494818410731)｜源文章：三省六部幻觉：为什么「虚拟公司」式多 Agent 架构在工程上走不通
