---
title: wake-up 协议
type: concept
tags:
- 记忆系统
- Agent 编排
status: 草稿
confidence: high
last_compiled: '2026-04-19'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/b0df5a30311d45aebbe165ea6781a1c5
notion_id: b0df5a30-311d-45ae-bbe1-65ea6781a1c5
---

## 定义

wake-up 协议是一种给 Agent 在启动或恢复上下文时快速注入关键信息的唤醒机制，通常按层提供身份、事实、语义知识与近期上下文。

## 关键要点

- 它的目标不是完整还原全部历史，而是在最小 token 成本下恢复“现在最需要知道什么”。

- 在这篇文章里，wake-up 协议把 Wiki 的 L2/L3 语义上下文与 MemPalace 的 L0/L1 记忆结合起来。

- 这类协议非常适合多轮协作、长期任务和具备持久记忆的 Agent 系统。

- 它本质上是记忆系统对 Agent 使用场景的一层接口抽象。

## 关联概念

- [MemPalace](entities/MemPalace.md)

- [MCP Server](concepts/MCP Server.md)

- [llm-wiki](entities/llm-wiki.md)

## 来源引用

- 摘要：Rust-llm-wiki & Rust-mempalace合并，提供22 个 MCP 工具，Agent 终于有了"持久大脑"，持续的高质量上下文，这事靠谱了（[原文](https://mp.weixin.qq.com/s?__biz=MzkxNzY0OTA4Mg%3D%3D&mid=2247493215&idx=1&sn=7cc67138b3f4025466cb3a64a55c8109&chksm=c0ccfbe465f303ae41c71f66e977f5051c02fda3d0eb7a62327f390e017b04181fb0fcbff59e#rd)）
