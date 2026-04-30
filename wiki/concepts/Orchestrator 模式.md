---
title: Orchestrator 模式
type: concept
tags:
- Agent 协作模式
- 多Agent协作
- OpenClaw
status: 审核中
confidence: high
last_compiled: '2026-04-30'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/06e009e6ba284035af6207bc2ce09a32
notion_id: 06e009e6-ba28-4035-af62-07bc2ce09a32
---

## 定义

Orchestrator 模式是一种让主 Agent 主要负责规划、拆解与调度，而把具体执行交给子智能体的编排策略。

## 关键要点

- 它适合并行性强、角色分工清晰的复杂任务，而不适合一切场景都强制拆分。

- 真实收益来自上下文隔离和任务并行，而不是“智能体数量越多越强”。

- 如果共享上下文、回溯推理或资源限制更重要，多智能体反而可能降低效率。

## 来源引用

- [原文链接](https://x.com/shao__meng/status/2030818206882103640)｜《OpenClaw Orchestrator 模式：一条提示词让智能体效率提升 10 倍？》｜来源条目：OpenClaw Orchestrator 模式：一条提示词让智能体效率提升 10 倍？

- [原文链接](https://x.com/LawrenceW_Zen/status/2035949835124351009)｜《用 Claude Code 调度 Codex 当 SubAgent：省 Token 的多 Agent 编排实践》｜来源条目：[摘要：用 Claude Code 调度 Codex 当 SubAgent：省 Token 的多 Agent 编排实践](summaries/摘要：用 Claude Code 调度 Codex 当 SubAgent：省 Token 的多 Agent 编排实践.md)

- [原文链接](https://x.com/alin_zone/status/2036000855389020406)｜《前端 Gemini、后端 Codex：用 Claude Code 调度多 Agent 的分工哲学》｜来源条目：[摘要：前端 Gemini、后端 Codex：用 Claude Code 调度多 Agent 的分工哲学](summaries/摘要：前端 Gemini、后端 Codex：用 Claude Code 调度多 Agent 的分工哲学.md)

- [原文链接](https://x.com/sujingshen/status/2043898494818410731)｜《三省六部幻觉：为什么"虚拟公司"式多Agent架构在工程上不成立》｜来源条目：三省六部幻觉：为什么「虚拟公司」式多 Agent 架构在工程上走不通

- [摘要：Single-agent AI coding is a nightmare for engineers](summaries/摘要：Single-agent AI coding is a nightmare for engineers.md)（[原文](https://x.com/MilksandMatcha/status/2044863551186309460)）

- [摘要：Composing a Search Engine](summaries/摘要：Composing a Search Engine.md)（[原文](https://exa.ai/blog/composing-a-search-engine)）

- [摘要：Sub-Agents vs Agent Teams: The Architecture Decision That Changes Everything](summaries/摘要：Sub-Agents vs Agent Teams- The Architecture Decision That Changes Everything.md)（[原文](https://x.com/NainsiDwiv50980/status/2049529787300090344)）

## 关联概念

- [Claude Code](entities/Claude Code.md)

- [Codex](entities/Codex.md)

- [Gemini 3 Pro](entities/Gemini 3 Pro.md)

- [三省六部式多 Agent 架构](concepts/三省六部式多 Agent 架构.md)

- [显式外部状态](concepts/显式外部状态.md)

- [Context Engineering](concepts/Context Engineering.md)

- [上下文隔离](concepts/上下文隔离.md)

- [阶段式并行执行](concepts/阶段式并行执行.md)

- [Codex Spark](entities/Codex Spark.md)
