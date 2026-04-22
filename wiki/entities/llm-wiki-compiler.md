---
title: llm-wiki-compiler
type: entity
tags:
- 知识管理
- 开发工具
status: 草稿
confidence: high
last_compiled: '2026-04-20'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/449cdfa601bf4a548b48d2d69d161caa
notion_id: 449cdfa6-01bf-4a54-8b48-d2d69d161caa
---

## 定义

llm-wiki-compiler 是一个把原始网页、文档与笔记编译成互相链接的 Markdown Wiki 的知识编译工具，灵感直接来自 Karpathy 的 LLM Wiki 方法论。

## 核心要点

- **两阶段编译**：先统一抽取概念，再批量生成页面，减少顺序依赖并把共享概念合并到同一词条。

- **增量更新**：通过哈希检测只重编发生变化的源资料，适合持续积累型知识库。

- **问答可沉淀**：查询结果可以保存回 Wiki，让后续检索直接复用之前的思考产物。

- **MCP 接入**：内置 MCP Server，方便 Claude Desktop、Cursor、Claude Code 等 Agent 直接驱动 ingest、compile、query、lint 流程。

## 项目数据

- **仓库**：atomicmemory/llm-wiki-compiler

- **语言**：TypeScript

- **GitHub Stars**：618

- **License**：MIT

## 来源引用

- [摘要：AI researchers and engineers](summaries/摘要：AI researchers and engineers.md)（[原文](https://x.com/ollama/status/2045282803387158873)）

## 关联概念

- [Karpathy LLM Wiki 方法论](concepts/Karpathy LLM Wiki 方法论.md)

- [Hermes Agent](entities/Hermes Agent.md)

- [Ollama](entities/Ollama.md)
