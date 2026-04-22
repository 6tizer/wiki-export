---
title: RAG
type: concept
tags:
- RAG/检索
status: 已审核
confidence: medium
last_compiled: '2026-04-22'
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

- [摘要：RAG真被“替换”了？Mintlify造出ChromaFs假文件系统：冷启动46秒砍到100ms！](summaries/摘要：RAG真被“替换”了？Mintlify造出ChromaFs假文件系统：冷启动46秒砍到100ms！.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzkyODY4MjMxNw%3D%3D&mid=2247486957&idx=1&sn=a138c5f63d7a073cb6a379cd5b4f4228&chksm=c3d4c35bbb262a84c381bbe93326cfa84b8bdac9410335dacfe4aec68823c600edf420e857e6#rd)）——强调 RAG 的检索接口不应被窄化为向量 Top-K，而应允许目录遍历、grep 与文件级探索

- [摘要：Karpathy LLM Wiki 个人知识库方法论](summaries/摘要：Karpathy LLM Wiki 个人知识库方法论.md)（来源：微信 / Alphana和大船的AI工作区）——讨论 RAG 的适用边界，提出小规模场景下的替代方案

- [原文链接](https://x.com/AYi_AInotes/status/2043033290014147063)｜[摘要：LangChain创始人Harrison Chase这篇，直接点透了现在所有AI Agent的核心问题。](summaries/摘要：LangChain创始人Harrison Chase这篇，直接点透了现在所有AI Agent的核心问题。.md)

- [摘要：加粗](summaries/摘要：加粗.md)（[原文](https://x.com/AI_jacksaku/status/2042880330160316846)，来源条目）

- [摘要：Here are the 3 Core Pillars of Every AI Agent's Context](summaries/摘要：Here are the 3 Core Pillars of Every AI Agent's Context.md)（[原文](https://x.com/Ai_Vaidehi/status/2045050337149513974)）

- [摘要：用好NotebookLM立省80%Token](summaries/摘要：用好NotebookLM立省80%Token.md)（[原文](https://x.com/MinLiBuilds/status/2046002143937941988)）

## 关联概念

- [MCP 协议](concepts/MCP 协议.md)

- [Agent Skills](concepts/Agent Skills.md)

- [Mintlify](entities/Mintlify.md)

- [ChromaFs](concepts/ChromaFs.md)

- [just-bash](entities/just-bash.md)

- [ChromaDB](entities/ChromaDB.md)

- [NotebookLM](entities/NotebookLM.md)

- [Claude Code](entities/Claude Code.md)

- [Prompt Cache](concepts/Prompt Cache.md)

- [notebooklm-client](entities/notebooklm-client.md)
