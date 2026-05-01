---
title: Self-Augmented History Training
type: concept
tags: []
status: 审核中
confidence: high
last_compiled: '2026-04-20'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/53a90aaa681c4aceabd28f5f9a8436f2
notion_id: 53a90aaa-681c-4ace-abd2-8f5f9a8436f2
---

### 定义

Self-Augmented History Training 是一种面向长程生成任务的训练策略：在训练阶段主动把模型自身产生的退化历史加入上下文，让模型学习在不完美历史条件下继续生成并纠正误差，而不是单纯依赖理想数据分布。

### 关键要点

- 核心目标是提升模型在长序列生成中的鲁棒性

- 通过暴露模型自己的“错误历史”，减少训练/推理之间的分布落差

- 特别适合世界模型、长视频生成和可探索场景合成等任务

- 在 Lyra 2.0 中，它被用来缓解长轨迹生成中的时序漂移问题

### 来源引用

- [摘要：NVIDIA Lyra 2.0：从一张图片生成可探索的持久 3D 世界](summaries/摘要：NVIDIA Lyra 2.0：从一张图片生成可探索的持久 3D 世界.md)（[原文](https://x.com/HuggingModels/status/2045337281775718800)）
