---
title: Ingest 摄入流程
type: concept
tags:
- 知识管理
- 工作流
status: 审核中
confidence: high
last_compiled: '2026-04-25'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/628fef81a1b247de9d91340fc81b0e35
notion_id: 628fef81-a1b2-47de-9d91-340fc81b0e35
---

## 定义

Ingest 摄入流程是 LLM Wiki 工作流中的入口操作：当新资料进入 raw 层后，LLM 读取内容、抽取关键事实、生成摘要，并把增量信息写回相关概念页、实体页和索引页。

## 关键要点

- 摄入不是简单存档，而是触发多页面的增量更新

- 一份资料可能同时更新摘要、概念、实体、综述与索引

- 摄入阶段要处理新增信息、冲突信息和交叉引用

- 它决定了知识库是否能持续增长，而不是只堆积原文

## 来源引用

- [原文链接](https://x.com/sitinme/status/2043865262982869105)｜《别再用 RAG 了，让 AI 帮你养一个会长大的知识库！》｜源文章：Karpathy 的 LLM Wiki：用 AI 养一个会自我生长的知识库

- 《Claude + Obsidian | How to use your second brain》｜X书签文章｜原文链接：[https://x.com/defileo/status/2043762213597397179](https://x.com/defileo/status/2043762213597397179)｜来源条目：[摘要：Claude + Obsidian | How to use your second brain](summaries/摘要：Claude + Obsidian  How to use your second brain.md)

- [摘要：3K Star！基于 Andrej Karpathy 提出的 LLM Wiki 方法论打造的 AI 知识库应用！](summaries/摘要：3K Star！基于 Andrej Karpathy 提出的 LLM Wiki 方法论打造的 AI 知识库应用！.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzkwMjQ0NzI0OQ%3D%3D&mid=2247505963&idx=1&sn=b590481b7f9c1dd86ea25cf168a2d7a4&chksm=c117c2239e6f0d9f4bcb402b081126525c06d59d365925b3d4a00f67978b1b98416d0fadb10a#rd)）

## 关联概念

- [Karpathy LLM Wiki 方法论](concepts/Karpathy LLM Wiki 方法论.md)

- [三层知识架构](concepts/三层知识架构.md)

- [Wiki 健康检查](concepts/Wiki 健康检查.md)

- [llm-wiki](entities/llm-wiki.md)

- [Idea File](concepts/Idea File.md)

- [claude-obsidian](entities/claude-obsidian.md)

- [SHA256 增量缓存](concepts/SHA256 增量缓存.md)
