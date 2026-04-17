---
title: FTS5 全文检索
type: concept
tags:
- 开发工具
- 知识管理
status: 草稿
confidence: high
last_compiled: '2026-04-17'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/8005b6c29d4641eaac1c8d9ce4099125
notion_id: 8005b6c2-9d46-41ea-ac1c-8d9ce4099125
---

## 定义

FTS5 全文检索是 SQLite 提供的全文检索能力，支持倒排索引、相关性排序与 snippet 提取，适合在本地知识库中实现低成本且高质量的 BM25 检索。

## 关键要点

- 相比 token 重叠式 stub 检索，FTS5 提供更接近正式信息检索系统的排序能力

- 可直接结合 SQLite 使用，适合本地优先的 Agent 记忆系统

- 在本文语境里，它是 llm-wiki 检索能力从 demo 走向可用底座的关键升级

- 常与 BM25、snippet、高亮、混合检索链路一起出现

## 来源引用

- [摘要：Rust-llm-wiki & Rust-mempalace合并，提供22 个 MCP 工具，Agent 终于有了"持久大脑"，持续的高质量上下文，这事靠谱了](summaries/摘要：Rust-llm-wiki & Rust-mempalace合并，提供22 个 MCP 工具，Agent 终于有了持久大脑，持续的高质量上下文，这事靠谱了.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzkxNzY0OTA4Mg%3D%3D&mid=2247493215&idx=1&sn=7cc67138b3f4025466cb3a64a55c8109&chksm=c0ccfbe465f303ae41c71f66e977f5051c02fda3d0eb7a62327f390e017b04181fb0fcbff59e#rd)）

## 关联概念

- [MemPalace](entities/MemPalace.md)

- [llm-wiki](entities/llm-wiki.md)

- [wiki-mempalace-bridge](entities/wiki-mempalace-bridge.md)

- [时序知识图谱](concepts/时序知识图谱.md)
