---
title: Data Automixing
type: concept
tags:
- 训练/微调
status: 草稿
confidence: medium
last_compiled: '2026-04-29'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/b5b52b00a0764420a7cd8ea37a328dce
notion_id: b5b52b00-a076-4420-a7cd-8ea37a328dce
---

## 定义

Data Automixing（数据自动混合）是一种训练数据配比优化方法，通过多轮小规模实验运行拟合代理回归模型（surrogate regressors），以近似估计数据集比例变化对下游评估的影响，从而自动确定最优的数据混合策略。

## 关键要点

- **核心思路**：不手动调配训练数据比例，而是通过实验 → 回归 → 预测的自动化循环来发现最佳配比

- **代理回归器**：从多组配比实验中拟合 surrogate regressors，用于快速预测不同数据比例下的模型表现

- **Poolside 实践**：Laguna 系列模型训练中使用了 Data Automixing 技术，在 30 万亿 token 规模的预训练中优化数据组成

- **优势**：将数据配比从经验调参转变为数据驱动的自动化过程，适用于大规模预训练

## 来源引用

- [摘要：Today we're releasing Laguna XS.2, Poolside's first open-weight model.](summaries/摘要：Today we're releasing Laguna XS.2, Poolside's first open-weight model.md)（[原文](https://x.com/poolsideai/status/2049144111626670282)）

## 关联概念

- [Laguna XS.2](entities/Laguna XS.2.md)

- [Poolside](entities/Poolside.md)

- [Agent RL](concepts/Agent RL.md)

- [Shimmer](entities/Shimmer.md)
