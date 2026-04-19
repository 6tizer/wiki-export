---
title: FTS5 全文检索
type: concept
tags:
- 记忆系统
status: 草稿
confidence: high
last_compiled: '2026-04-19'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/3eb08e5cd1a44ecc9c362f97edc1cc36
notion_id: 3eb08e5c-d1a4-4ecc-9c36-2f97edc1cc36
---

## 定义

FTS5 全文检索是 SQLite 的全文索引能力，能基于真实的倒排索引与 BM25 排序进行高质量文本召回，适合作为本地知识库与记忆系统的基础检索层。

## 关键要点

- 它比简单的 token 重叠匹配更接近真正的信息检索系统。

- 在这篇文章的架构里，FTS5 取代了 llm-wiki 里原本较弱的 stub 检索。

- 它被 MemPalace 用作统一搜索底座，再通过 bridge 反馈给 Wiki 检索链路。

- 当知识条目持续增长时，FTS5 仍能保持较好的本地检索效率与可解释性。

## 关联概念

- [MemPalace](entities/MemPalace.md)

- [llm-wiki](entities/llm-wiki.md)

- [RRF 融合检索](concepts/RRF 融合检索.md)

## 来源引用

- 摘要：Rust-llm-wiki & Rust-mempalace合并，提供22 个 MCP 工具，Agent 终于有了"持久大脑"，持续的高质量上下文，这事靠谱了（[原文](https://mp.weixin.qq.com/s?__biz=MzkxNzY0OTA4Mg%3D%3D&mid=2247493215&idx=1&sn=7cc67138b3f4025466cb3a64a55c8109&chksm=c0ccfbe465f303ae41c71f66e977f5051c02fda3d0eb7a62327f390e017b04181fb0fcbff59e#rd)）
