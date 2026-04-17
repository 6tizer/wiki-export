---
title: Claim 断言模型
type: concept
tags:
- 知识管理
- 记忆系统
status: 草稿
confidence: high
last_compiled: '2026-04-16'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/fbb8e4be0a924515bfce5d524936f394
notion_id: fbb8e4be-0a92-4515-bfce-5d524936f394
---

## 定义

Claim 断言模型是一种把知识条目表示为结构化断言的建模方式。它不把知识仅仅视为静态文本，而是为每条知识附加层级、置信度、质量分、取代关系与过时状态，从而支持知识演化、追溯与治理。

## 核心要点

- **知识对象化**：每条知识都可被独立记录、检索、更新与替换

- **支持生命周期管理**：可通过 `supersedes` 与 `stale` 表达知识的取代与过时关系

- **适合长期记忆系统**：可与工作记忆、情节记忆、语义记忆、程序性记忆等层级配合使用

- **优于纯文本堆积**：相比只维护 Markdown 页面，断言模型更适合做审计、检索加权与结构化演进

## 关联概念

- [记忆分层架构](concepts/记忆分层架构.md)

- [Karpathy LLM Wiki 方法论](concepts/Karpathy LLM Wiki 方法论.md)

- [llm-wiki](entities/llm-wiki.md)

- [RRF 融合检索](concepts/RRF 融合检索.md)

## 来源引用

- [原文链接](https://mp.weixin.qq.com/s?__biz=MzkxNzY0OTA4Mg%3D%3D&mid=2247493206&idx=1&sn=7080809308368860641fd4df6601bef9&chksm=c0a8ea2ad24191e6e6e084a08eacab4b318f12dd484d75fe35bb554e96c6e9906e407e998911#rd)｜《Karpathy 提出了 LLM Wiki，我用 Rust 把它造出来了，还打通了 MemPalace 知识图谱》｜源文章：Karpathy 提出了 LLM Wiki，我用 Rust 把它造出来了，还打通了 MemPalace 知识图谱
