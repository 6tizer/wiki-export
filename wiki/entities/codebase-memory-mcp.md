---
title: codebase-memory-mcp
type: entity
tags:
- Coding Agent
- Agent 技能
status: 审核中
confidence: high
last_compiled: '2026-04-21'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/032e8503f6714c2dbdc345a1d93d2bd1
notion_id: 032e8503-f671-4c2d-bdc3-45a1d93d2bd1
---

## 定义

codebase-memory-mcp 是一个面向 AI 编程代理的代码智能引擎与 MCP Server，通过 tree-sitter 和持久化知识图谱把代码库转换成可结构化查询的索引，以减少 file-by-file 探索带来的 token 浪费。

## 档案要点

- 形态是单二进制、零依赖的代码索引与查询工具，强调快速安装与本地运行。

- 核心价值不是“读更多文件”，而是把函数、类、调用链、路由和跨服务关系预先结构化，再按需返回给代理。

- 它适合大型仓库、复杂架构和需要反复追踪调用关系的 Coding Agent 场景。

- 在这篇文章里，它代表“把代码理解从全文搜索升级为结构化检索”的路线。

## 关联概念

- [RTK](entities/RTK.md)

- [Context Mode](concepts/Context Mode.md)

## 来源引用

- [摘要：The fastest and most efficient code intelligence engine for AI coding agents.](summaries/摘要：The fastest and most efficient code intelligence engine for AI coding agents.md)（[原文](https://x.com/DataChaz/status/2045784379155226971)）
