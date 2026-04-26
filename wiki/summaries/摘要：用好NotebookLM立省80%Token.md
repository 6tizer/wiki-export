---
title: 摘要：用好NotebookLM立省80%Token
type: summary
tags:
- 知识管理
- RAG/检索
- 笔记工具
status: 已审核
confidence: high
last_compiled: '2026-04-20'
source_tags: ''
source_article_url: https://www.notion.so/348701074b68816da58ad6832d7b9710
notion_url: https://www.notion.so/695da476a22045938fb6fdfdfcb0e3c5
notion_id: 695da476-a220-4593-8fb6-fdfdfcb0e3c5
---

## 一句话摘要

把重语料交给 NotebookLM 存储与检索，把 Claude Code 限定为推理、编排与执行层，可以显著降低高强度研究场景下的 Token 成本，同时减少在网页、终端与资料库之间反复切换的心智负担。

## 关键洞察

- 真正省 Token 的关键，不是单纯依赖 prompt cache，而是避免把大体量原始语料反复塞进 Claude 主会话。

- NotebookLM 更像来源受限、带引用的“老师”，适合做资料检索、问答与证据回溯；Claude Code 更像“助手”，适合写代码、跑脚本、整理结果与调度工作流。

- 这种分工本质上是用 RAG/检索式成本模型替代“整包塞上下文”的线性成本模型，尤其适合论文、招股书、知识库等高密度文本场景。

- 借助 notebooklm-client 这类第三方客户端与 skill，可以把 NotebookLM 接入命令行与 Agent 工作流，让检索结果直接流入后续执行链路。

- 这套方案的代价是响应变慢、依赖非官方客户端、并需要额外注意登录 session 与工具稳定性。

## 提取的概念

- [NotebookLM](entities/NotebookLM.md)

- [Claude Code](entities/Claude Code.md)

- [RAG](concepts/RAG.md)

- [Prompt Cache](concepts/Prompt Cache.md)

- [notebooklm-client](entities/notebooklm-client.md)

## 原始文章信息

- 作者：@MinLiBuilds

- 来源：X书签

- 发布时间：2026-04-19

- 原文链接：[https://x.com/MinLiBuilds/status/2046002143937941988](https://x.com/MinLiBuilds/status/2046002143937941988)

## 个人评注

- 对 Tizer 的启发是把“原始资料读取”和“结论编译”拆成两层：前者交给来源受限的资料工作台，后者交给执行型 Agent，这样更适合知识 Wiki、研究摘要与内容流水线的稳定扩展。
