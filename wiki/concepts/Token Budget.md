---
title: Token Budget
type: concept
tags:
- Coding Agent
- 工作流
status: 审核中
confidence: medium
last_compiled: '2026-04-28'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/ce03c5ab9fff42de98178887bb517ed4
notion_id: ce03c5ab-9fff-42de-9817-8887bb517ed4
---

## 定义

Token Budget 是一种把大模型调用成本显式预算化的控制机制：为 Agent 设定日度或任务级 Token 上限，并在接近阈值时自动压缩上下文或调整执行策略。

## 关键要点

- 它把“成本”从事后结算问题变成运行时治理问题。

- 常见实现包括每日额度、阈值告警、自动 concise 模式、上下文裁剪等。

- 对会长期运行、持续调用模型的 Agent 来说，Token Budget 是可运营性的基础设施。

- 它常与上下文管理、记忆压缩、任务优先级控制一起出现。

## 来源引用

- [摘要：Mercury: The AI Agent We All Wanted - Where Control, Permissions, and Autonomy Finally Got Real](summaries/摘要：Mercury- The AI Agent We All Wanted - Where Control, Permissions, and Autonomy Finally Got Real.md)（[原文](https://x.com/Ctrl_Alt_Zaid/status/2046902326657749114)）

- [摘要：Context Management in Agent Harnesses](summaries/摘要：Context Management in Agent Harnesses.md)（[原文](https://x.com/aparnadhinak/status/2048492731929149929)）

## 关联概念

- [Mercury](entities/Mercury.md)

- [Context Compaction](concepts/Context Compaction.md)

- [Alyx](entities/Alyx.md)
