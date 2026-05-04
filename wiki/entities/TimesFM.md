---
title: TimesFM
type: entity
tags:
- 训练/微调
- 模型评测
status: 草稿
confidence: medium
last_compiled: ''
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/4c1c4c3655164dc8a0a08cbc2e3e76fb
notion_id: 4c1c4c36-5516-4dc8-a0a0-8cbc2e3e76fb
---

**定义**

TimesFM（Time Series Foundation Model）是 Google Research 开发的预训练通用时序基础模型，采用 decoder-only 架构，面向零样本时序预测。

### 关键要点

- 最新版本 TimesFM 2.5 将参数降至 200M，上下文窗口扩展到 16k。

- 采用 patch-based tokenization：把连续时间点分组为 patch 作为 token，在 stacked Transformer 上做自回归预测。

- 定位是通用时序底座，金融只是其中一个子场景；Kronos 论文将其作为 baseline 之一。

- 开源：[GitHub](https://github.com/google-research/timesfm)

### 与知识库其他条目的关系

- 是 [Kronos](entities/Kronos.md) 论文中的主要对标对象

- 已有摘要条目讨论 2.5 版本更新

- 与 [金融市场基础模型](concepts/金融市场基础模型.md) 的区别：通用 vs 金融专用
