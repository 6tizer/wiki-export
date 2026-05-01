---
title: 摘要：前两天看到 Dario Amodei 在一个采访里说，continual learning已经 solved 了。
type: summary
tags: []
status: 已审核
confidence: high
last_compiled: '2026-04-13'
source_tags: ''
source_article_url: https://www.notion.so/341701074b688174a4a1db6be5a32f64
notion_url: https://www.notion.so/Tizer/5c2b59e1af804e599809ca69adcb0a55
notion_id: 5c2b59e1-af80-4e59-9809-ca69adcb0a55
---

### 一句话摘要

这篇文章借 Tianle Cai 对 Dario Amodei 观点的回应，提出应把 Continual Learning 理解为持续推高模型 Task Horizon 的长期方向，而不是某一种单点训练方法。

### 关键洞察

- 传统机器学习语境里，Continual Learning 常被狭义理解为解决灾难性遗忘，但这个定义已经不足以覆盖今天的大模型系统演进。

- 文章提出一个更有解释力的框架：Continual Learning 不是一个“点状方法”，而是一支持续把能力边界向外推进的“箭头”。

- Task Horizon 被当作统一指标，用来衡量模型能够稳定完成任务的时间跨度，也因此能把 pretraining、SFT、RL、Agentic Context Management 放到同一演化坐标里理解。

- Dario 所说的“已经 solved”，更接近“在人类可用尺度上已经够用”，而不是说所有超长周期学习问题都已彻底解决。

- 对 Agent 系统而言，真正关键的不只是更大的 context window，而是如何通过笔记、压缩、外部记忆与流程设计，把长期执行能力延伸出去。

### 提取的概念

- [Continual Learning](concepts/Continual Learning.md)

- [Task Horizon](concepts/Task Horizon.md)

- [Agentic Context Management](concepts/Agentic Context Management.md)

- [灾难性遗忘](concepts/灾难性遗忘.md)

- [Test-time Training](concepts/Test-time Training.md)

### 原始文章信息

- 作者：@AI_Whisper_X

- 来源：X书签

- 发布时间：2026/04/12

- 原文链接：[X 原文](https://x.com/AI_Whisper_X/status/2043279143496769940)

- 源文章页面：Continual Learning 究竟有没有被「解决」？Dario 与蔡天乐的框架之争

### 个人评注

这篇文章对 Tizer 的工作流很有启发，因为它把“长期能力”从模型参数问题，转成了系统设计问题。对 OpenClaw、HITL 和内容流水线来说，真正重要的不是一次性回答质量，而是能否通过记忆、上下文管理、笔记沉淀和阶段性交接，把任务稳定推进到更长 horizon。
