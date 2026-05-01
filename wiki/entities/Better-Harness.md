---
title: Better-Harness
type: entity
tags: []
status: 审核中
confidence: high
last_compiled: '2026-04-12'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/e82a33b8911b4340928962bea3033e14
notion_id: e82a33b8-911b-4340-9289-62bea3033e14
---

## 定义

Better-Harness 是 LangChain 提出的 Agent 优化方法论，核心是把评测结果当作反馈信号，持续迭代 Agent 的执行底座，而不是优先更换底层模型。

## 关键要点

- 强调 **Agent = Model + Harness**，决定上限的往往不是模型本身，而是模型外的系统设计

- 通过反复运行评测、分析失败样本、调整 prompt、工具描述与验证循环来提升表现

- 重点关注泛化能力，而不是只对少量已知任务做局部调优

- 特别适合终端型 Coding Agent 和可重复回放的工作流场景

## 关联概念

- [Agent Harness](concepts/Agent Harness.md)

- [Harness Engineering](concepts/Harness Engineering.md)

- [Terminal Bench 2](entities/Terminal Bench 2.md)

## 来源引用

- [原文链接](https://x.com/berryxia/status/2042367800338260467)｜《Better-Harness：LangChain 用 Evals 当梯度信号，让 Agent 越跑越强》｜源文章：Better-Harness：LangChain 用 Evals 当梯度信号，让 Agent 越跑越强
