---
title: Cursor /multitask
type: concept
tags:
- IDE 集成
- 多Agent协作
- 代码生成
status: 草稿
confidence: medium
last_compiled: '2026-04-27'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/10d601c1f4ac4a659df509276991bbb1
notion_id: 10d601c1-f4ac-4a65-9df5-09276991bbb1
---

## 定义

Cursor /multitask 是 Cursor 3 引入的异步子代理并行执行功能。用户可以通过 `/multitask` 命令让 Cursor 同时启动多个异步子代理（async subagents），并行处理不同的编码任务，而不是将请求排入串行队列依次等待。对于已在队列中的消息，也可以选择切换到并行模式执行。

别名：/multitask command, Cursor multitask

## 关键要点

- 解决了传统 IDE Agent 串行队列的效率瓶颈——第二个任务必须等第一个完成才能开始

- 支持最多 10 个并行 worker（据社区反馈），云端 Agent 在用户基础设施上运行

- 结合 Git Worktree 实现分支隔离，避免多个 Agent 编辑同一文件造成冲突

- 核心挑战在于 Agent 协调层——当 Agent A 写入的文件被 Agent B 需要时，如何处理依赖关系、共享状态漂移、冲突检测

- 社区讨论指出：并行化本身容易，真正的工程难题是协调——没有冲突检测的并行只会更快地制造混乱

## 关联概念

- [Cursor](entities/Cursor.md)

- [Git Worktree](concepts/Git Worktree.md)

- [Subagents 并行](concepts/Subagents 并行.md)

- [协调税](concepts/协调税.md)

## 来源引用

- [摘要：Cursor 3 /multitask 异步子代理并行执行](summaries/摘要：Cursor 3 -multitask 异步子代理并行执行.md)（[原文](https://x.com/cursor_ai/status/2047764651363180839)）
