---
title: Class-Incremental Learning
type: concept
tags:
- LLM
- 训练/微调
status: 草稿
confidence: high
last_compiled: '2026-04-23'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/6ce6d853bc404a4890491c81c6c73c06
notion_id: 6ce6d853-bc40-4a48-9049-1c81c6c73c06
---

## 定义

Class-Incremental Learning 指模型在按阶段顺序学习不同类别或技能后，不仅能分别完成各阶段任务，还能把不同阶段习得的表示整合起来，在统一任务空间中进行跨阶段泛化与组合。

## 关键要点

- 它是持续学习中的一个高标准测试，不满足于“记住旧任务 + 学会新任务”。

- 更关键的是让模型能把不同时间点学到的能力重新组合，而不是彼此隔离。

- 在本文语境下，它被用来说明持续学习应具备累积性与组合性，而不是只做局部适配。

## 来源引用

- [摘要：Defining Continual Learning](summaries/摘要：Defining Continual Learning.md)（[原文](https://x.com/carnot_cyclist/status/2041479655035679163)）

## 关联概念

- [Continual Learning](concepts/Continual Learning.md)

- [灾难性遗忘](concepts/灾难性遗忘.md)

- [Harness Engineering](concepts/Harness Engineering.md)

- [参数化持续学习](concepts/参数化持续学习.md)
