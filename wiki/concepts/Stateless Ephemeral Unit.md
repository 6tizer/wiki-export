---
title: Stateless Ephemeral Unit
type: concept
tags:
- Agent 编排
status: 草稿
confidence: medium
last_compiled: '2026-04-20'
source_tags: Multi-Agent, Agent, 自动化, LLM
source_article_url: https://www.notion.so/348701074b68811e9eddc16eb1202200
notion_url: https://www.notion.so/b4a0c98c85b24d38a18990ffb392be5e
notion_id: b4a0c98c-85b2-4d38-a189-90ffb392be5e
---

## 定义

Stateless Ephemeral Unit 是 Hermes 多 Agent 调度中的一次性无状态执行单元：每次委派都会创建全新的子 Agent，在不继承历史记忆与上下文文件的前提下独立完成局部任务。

## 关键要点

- 通过临时实例化子 Agent，实现任务级别的上下文隔离，避免不同子任务互相污染

- 适合日志读取、并行检索、局部分析等可以拆分为独立子任务的场景

- 核心价值不只是“多开几个 Agent”，而是把子 Agent 视作可调度的函数式执行单元

- 与长驻、连续对话型 Agent 相比，这种模式更强调 token 效率、可控性与并行吞吐

## 来源引用

- [摘要：Hermes 多 Agent 深水区：三个高级实战技巧](summaries/摘要：Hermes 多 Agent 深水区：三个高级实战技巧.md)（[原文](https://x.com/BTCqzy1/status/2045720855137903046)）

## 关联概念

- [Hermes Agent](entities/Hermes Agent.md)

- [delegate_task](concepts/delegate_task.md)

- [LLM-Driven Replan](concepts/LLM-Driven Replan.md)

- [Subdirectory Hints](concepts/Subdirectory Hints.md)
