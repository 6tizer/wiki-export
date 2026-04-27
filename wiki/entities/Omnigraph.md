---
title: Omnigraph
type: entity
tags:
- RAG/检索
- CLI 工具
status: 草稿
confidence: medium
last_compiled: '2026-04-27'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/9b3e8cbd87814482a089274ac06f41f1
notion_id: 9b3e8cbd-8781-4482-a089-274ac06f41f1
---

## 定义

Omnigraph 是一个用 Rust 编写的类型化属性图引擎（typed property graph engine），专为 AI Agent 提供知识/上下文层。支持 Git 风格的工作流（分支、提交、合并）、Schema-as-code 建模，以及混合搜索（图遍历 + 文本/模糊/BM25/向量/RRF 搜索）。

别名：omnigraph-cli

## 关键要点

- **Git 风格图工作流**：支持 branches、commits、merges 和 transactional runs

- **混合搜索**：在单一运行时内支持图遍历 + 文本搜索 + BM25 + 向量搜索 + RRF 融合

- **Schema-as-code**：类型化 schema、类型化查询、查询校验和 linting

- **存储灵活**：支持本地路径、S3 原生存储和快照固定读取

- **Policy-as-code**：服务端访问控制策略

- 语言：Rust（stable toolchain, edition 2024）

- 许可证：MIT

- GitHub Stars：43（截至 2026-04-27）

- 仓库：[https://github.com/ModernRelay/omnigraph](https://github.com/ModernRelay/omnigraph)

## 来源引用

- [摘要：Graph is the final boss of memory](summaries/摘要：Graph is the final boss of memory.md)（[原文](https://x.com/rohit4verse/status/2048081996841435596)）
