---
title: MaTTS
type: concept
tags:
- 推理优化
- 长期记忆
status: 草稿
confidence: medium
last_compiled: '2026-04-30'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/7caab153e23d485f93441fcc322351d6
notion_id: 7caab153-e23d-485f-9344-1fcc322351d6
---

## 定义

MaTTS（Memory-aware Test-Time Scaling）是 ReasoningBank 论文中提出的一种推理时扩展策略。核心思路是在每个任务上分配更多计算资源，让 Agent 生成丰富、多样的交互经验，从而为记忆合成提供更强的对比信号，反过来又能指导更高质量的推理。

全称：Memory-aware Test-Time Scaling

## 关键要点

- **扩展交互经验**：通过增加每次任务的计算预算，产出更多元的经验样本

- **对比信号增强**：丰富经验为记忆蒸馏提供更强的正负对比，提升策略卡片质量

- **与 ReasoningBank 协同**：MaTTS 产出的高质量记忆反哺 ReasoningBank，形成正向循环

- **在基准测试中效果叠加**：单独使用 ReasoningBank 已有提升，叠加 MaTTS 后收益进一步放大

## 来源引用

- [摘要：Google just made AI agents learn from experience like humans do.](summaries/摘要：Google just made AI agents learn from experience like humans do.md)（[原文](https://x.com/AlphaSignalAI/status/2049821506515968132)）

## 关联概念

- [ReasoningBank](concepts/ReasoningBank.md)
