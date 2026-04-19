---
title: wiki-mempalace-bridge
type: entity
tags:
- 记忆系统
- 知识管理
status: 草稿
confidence: high
last_compiled: '2026-04-17'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/3a870c10fa174d07a8089b375c498b51
notion_id: 3a870c10-fa17-4d07-a808-9b375c498b51
---

## 定义

wiki-mempalace-bridge 是连接 llm-wiki 与 rust-mempalace 的桥接 crate，负责把知识写入事件同步到 MemPalace，并把检索与图谱能力反向接回 Wiki 引擎。

## 关键要点

- 提供写路径 sink，把 claim、source 与 supersede 关系同步到 MemPalace

- 提供读路径 ranker/search ports，把 FTS5 检索与图谱结果回灌给 Wiki 查询流程

- 通过 feature flag 控制 live 集成，关闭时两边仍可独立运行

- 是这次“两个系统焊死但仍保持模块边界”设计的关键中间层

## 来源引用

- 摘要：Rust-llm-wiki & Rust-mempalace合并，提供22 个 MCP 工具，Agent 终于有了"持久大脑"，持续的高质量上下文，这事靠谱了（[原文](https://mp.weixin.qq.com/s?__biz=MzkxNzY0OTA4Mg%3D%3D&mid=2247493215&idx=1&sn=7cc67138b3f4025466cb3a64a55c8109&chksm=c0ccfbe465f303ae41c71f66e977f5051c02fda3d0eb7a62327f390e017b04181fb0fcbff59e#rd)）

## 关联概念

- [llm-wiki](entities/llm-wiki.md)

- [MemPalace](entities/MemPalace.md)

- [MCP 协议](concepts/MCP 协议.md)

- [FTS5 全文检索](concepts/FTS5 全文检索.md)

- [时序知识图谱](concepts/时序知识图谱.md)

- [RRF 融合检索](concepts/RRF 融合检索.md)

- [wake-up 协议](concepts/wake-up 协议.md)
