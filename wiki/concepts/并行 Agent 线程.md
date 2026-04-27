---
title: 并行 Agent 线程
type: concept
tags:
- Harness 工程
- 多Agent协作
status: 草稿
confidence: medium
last_compiled: '2026-04-28'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/cfde6a681cf34e32847f91667758f0a6
notion_id: cfde6a68-1cf3-4e32-847f-91667758f0a6
---

## 定义

并行 Agent 线程（Parallel Agent Threads）是在 Agent Harness 中从主对话分叉出独立侧线程、并行执行任务、完成后自动将结果注入回主会话的执行模式。

## 关键要点

- 与 Claude Code 的 /btw 功能类似但更完善，属于 Agent Harness 层的并行能力

- 工作流程：从当前会话的最后稳定点 fork → 侧线程独立运行 → 完成后自动注入主线程

- 侧线程跟踪元数据：修改的文件、附件、副作用、与主线程可能的冲突

- 如果主线程仍在运行，结果会排队在 Parallel 面板中，用户可选择导入、跳过、取消或查看

- 关键设计：侧线程获得与主线程相同的上下文但不会污染主 Agent 循环

- 区别于「多会话并行探索」——后者是用户手动开多个会话做方向发散，而并行 Agent 线程是 Harness 自动管理的 fork-execute-rejoin 机制

## 来源引用

- [摘要：Personal Agent Features (Part 2)](summaries/摘要：Personal Agent Features (Part 2).md)（[X 原文](https://x.com/trashpandaemoji/status/2048387560339013912)）

## 关联概念

- [Personal Agent](entities/Personal Agent.md)

- [上下文播种](concepts/上下文播种.md)

- [会话分叉](concepts/会话分叉.md)

- [Context Compaction](concepts/Context Compaction.md)

- [多会话并行探索](concepts/多会话并行探索.md)
