---
title: Continual Learning
type: concept
tags: []
status: 审核中
confidence: high
last_compiled: '2026-04-23'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/c5d4696c61814869ad672b1663a43804
notion_id: c5d4696c-6181-4869-ad67-2b1663a43804
---

### 定义

持续学习是指让模型或系统在持续接触新任务、新数据和新环境时，不断扩展能力边界的一类研究方向。本文强调它不应被狭义理解为某一种具体训练方法，而更接近一个持续推动能力上限外移的目标方向。

### 关键要点

- 它不只等于“解决灾难性遗忘”。

- 它更像一支“箭头”，指向模型能力持续外推，而不是一个独立的点状技术。

- 在不同技术阶段，承担这一角色的实现手段会变化，例如从 pretraining 到 SFT，再到 RL 与 context management。

- 对这类问题的评估，不能只看单次任务表现，还要看长期任务跨度是否被推进。

### 来源引用

- 《前两天看到 Dario Amodei 在一个采访里说，continual learning已经 solved 了。》｜X书签｜2026/04/12｜主链接：[X 原文](https://x.com/AI_Whisper_X/status/2043279143496769940)｜源页面：Continual Learning 究竟有没有被「解决」？Dario 与蔡天乐的框架之争

- [摘要：Defining Continual Learning](summaries/摘要：Defining Continual Learning.md)（[原文](https://x.com/carnot_cyclist/status/2041479655035679163)）

### 关联概念

- Continual Learning 究竟有没有被「解决」？Dario 与蔡天乐的框架之争中同时讨论了 Task Horizon、Agentic Context Management、灾难性遗忘、Test-time Training。

- 本文进一步把 [灾难性遗忘](concepts/灾难性遗忘.md)、[Class-Incremental Learning](concepts/Class-Incremental Learning.md)、[参数化持续学习](concepts/参数化持续学习.md) 与 [Harness Engineering](concepts/Harness Engineering.md) 放到同一框架下讨论。
