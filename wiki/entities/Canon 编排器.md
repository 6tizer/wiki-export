---
title: Canon 编排器
type: entity
tags:
- 开发工具
- 工作流
status: 审核中
confidence: high
last_compiled: '2026-04-20'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/24e8f1f27e2c44b193c729b92ccea27f
notion_id: 24e8f1f2-7e2c-44b1-93c7-29b92ccea27f
---

## 定义

Canon 编排器是 Exa 为搜索引擎内部流水线构建的图式编排系统，用来统一调度查询编码、路由、检索、重排与内容提取等多个阶段。

## 关键要点

- 它把搜索过程表示为一组有依赖关系的节点，而不是一条写死的串行流程。

- 节点按需执行，便于在复杂度持续上升时保持系统可维护性。

- 其设计目标不只是性能，还包括开发体验、可组合性与可观察性。

## 来源引用

- [摘要：Composing a Search Engine](summaries/摘要：Composing a Search Engine.md)（[原文](https://exa.ai/blog/composing-a-search-engine)）

## 关联概念

- [Orchestrator 模式](concepts/Orchestrator 模式.md)

- [惰性求值](concepts/惰性求值.md)

- [取消传播](concepts/取消传播.md)

- [记忆化](concepts/记忆化.md)

- [Typestate](concepts/Typestate.md)
