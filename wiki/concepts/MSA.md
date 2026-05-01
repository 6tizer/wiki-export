---
title: MSA
type: concept
tags:
- 长期记忆
- 上下文管理
- 推理优化
status: 审核中
confidence: high
last_compiled: '2026-04-11'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/39a7ff952601468c9cb78f907ca95c84
notion_id: 39a7ff95-2601-468c-9cb7-8f907ca95c84
---

## 定义

MSA 是 EverMind AI 提出的长上下文记忆架构，全称 **Memory Sparse Attention**。它通过可学习的稀疏路由，让模型在超长上下文中只关注最相关的记忆块。

## 关键要点

- 目标是在不外挂 RAG 的情况下，把记忆能力内化进模型本身

- 强调端到端训练，而不是后处理式检索补丁

- 面向超长上下文、多跳推理和记忆扩展场景

## 来源引用

- 《MSA：让大模型原生「记住」一亿个 Token 的新架构》｜X书签｜原文链接：[https://x.com/elliotchen100/status/2034479369855590660](https://x.com/elliotchen100/status/2034479369855590660)｜来源条目：MSA：让大模型原生「记住」一亿个 Token 的新架构
