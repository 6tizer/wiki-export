---
title: Context Anxiety
type: concept
tags:
- 上下文管理
status: 草稿
confidence: medium
last_compiled: '2026-05-03'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/f80c367f92d04d2b85dd7e304c148188
notion_id: f80c367f-92d0-4d2b-85dd-7e304c148188
---

## 定义

Context Anxiety（上下文焦虑）是 Cursor 团队观察到的一种 LLM 行为模式：当 context window 被逐渐填满时，某些模型会开始拒绝执行任务，表现为回复"这任务太大了"等回避性语言。

这是一种类似于"工作压力反应"的 LLM 行为退化，不是模型的显式设计，而是在长 context 下的涌现行为。

## 关键要点

- **触发条件**：context window 使用率较高时（如 70%+）更容易出现

- **表现形式**：模型开始 hedge（含糊其辞）、拒绝执行、声称任务过于复杂

- **对治方法**：Cursor 通过调整 prompt 来抑制此行为，属于 per-model harness 定制的一部分

- **工程启示**：harness 工程师的工作之一是识别这类模型特有的行为模式并对症下药，维护一份"模型 quirks 笔记"很有价值

## 与相关概念的区别

- 与 Context Rot 不同：Context Rot 是错误信息在 context 中累积导致后续推理质量下降；Context Anxiety 是模型对长 context 的主动回避行为

- 是 per-model 定制的一个实际用例——不同模型的 anxiety 阈值和表现形式不同

## 来源引用

- [摘要：精读 Cursor《Continually improving our agent harness》：一个 agent 产品团队的工程方法论全景](summaries/摘要：精读 Cursor《Continually improving our agent harness》：一个 agent 产品团队的工程方法论全景.md)（[原文](https://x.com/elliotchen100/status/2050757239364002193)）
