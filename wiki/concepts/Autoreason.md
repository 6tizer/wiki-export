---
title: Autoreason
type: concept
tags: []
status: 审核中
confidence: high
last_compiled: '2026-04-14'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/0f75150195064edfb2842c47becf7ef1
notion_id: 0f751501-9506-4edf-b284-2c47becf7ef1
---

## 定义

Autoreason 是一种面向主观任务的结构化自优化方法，受 [autoresearch](entities/autoresearch.md) 启发，将每轮优化组织为 A 原稿、B 对抗修订、AB 综合稿的三路竞赛，并用 fresh agents 组成的盲评裁判团通过 Borda count 选出下一轮胜者。

## 核心要点

- 把“保持不变”作为一等候选，避免模型为了修改而修改

- 将批评、修订、综合、评审拆给不同 agent，降低自我确认偏差

- 以 A 连续两轮获胜作为停止条件，避免无限 refinement

- 更适合开放式写作、研究和策略任务，不是纯客观题的万能方案

- 方法效果取决于模型生成能力与自评能力之间是否存在可利用差距

## 来源引用

- [原文链接](https://x.com/SHL0MS/status/2043415274196435325)｜《SHL0MS | HERMES AGENT》｜源文章：Autoreason：让 AI 知道什么时候该停止「自我批评」

- [原文链接](https://x.com/shannholmberg/status/2043983746094026984)｜《how to use autoreason for marketing》｜来源条目：[摘要：how to use autoreason for marketing](summaries/摘要：how to use autoreason for marketing.md)

- [摘要：Audit, fix, and optimize any website to be cited by ChatGPT, Perplexity, Claude, and Gemini.](summaries/摘要：Audit, fix, and optimize any website to be cited by ChatGPT, Perplexity, Claude, and Gemini.md)（[原文](https://x.com/shannholmberg/status/2046891905389334958)）

## 关联概念

- [Borda count](concepts/Borda count.md)

- [盲评裁判团](concepts/盲评裁判团.md)

- [隔离式 Agent](concepts/隔离式 Agent.md)

- 对抗式评审

- [组织级知识层](concepts/组织级知识层.md)

- [autoresearch](entities/autoresearch.md)
