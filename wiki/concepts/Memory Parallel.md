---
title: Memory Parallel
type: concept
tags:
- LLM
- 记忆系统
status: 审核中
confidence: medium
last_compiled: '2026-04-11'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/c5ef44efe03943029cb943dd203f10f1
notion_id: c5ef44ef-e039-4302-9cb9-43dd203f10f1
---

## 定义

Memory Parallel 是 MSA 的推理机制，通过把记忆检索相关状态分布到多张 GPU 上，实现超长上下文下的可扩展推理。

## 关键要点

- 将路由相关 Key 常驻显存，其余内容按需加载

- 支持多 GPU 分片与全局归约

- 目标是在有限硬件上承载超长记忆

## 来源引用

- 《MSA：让大模型原生「记住」一亿个 Token 的新架构》｜X书签｜原文链接：[https://x.com/elliotchen100/status/2034479369855590660](https://x.com/elliotchen100/status/2034479369855590660)｜来源条目：MSA：让大模型原生「记住」一亿个 Token 的新架构
