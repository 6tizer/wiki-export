---
title: Dataset Policy Gradient
type: concept
tags:
- LLM
status: 草稿
confidence: medium
last_compiled: '2026-04-16'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/3a5dd74e64b5404aa50d375687813d03
notion_id: 3a5dd74e-64b5-404a-a50d-375687813d03
---

### 定义

Dataset Policy Gradient 是一种用于优化合成数据生成器的强化学习原语，目标是生成能把目标模型推向特定可微指标的数据集。

### 关键要点

- 在线程引用的相关工作中，它被用来说明合成训练数据可以精确塑造模型属性。

- 这意味着风险与能力都可能通过数据构造阶段被放大，而不只是发生在推理阶段。

- 它与 Subliminal Learning 共同指向一个结论：训练数据本身就是强控制面。

### 来源引用

- [Our paper on Subliminal Learning was just published in Nature!](https://x.com/OwainEvans_UK/status/2044488099707949545)｜源页面：潜意识学习：LLM 能通过语义无关数据悄悄传递「对齐信号」
