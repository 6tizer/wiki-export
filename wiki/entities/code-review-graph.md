---
title: code-review-graph
type: entity
tags:
- Coding Agent
- 开发工具
status: 草稿
confidence: high
last_compiled: '2026-04-17'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/353e29a1f1b54f5089d04a94124b7065
notion_id: 353e29a1-f1b5-4f50-89d0-4a94124b7065
---

## 定义

code-review-graph 是一个面向 Claude Code 等 AI 编码助手的本地代码知识图谱工具。它通过解析代码结构、持续追踪变更，并经由 MCP 向 Agent 提供精确上下文，减少每次任务都重扫整个仓库带来的 Token 浪费。

## 关键要点

- **定位**：不是通用 IDE 插件，而是给 Coding Agent 提供结构化上下文层的基础设施

- **核心机制**：结合 Tree-sitter、增量更新和影响范围计算，把代码库转成可查询的图谱

- **接入方式**：通过 MCP 暴露给 Claude Code 等工具，让 Agent 只读取真正相关的函数、类、依赖和测试

- **价值点**：在代码审查和日常编码任务中显著降低上下文读取成本，尤其适合大型单体仓库

## 来源引用

- [原文链接](https://mp.weixin.qq.com/s?__biz=MzY5NzIxODM2MQ%3D%3D&mid=2247484353&idx=1&sn=f2ad30ea21fee327daac93a9143a76fb&chksm=f539ae6800aa8066504c6b4ed683e14b501d516a93882ddd92b4c501a2537281c3b85d7d3c8f#rd)｜《code-review-graph：Claude Code 本地知识图谱，减少 6.8 倍代码审查 Token !》｜源页面：code-review-graph：Claude Code 本地知识图谱，减少 6.8 倍代码审查 Token !

## 关联概念

- [Claude Code](entities/Claude Code.md)

- [MCP 协议](concepts/MCP 协议.md)
