---
title: wake-up 协议
type: concept
tags:
- MCP 协议
- 上下文管理
- 知识管理
- RAG/检索
status: 审核中
confidence: high
last_compiled: '2026-04-17'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/1a3e4b98a8f14648bae0218a73d5aa3a
notion_id: 1a3e4b98-a8f1-4648-bae0-218a73d5aa3a
---

## 定义

wake-up 协议是一类面向 Agent 启动阶段的上下文注入协议，用来在会话开始时按层级加载身份、关键事实、活跃语义知识与最近上下文。

## 关键要点

- 目标不是一次性塞入全部记忆，而是按层次唤醒最相关上下文

- 适合与记忆系统、知识图谱和检索系统联动，降低上下文噪声

- 在本文里，wake-up 协议既出现在 MemPalace 工具侧，也出现在统一 MCP Server 的对外能力里

- 它体现了“检索可得”向“启动即得”的体验升级

## 来源引用

- 摘要：Rust-llm-wiki & Rust-mempalace合并，提供22 个 MCP 工具，Agent 终于有了"持久大脑"，持续的高质量上下文，这事靠谱了（[原文](https://mp.weixin.qq.com/s?__biz=MzkxNzY0OTA4Mg%3D%3D&mid=2247493215&idx=1&sn=7cc67138b3f4025466cb3a64a55c8109&chksm=c0ccfbe465f303ae41c71f66e977f5051c02fda3d0eb7a62327f390e017b04181fb0fcbff59e#rd)）

## 关联概念

- [MemPalace](entities/MemPalace.md)

- [MCP 协议](concepts/MCP 协议.md)

- [llm-wiki](entities/llm-wiki.md)

- [MCP Server](concepts/MCP Server.md)

- [wiki-mempalace-bridge](entities/wiki-mempalace-bridge.md)
