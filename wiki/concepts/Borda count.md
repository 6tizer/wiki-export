---
title: Borda count
type: concept
tags:
- Agent 编排
status: 草稿
confidence: high
last_compiled: '2026-04-14'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/0cfc4e1536ab4635a0c5957b693075bf
notion_id: 0cfc4e15-36ab-4635-a0c5-957b693075bf
---

## 定义

Borda count 是一种按排序位置分配分值的聚合投票方法。在 Autoreason 中，它用于汇总多位裁判对 A、B、AB 三个候选版本的盲评排序，减少单个裁判噪声对结果的影响。

## 核心要点

- 不是简单多数决，而是利用完整排序信息聚合偏好

- 适合多个候选版本并存的评审场景

- 比单裁判或只看第一名更稳定，能提升收敛质量

- 在多 agent 评审流程里，本质上是“判断汇总层”

## 来源引用

- [原文链接](https://x.com/SHL0MS/status/2043415274196435325)｜《SHL0MS | HERMES AGENT》｜源文章：Autoreason：让 AI 知道什么时候该停止「自我批评」

- [原文链接](https://x.com/shannholmberg/status/2043983746094026984)｜《how to use autoreason for marketing》｜来源条目：[摘要：how to use autoreason for marketing](summaries/摘要：how to use autoreason for marketing.md)

## 关联概念

- [Autoreason](concepts/Autoreason.md)

- [盲评裁判团](concepts/盲评裁判团.md)

- [隔离式 Agent](concepts/隔离式 Agent.md)

- [对抗式评审](concepts/对抗式评审.md)

- [组织级知识层](concepts/组织级知识层.md)

- [autoresearch](entities/autoresearch.md)
