---
title: MOIRAI
type: entity
tags:
- 模型评测
- AI 产品
status: 草稿
confidence: medium
last_compiled: ''
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/1a86c899a9d943c3882f8e864579b29f
notion_id: 1a86c899-a9d9-43c3-882f-8e864579b29f
---

**定义**

MOIRAI 是 Salesforce 推出的通用多变量时序基础模型，支持不同频率、不同变量数量的时序预测任务。

### 关键要点

- 设计目标是「Universal Forecasting Transformer」——一个模型适配任意频率、任意变量数的时序任务。

- 通过 Any-Variate Attention 机制处理多变量，通过 Multiple Input/Output Patch Sizes 适配不同频率。

- 与 Kronos 的区别：MOIRAI 是通用底座，金融数据在训练集中占比不高；Kronos 是金融专用。

- 是 Kronos 论文中的 baseline 之一。

### 与知识库其他条目的关系

- 与 [Kronos](entities/Kronos.md) 论文中被比较

- 同属通用时序底座阵营，与 TimesFM、Chronos 并列

- 与 [金融市场基础模型](concepts/金融市场基础模型.md) 形成通用 vs 专用的对照
