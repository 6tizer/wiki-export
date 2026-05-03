---
title: Holographic Memory
type: concept
tags:
- 长期记忆
status: 草稿
confidence: medium
last_compiled: '2026-05-03'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/3a2bf1c775514eb3b08953b4606ebe72
notion_id: 3a2bf1c7-7551-4eb3-b089-53b4606ebe72
---

## 定义

Holographic Memory 是 Orb 框架中实现的一种本地持久化记忆架构，基于 SQLite 存储，提供事实提取（fact extraction）、信任评分（trust scoring）、衰减控制（decay controls）和写入时仲裁（write-time arbitration）能力。

别名：holographic long-term memory

## 关键要点

- 每个 Agent profile 拥有独立的 `memory.db`，存储在 `profiles/{name}/data/` 目录下

- 支持跨线程的事实召回（cross-thread factual recall），与 Claude Code 自带的 auto-memory 形成分层互补

- 包含矛盾处理（contradiction handling）和记忆卫生任务（memory hygiene jobs），确保事实库一致性

- 信任评分机制对提取的事实进行加权，影响后续召回优先级

- Python 桥接层（`lib/holographic/`）负责记忆的维护和检索操作

## 与 Claude Code Auto-memory 的区别

- Holographic Memory：Orb 层面拥有，跨线程事实召回和文档查找

- Claude Code Auto-memory：CLI 原生持久记忆，按 workspace `cwd` 路径键值存储

## 来源引用

- [摘要：Orb 自建记忆与路由的 Claude Code 封装框架](summaries/摘要：Orb 自建记忆与路由的 Claude Code 封装框架.md)（[原文](https://x.com/karry_viber/status/2050483217858482374)）

## 关联概念

- [Orb](entities/Orb.md)

- [Multi-profile Agent 隔离](concepts/Multi-profile Agent 隔离.md)

- [Claude Code](entities/Claude Code.md)

- [持久化跨会话记忆](concepts/持久化跨会话记忆.md)
