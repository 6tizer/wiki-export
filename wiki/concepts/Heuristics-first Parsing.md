---
title: Heuristics-first Parsing
type: concept
tags:
- 知识管理
- Agent 协作模式
- 推理优化
status: 审核中
confidence: medium
last_compiled: '2026-04-23'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/77af623fae35447bb4b26711c407c20d
notion_id: 77af623f-ae35-447b-b4b2-6711c407c20d
---

## 定义

Heuristics-first Parsing 指优先用规则、锚点、版式线索和后处理策略来完成文档解析，而不是一开始就依赖 VLM 或其他机器学习模型。

## 关键要点

- 适合结构较稳定、对延迟和成本敏感的解析任务。

- 优势是可解释、可控、易于本地部署。

- 不足是面对极端复杂版式或噪声文档时上限可能低于重模型方案。

- 在 Agent 工作流里，它适合作为“先快后重”的第一层解析策略。

## 来源引用

- [摘要：fast and light](summaries/摘要：fast and light.md)（[原文](https://x.com/jerryjliu0/status/2047041129326194882)）
