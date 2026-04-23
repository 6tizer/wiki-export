---
title: Agentic Kernel Synthesis
type: concept
tags:
- 开发工具
- 推理优化
status: 草稿
confidence: high
last_compiled: '2026-04-23'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/cf76f92aaf8a4922b7c20a37604353f1
notion_id: cf76f92a-af8a-4922-b7c2-0a37604353f1
---

## 定义

Agentic Kernel Synthesis 是一种用 LLM agent 自动生成、进化并评估 CUDA/Triton 内核候选的推理编译优化方法，用于降低模型推理时延。

## 关键要点

- 通过候选生成、并行进化与延迟/数值精度打分来筛选最优内核。

- 属于“用 agent 优化底层系统”的工程化范式。

- 在 Avatar V 中被用于显著降低推理延迟。

## 来源引用

- [摘要：Avatar V: The End of Avatar Drift](summaries/摘要：Avatar V- The End of Avatar Drift.md)（[原文](https://x.com/joshua_xu_/status/2047099908281499803)）
