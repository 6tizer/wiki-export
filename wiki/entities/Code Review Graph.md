---
title: Code Review Graph
type: entity
tags: []
status: 审核中
confidence: medium
last_compiled: '2026-04-21'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/d4e8636ff0f74dcca29b4785a9ba8dba
notion_id: d4e8636f-f0f7-4dcc-a29b-4785a9ba8dba
---

## 定义

Code Review Graph 是一种基于 Tree-sitter 图结构的代码审查/代码检索工具思路，用结构化图谱替代大范围文件读取，让 AI 只读取与当前问题相关的符号与依赖关系。

## 档案要点

- 重点解决的是大仓库里“Claude 读了很多但真正有用的信息很少”的问题。

- 它把代码理解入口从文件级切换到符号级、关系级，因此更适合 monorepo 与跨模块审查。

- 在本文语境里，它代表结构化代码图在 token 节流上的优势。

## 关联概念

- [codebase-memory-mcp](entities/codebase-memory-mcp.md)

- [RTK](entities/RTK.md)

## 来源引用

- [摘要：The fastest and most efficient code intelligence engine for AI coding agents.](summaries/摘要：The fastest and most efficient code intelligence engine for AI coding agents.md)（[原文](https://x.com/DataChaz/status/2045784379155226971)）
