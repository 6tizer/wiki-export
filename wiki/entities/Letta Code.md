---
title: Letta Code
type: entity
tags:
- Agent 框架
- 记忆系统
status: 草稿
confidence: high
last_compiled: '2026-04-14'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/1f910286e863430e997a4d506ca6c61f
notion_id: 1f910286-e863-430e-997a-4d506ca6c61f
---

## 定义

Letta Code 是 Letta 推出的 **memory-first agent harness**，把记忆、提示重写与上下文治理直接做进执行底座，而不是作为外接插件来补丁式叠加。

## 关键要点

- 它把 Agent 记忆投影到 Git 支撑的文件系统中，让长期状态具备可读写、可追踪和可并发维护的能力。

- 它支持后台记忆子 Agent 持续执行 prompt rewriting 和 active memory management。

- 它把上下文装载、状态持久化、压缩保留与工具执行放在同一 harness 内统一设计。

- 它代表了“记忆优先” coding agent / agent harness 的产品形态。

## 来源引用

- [原文链接](https://x.com/sarahwooders/status/2040121230473457921)｜《Why memory isn't a plugin (it's the harness)》｜源文章：记忆不是插件，它是 Harness 本身：Letta 对 Agent 架构的重新定义

## 关联概念

- [Agent Harness](concepts/Agent Harness.md)

- [Agentic Context Management](concepts/Agentic Context Management.md)

- [Context Compaction](concepts/Context Compaction.md)
