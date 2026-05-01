---
title: Subdirectory Hints
type: concept
tags:
- Harness 工程
- 上下文管理
- 多Agent协作
status: 审核中
confidence: medium
last_compiled: '2026-04-20'
source_tags: Multi-Agent, Agent, 自动化, LLM
source_article_url: https://www.notion.so/348701074b68811e9eddc16eb1202200
notion_url: https://www.notion.so/Tizer/4c6c4938b2924ec4a97349274236c714
notion_id: 4c6c4938-b292-4ec4-a973-49274236c714
---

## 定义

Subdirectory Hints 是一种局部上下文注入机制：当子 Agent 进入特定目录执行工具调用时，系统会把该目录下的 [AGENTS.md](http://agents.md/) 或 .cursorrules 等规则文件随工具结果一并注入，从而让目录级规则在需要时动态生效。

## 关键要点

- 它把规则注入时机从全局提示词阶段，后移到具体工具调用阶段，降低静态 Prompt 膨胀

- 规则只在进入对应目录并触发相关工具调用时出现，强调按需加载而非全局常驻

- 这种模式适合大型代码库或多子目录项目，让不同模块拥有各自的局部工作规范

- 它连接了目录结构、工具返回结果与 Agent 行为约束，是“文件即策略”的细粒度实现方式

## 来源引用

- [摘要：Hermes 多 Agent 深水区：三个高级实战技巧](summaries/摘要：Hermes 多 Agent 深水区：三个高级实战技巧.md)（[原文](https://x.com/BTCqzy1/status/2045720855137903046)）

## 关联概念

- [Hermes Agent](entities/Hermes Agent.md)

- [AGENTS.md](concepts/AGENTS.md.md)

- [delegate_task](concepts/delegate_task.md)

- [Stateless Ephemeral Unit](concepts/Stateless Ephemeral Unit.md)

- [LLM-Driven Replan](concepts/LLM-Driven Replan.md)
