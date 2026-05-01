---
title: mempal
type: entity
tags: []
status: 审核中
confidence: high
last_compiled: '2026-04-13'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/c4c3b4f372c24d538e96ee5bec4914a5
notion_id: c4c3b4f3-72c2-4d53-8e96-ee5bec4914a5
---

## 定义

mempal 是一个面向 Coding Agent 的项目记忆工具，是对 MemPalace 设计理念的 Rust 重写与工程化实现，强调本地优先、可验证检索、跨 Agent 协作和单二进制部署。

## 关键要点

- 采用 **BM25 + 向量检索 + RRF 融合** 的混合检索路径，兼顾精确命中与语义召回。

- 用 SQLite + sqlite-vec 作为本地存储基础，支持知识图谱、时间线和统计等能力。

- 通过 MCP 暴露 7 个工具，并把使用规则写进 `MEMORY_PROTOCOL`，降低 Agent 接入成本。

- 支持跨项目隧道、Agent 日记、多语言嵌入和审计式删除，更贴近实际开发协作场景。

## 来源引用

- [原文链接](https://x.com/blackanger/status/2043063705324392585)｜源文章：mempal：用 Rust 重铸 AI 记忆宫殿，Coding Agent 的项目记忆工具
