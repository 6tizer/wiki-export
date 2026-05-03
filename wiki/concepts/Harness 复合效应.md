---
title: Harness 复合效应
type: concept
tags:
- Harness 工程
- 商业/生态
status: 草稿
confidence: high
last_compiled: '2026-05-03'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/2131f061021d4386997b96d84d4b83d8
notion_id: 2131f061-021d-4386-997b-96d84d4b83d8
---

## 定义

Harness 复合效应指 Agent Harness 的改进具有持久累积性——每次故障修复（lint 规则、hook、sub-agent、上下文模式）都成为永久性改进，适用于后续所有运行和所有未来模型。与之对比，模型升级会重置原始智力水平，但不会重置 Harness 层积累的工程优势。

## 关键要点

- 模型发布重置智力基线，Harness 投资不会被重置

- 每次 Agent 犯错 → 工程修复 → 永久写入 Harness → 不再犯同类错误

- 这是 Harness 团队能持续碾压通用 Agent 的结构性原因

- Mitchell Hashimoto 的原话：「anytime an agent makes a mistake, you engineer a solution so it never makes that mistake again. That fix lives in the harness.」

- 该效应解释了为什么使用相同模型的不同 Harness 之间可以出现 13+ 分的基准差距（如 LangChain deepagents-cli 从 52.8% 跳到 66.5%）

## 关联概念

- [Agent Harness](concepts/Agent Harness.md)

- [Harness Engineering](concepts/Harness Engineering.md)

- [Deep Agents](entities/Deep Agents.md)

- [Terminal-Bench 2.0](entities/Terminal-Bench 2.0.md)

## 来源引用

- [摘要：Why Everyone Is Suddenly Building Their Own Agent Harness](summaries/摘要：Why Everyone Is Suddenly Building Their Own Agent Harness.md)（[原文](https://x.com/code_kartik/status/2050631735529095575)）
