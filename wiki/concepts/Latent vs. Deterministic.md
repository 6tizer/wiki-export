---
title: Latent vs. Deterministic
type: concept
tags:
- Agent 协作模式
- Harness 工程
status: 审核中
confidence: high
last_compiled: '2026-04-15'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/539fe8eff40a4638a4e43fcf82610bc3
notion_id: 539fe8ef-f40a-4638-a4e4-3fcf82610bc3
---

## 定义

Latent vs. Deterministic 是一种任务分工原则：把判断、解释、归纳、模式识别等放在模型的 latent space 中，把计算、检索、约束执行和可验证流程交给确定性系统。

## 关键要点

- 需要主观判断和语义综合的步骤适合交给 LLM

- 需要可重复、可校验、低容错的步骤应下放给代码、SQL、脚本或规则引擎

- 错把确定性问题塞进模型，通常会带来幻觉和不可追溯错误

- 好的 Agent 不是让模型做一切，而是明确边界并在两侧协作

## 关联概念

- [Agent Harness](concepts/Agent Harness.md)

- [Context Engineering](concepts/Context Engineering.md)

- [确定性工具](concepts/确定性工具.md)

- [Skillify](concepts/Skillify.md)

## 来源引用

- [原文链接](https://x.com/garrytan/status/2042925773300908103)｜《Thin Harness, Fat Skills》｜源文章：Thin Harness, Fat Skills：Garry Tan 的 AI Agent 生产力架构

- [摘要：How to really stop your agents from making the same mistakes](summaries/摘要：How to really stop your agents from making the same mistakes.md)（[原文](https://x.com/garrytan/status/2046876981711769720)）
