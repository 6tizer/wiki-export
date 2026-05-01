---
title: Tuned Lens
type: concept
tags:
- 模型评测
status: 草稿
confidence: medium
last_compiled: '2026-04-27'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/644c1869b2a94c5faf979241ae6e3e79
notion_id: 644c1869-b2a9-4c5f-af97-9241ae6e3e79
---

## 定义

Tuned Lens 是一种把语言模型中间层表征映射到输出词分布空间的分析方法，用来观察模型在不同深度的“临时预测”。

## 关键要点

- 它可帮助研究者跟踪信息如何从深层隐藏状态逐步投影到最终输出空间。

- 在这篇论文中，Tuned Lens 被用于分析残差流向 logit 空间过渡时的信息保留情况。

- 结果表明，即使在低维投影轨迹中，背景与无关特征仍然可以被探针读出。

## 来源引用

- [摘要：苹果新论文发出惊人一问：What do your logits know?](summaries/摘要：苹果新论文发出惊人一问：What do your logits know.md)

## 关联概念

- [残差流](concepts/残差流.md)

- [探针](concepts/探针.md)

- [Top-k Logits](concepts/Top-k Logits.md)

- [信息瓶颈原则](concepts/信息瓶颈原则.md)
