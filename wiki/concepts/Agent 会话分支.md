---
title: Agent 会话分支
type: concept
tags:
- 上下文管理
status: 草稿
confidence: medium
last_compiled: '2026-04-29'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/5da8b931f3e64d3b99a28a9ff56de699
notion_id: 5da8b931-f3e6-4d3b-99a2-8a9ff56de699
---

## 定义

Agent 会话分支（Session Branching / Forking）是一种在 AI Agent 对话中创建平行分支的机制，类似 Git 的 branch 操作。用户可以在某个对话节点分叉出新路径，探索不同方案，而不会丢失原始上下文。

## 关键要点

- 在 Hermes Agent 中通过 `/branch`（别名 `/fork`）命令实现

- 允许用户在不丢失已建立上下文的前提下探索风险更高的方案

- 如果分支方案失败，可返回原始分支继续

- 解决了传统聊天界面的核心痛点：开新会话 = 丢失所有上下文

- 概念上等同于「对话的版本控制」

## 与其他概念的关系

- 与 Steer 机制（运行中纠偏）互补：分支是「试另一条路」，Steer 是「在当前路上调方向」

- 与上下文管理密切相关：分支的价值在于保留上下文窗口中的已有信息

- 与 Agent 文件系统快照（/rollback、/snapshot）配合使用，形成完整的「后悔药」体系

## 来源引用

- [摘要：15 Hermes Agent features you've never touched](summaries/摘要：15 Hermes Agent features you've never touched.md)（[原文](https://x.com/sharbel/status/2049158152709382177)）
