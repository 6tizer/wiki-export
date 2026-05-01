---
title: PPAF循环
type: concept
tags:
- Harness 工程
- 上下文管理
status: 审核中
confidence: high
last_compiled: '2026-04-23'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/1ca5aa0ecc074023b77e04bfb19542ae
notion_id: 1ca5aa0e-cc07-4023-b77e-04bfb19542ae
---

## 定义

PPAF循环（Perception-Planning-Action-Feedback）是Harness Engineering描述Agent运作的四阶段持续循环模型。

## 四个阶段

- **感知（Perception）**：Agent感知当前世界状态，包括用户输入、工具结果、历史对话等

- **规划（Planning）**：基于感知信息，由规划器更新目标、拆解任务、选择下一步行动

- **行动（Action）**：执行内部操作或外部操作（调用工具、发出回复）

- **反思（Feedback）**：行动结果重新注入上下文，驱动下一轮感知

## 关联概念

- [Harness Engineering](concepts/Harness Engineering.md)

- [R.E.S.T模型](concepts/R.E.S.T模型.md)

- [REPL Harness](concepts/REPL Harness.md)

- [Token Transformation Pipeline](concepts/Token Transformation Pipeline.md)

- Agent八原语框架

## 来源引用

- [摘要：万字干货：理解 Harness Engineering，看这一篇就够了](summaries/摘要：万字干货：理解 Harness Engineering，看这一篇就够了.md)（[TRAE.ai](http://trae.ai/)，微信，2026-04-10）

- [摘要：The Definitive Guide to Harness Engineering](summaries/摘要：The Definitive Guide to Harness Engineering.md)（[原文](https://x.com/Trae_ai/status/2047145274200768969)）
