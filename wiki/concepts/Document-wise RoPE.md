---
title: Document-wise RoPE
type: concept
tags:
- 上下文管理
- 长期记忆
status: 审核中
confidence: medium
last_compiled: '2026-04-11'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/0804f3d8e64340b682a2851c7a6d3c0c
notion_id: 0804f3d8-e643-40b6-82a2-851c7a6d3c0c
---

## 定义

Document-wise RoPE 是 MSA 中采用的位置编码策略，为每个文档单独重置位置计数，从而避免长序列外推时的位置错位问题。

## 关键要点

- 每个文档内部从位置 0 重新计数

- 更适合多文档记忆场景

- 让短上下文训练的模型外推到超长上下文成为可能

## 来源引用

- 《MSA：让大模型原生「记住」一亿个 Token 的新架构》｜X书签｜原文链接：[https://x.com/elliotchen100/status/2034479369855590660](https://x.com/elliotchen100/status/2034479369855590660)｜来源条目：MSA：让大模型原生「记住」一亿个 Token 的新架构

- [原文链接](https://x.com/bozhou_ai/status/2035033044831400166)｜《EverMind MSA：把「记忆」直接长进注意力机制，4B 小模型干翻 235B RAG》｜来源条目：[摘要：EverMind MSA：把「记忆」直接长进注意力机制，4B 小模型干翻 235B RAG](summaries/摘要：EverMind MSA：把「记忆」直接长进注意力机制，4B 小模型干翻 235B RAG.md)
