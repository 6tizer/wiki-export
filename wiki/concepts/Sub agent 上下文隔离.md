---
title: Sub agent 上下文隔离
type: concept
tags:
- Agent 编排
- Agent 技能
status: 草稿
confidence: high
last_compiled: '2026-04-23'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/eabdce1ef9de4f4c852d11bad9ee6ad4
notion_id: eabdce1e-f9de-4f4c-852d-11bad9ee6ad4
---

## 定义

通过子线程或子 Agent 承担检索、试错和工具调用，让这些中间过程停留在独立 context 中，主线程只接收最终结论。

## 关键要点

- 隔离的不是任务本身，而是中间噪音、原始检索结果和临时试验。

- 子线程边界能降低主对话被大段资料污染的风险。

- 这种方式天然支持并行查询、失败隔离和后端替换。

- 在 Notion AI 中，`createAndRunThread` 是实现该模式的核心能力之一。

## 来源引用

- [摘要：Notion AI × Sub Agent：把检索隔离写进长期指令的实战](summaries/摘要：Notion AI × Sub Agent：把检索隔离写进长期指令的实战.md)（[原始对话](https://www.notion.so/)）

- [摘要：A new way to think about composing skills to increase leverage: Skill Graphs 2.0](summaries/摘要：A new way to think about composing skills to increase leverage- Skill Graphs 2.0.md)（[原文](https://x.com/shivsakhuja/status/2047124337191444844)）

## 关联概念

- [Skill Graph](concepts/Skill Graph.md)

- [原子-分子-化合物技能分层](concepts/原子-分子-化合物技能分层.md)

- [Brain RAM 杠杆模型](concepts/Brain RAM 杠杆模型.md)
