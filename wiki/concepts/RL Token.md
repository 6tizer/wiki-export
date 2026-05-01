---
title: RL Token
type: concept
tags: []
status: 审核中
confidence: high
last_compiled: '2026-04-23'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/ffef40bf566441478b8e417ac6c03b93
notion_id: ffef40bf-5664-4147-8b8e-417ac6c03b93
---

## 定义

RL Token 是文中强调的一条具身智能训练路线，核心思路是把强化学习后训练与 VLA 体系结合起来，在尽量冻结大模型主体能力的前提下，实现低成本、低遗忘的场景化优化。

## 关键要点

- 它试图解决 VLA 强化学习中推理成本高、微调容易灾难性遗忘的两类典型问题。

- 文章描述其做法包括信息瓶颈编码、冻结 VLA 主体参数与两阶段训练策略。

- 该路线把需要训练的参数规模大幅压缩，使消费级显卡也能完成后训练。

- 它的意义在于让强化学习更容易进入真实行业和具体任务，而不是停留在高门槛研究环境中。

## 来源引用

- [摘要：特斯拉开源硬件，中国公司回应来了：直接把机器人大脑开源了](summaries/摘要：特斯拉开源硬件，中国公司回应来了：直接把机器人大脑开源了.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzIzNjc1NzUzMw%3D%3D&mid=2247885437&idx=1&sn=6a4c424526417657d528b8bfa9d0c200&chksm=e9963f58459d6d389133ac94bd91c6f2c51c8c7cc4fba208ced0e1d73052dc4d5db0a7661e16#rd)）

## 关联概念

- [AlphaBrain Platform](entities/AlphaBrain Platform.md)

- [NeuroVLA](entities/NeuroVLA.md)

- [可插拔世界模型架构（WA）](concepts/可插拔世界模型架构（WA）.md)

- [智平方](entities/智平方.md)
