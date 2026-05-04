---
title: FinCast
type: entity
tags:
- AI 产品
- 模型评测
status: 草稿
confidence: medium
last_compiled: ''
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/c50de512f0c047c6942103b747d3c1d7
notion_id: c50de512-f0c0-47c6-9421-03b747d3c1d7
---

**定义**

FinCast 是首个专为金融时序预测设计的基础模型，目标是在零样本设定下解决非平稳性、多领域多样性和多时间分辨率问题，无需任务特定微调。

### 关键要点

- 零样本 MSE 比现有 SOTA 平均低约 20%。

- 避免了通用时序模型常见的 flat-line 输出和均值回归失败模式，能产出趋势感知的高保真预测。

- 与 Kronos 的区别：FinCast 不走 K 线 tokenize 路线，而是直接面向金融时序的连续值建模。

- 论文与代码：[arXiv 2508.19609](https://arxiv.org/abs/2508.19609) ｜ [GitHub](https://github.com/vincent05r/FinCast-fts)

### 与知识库其他条目的关系

- 同属 [金融市场基础模型](concepts/金融市场基础模型.md) 赛道

- 可与 [Kronos](entities/Kronos.md) 对比：同为金融专用基础模型，但技术路线不同

- 与 [零样本金融预测](concepts/零样本金融预测.md) 直接相关
