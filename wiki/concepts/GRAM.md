---
title: GRAM
type: concept
tags:
- 推理优化
status: 草稿
confidence: ''
last_compiled: '2026-05-22'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/604de84ef49e480a817b15e02b21b155
notion_id: 604de84e-f49e-480a-817b-15e02b21b155
---

## 定义

GRAM（Generative Recursive Reasoning Model，生成式递归推理模型）是由 Yoshua Bengio 团队与 KAIST、Mila、NYU 联合提出的轻量级递归推理架构。其核心创新在于将传统递归模型的确定性隐状态更新改造为概率多轨迹采样过程，使推理不再依赖单一路径，而是通过并行采样多条候选轨迹并择优输出。在 Sudoku-Extreme（97.0%）、N-Queens（99.7%）、ARC-AGI 等结构化推理任务中，仅用 10M 参数即取得显著表现。

## 关键要点

- **双层隐状态解耦**：将隐状态分为高层 h（抽象推理状态）和低层 l（细粒度中间计算），承担不同时间尺度的计算任务

- **高斯扰动注入**：在高层状态确定性候选值上叠加依赖当前状态的高斯噪声，均值引导推理方向，方差控制探索幅度

- **随机性仅加在高层**：作者尝试过向低层注入噪声但无性能提升

- **并行多轨迹采样**：推理时并行采样 N 条轨迹（如 N=20），通过隐过程奖励模型或多数投票选择最优输出

- **截断梯度传播训练**：采用有偏但显存高效的近似训练方法

- **双重能力**：可同时用于条件推理和无条件生成（如数独生成有效率 99.05%）

## 来源引用

- [摘要：10M参数也能跑ARC与数独，Bengio团队押注「多轨迹推理」](summaries/摘要：10M参数也能跑ARC与数独，Bengio团队押注「多轨迹推理」.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzIwMTc4ODE0Mw%3D%3D&mid=2247720447&idx=1&sn=da4ef5443c5505210f780251e893d488&chksm=9762df2a6aefb0d9bed05dc587b9abce39e573e094c876354f67e008cf28e5ad947df9f9f4a7#rd)）
