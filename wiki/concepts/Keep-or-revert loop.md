---
title: Keep-or-revert loop
type: concept
tags:
- 工作流
- Agent 编排
status: 草稿
confidence: medium
last_compiled: '2026-04-23'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/c0249f659c1f4898ba09c4b9fe8b916a
notion_id: c0249f65-9c1f-4898-ba09-c4b9fe8b916a
---

**定义**

Keep-or-revert loop 是一种自主优化闭环：Agent 提出改动、执行实验、根据预设指标判断结果是否变好，若变好则保留，若变差则回滚，然后继续下一轮迭代。

**关键要点**

- 它把开放式试错压缩为可度量、可比较、可累积的离散实验循环。

- 该机制适合训练、提示词优化、代码性能调优与工作流迭代等可量化任务。

- 这类循环的上限，通常不取决于“是否能改”，而取决于评估指标是否可靠、是否抗作弊。

**来源引用**

- [摘要：A curated, high-signal index of autonomous improvement loops, research agents, and descendants inspired by](summaries/摘要：A curated, high-signal index of autonomous improvement loops, research agents, and descendants inspired by.md)（[原文](https://x.com/aiwithmayank/status/2046914454353510893)）

**关联概念**

- [autoresearch](entities/autoresearch.md)
