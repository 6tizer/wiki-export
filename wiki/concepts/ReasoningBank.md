---
title: ReasoningBank
type: concept
tags:
- 长期记忆
- 推理优化
status: 草稿
confidence: medium
last_compiled: '2026-04-30'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/f4257f8feff64f0390cc422fb6a82461
notion_id: f4257f8f-eff6-4f03-90cc-422fb6a82461
---

## 定义

ReasoningBank 是 Google 提出的一种面向 AI Agent 的记忆框架，通过将每次任务执行的经验蒸馏为简短的「策略卡片」（strategy card），让 Agent 在不重新训练模型的前提下持续从成功与失败中学习。成功经验成为可复用的「剧本」（playbook），失败经验成为需要规避的「陷阱」（trap）。

别名：Reasoning Memory Framework

论文：[ReasoningBank: Scaling Agent Self-Evolving with Reasoning Memory](https://arxiv.org/abs/2509.25140)

## 关键要点

- **无需微调**：不依赖标注数据或 fine-tuning，模型权重不变，仅通过外挂记忆层改善行为

- **策略卡片工作流**：执行任务 → 标注结果 → 提取经验 → 存入记忆库 → 下次任务前检索最相关的卡片

- **实验效果**：在 WebArena 上成功率提升 8.3%，在 SWE-Bench Verified 上提升 4.6%，执行步骤减少约 3 步

- **可与 MaTTS 叠加**：搭配 Memory-aware Test-Time Scaling（MaTTS）后收益进一步放大

- **自我进化**：每个周期模型表现都更好，实现 Agent 自我迭代闭环

## 来源引用

- [摘要：Google just made AI agents learn from experience like humans do.](summaries/摘要：Google just made AI agents learn from experience like humans do.md)（[原文](https://x.com/AlphaSignalAI/status/2049821506515968132)）

- [摘要：ReasoningBank](summaries/摘要：ReasoningBank.md)

## 关联概念

- [MaTTS](concepts/MaTTS.md)

- [SWE-Bench Verified](entities/SWE-Bench Verified.md)
