---
title: Personal Agent
type: entity
tags:
- Harness 工程
- CLI 工具
status: 草稿
confidence: medium
last_compiled: '2026-04-28'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/e6f753292441482995881f1e15dc6778
notion_id: e6f75329-2441-4829-9588-1f1e15dc6778
---

## 定义

Personal Agent（PA）是 X 用户 @trashpandaemoji（Trash Panda）基于 Pi 构建的个人 Agent Harness，专注于桌面端长时对话、多线程管理和远程执行等高级功能。

别名：PA

## 关键要点

- 基于 @badlogicgames 开发的 Pi 框架构建，桌面应用为主界面

- 核心功能包括：Reply with Selection（引用回复）、Suggested Context（上下文播种）、Summarize & New（会话压缩重启）、Fork（会话分叉）、Parallel Execution（并行线程）、SSH Remotes（远程执行环境）

- 强调不依赖 RAG/embedding，使用轻量级词法检索做上下文推荐

- Parallel 功能从当前会话 fork 出侧线程，独立运行后自动注入回主线程

- SSH Remotes 允许在远程机器上部署 Pi + PA 运行环境，实现跨机器 Agent 循环

## 来源引用

- [摘要：Personal Agent Features (Part 2)](summaries/摘要：Personal Agent Features (Part 2).md)（[X 原文](https://x.com/trashpandaemoji/status/2048387560339013912)）

## 关联概念

- [上下文播种](concepts/上下文播种.md)

- [会话分叉](concepts/会话分叉.md)

- [并行 Agent 线程](concepts/并行 Agent 线程.md)

- [Context Compaction](concepts/Context Compaction.md)

- [Agent Harness](concepts/Agent Harness.md)
