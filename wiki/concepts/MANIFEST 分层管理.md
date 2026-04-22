---
title: MANIFEST 分层管理
type: concept
tags:
- Agent 编排
status: 审核中
confidence: medium
last_compiled: '2026-04-20'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/cb0477e320004b91a5ee3d65dfe01482
notion_id: cb0477e3-2000-4b91-a5ee-3d65dfe01482
---

## 定义

MANIFEST 分层管理是一种 AI 协作中的上下文控制策略，通过将项目文件分为三个层级（Tier 1 核心必读、Tier 2 按需加载、Tier 3 归档忽略）来严格控制 AI 每次交互能看到的信息范围，避免百万 token 窗口被无关内容填满。

## 关键要点

- **Tier 1**：核心真相文件，每次会话必须读取

- **Tier 2**：按需加载的项目文档，根据任务类型选择性引入

- **Tier 3**：归档文件，默认忽略

- 核心原则：严格最小化上下文，比塞满百万 token 窗口更有效

- 与 OpenClaw 的 [USER.md](http://user.md/) / [SOUL.md](http://soul.md/) / [AGENTS.md](http://agents.md/) 持久化文件理念一致

- 本质是 Context Engineering 在文件层面的具体实践

## 来源引用

- [摘要：让Claude cowork强100倍的17个习惯](summaries/摘要：让Claude cowork强100倍的17个习惯.md) — 将 MANIFEST 分层管理列为第一个核心习惯
