---
title: 摘要：10M参数也能跑ARC与数独，Bengio团队押注「多轨迹推理」
type: summary
tags:
- 推理优化
- 训练/微调
status: 已审核
confidence: high
last_compiled: '2026-05-22'
source_tags: ''
source_article_url: https://www.notion.so/368701074b68817c9585f2f408ee6e42
notion_url: https://www.notion.so/Tizer/001ec638399e4aa79a5922d78d6160ce
notion_id: 001ec638-399e-4aa7-9a59-22d78d6160ce
---

## 一句话摘要

[GRAM](concepts/GRAM.md) 将传统递归推理模型从确定性单轨迹更新改造为概率多轨迹采样过程，仅用 10M 参数在 Sudoku-Extreme（97.0%）、N-Queens（99.7%）、ARC-AGI 等任务中超越大模型零样本表现，展示了「宽度扩展」替代「深度扩展」的推理时计算新范式。

## 关键洞察

- GRAM 的核心机制是 [随机引导](concepts/随机引导.md)：每次高层隐状态转移时，向确定性候选注入依赖当前状态的高斯扰动，均值引导方向、方差控制探索——消融实验显示两者缺一不可：仅保留随机 → 50.27%，仅保留引导 → 0.0%

- [多轨迹推理](concepts/多轨迹推理.md) 将推理时计算从「深度扩展」拓展到「宽度扩展」：16 次迭代 × 20 条并行轨迹就能超过确定性模型的 320 次迭代（90.5% → 97.0%）

- [推理时计算扩展](concepts/推理时计算扩展.md) 的两种策略（深度 vs 宽度）互补：数据增强较强时，增加采样数的边际收益趋于饱和，说明数据增强和推理时采样承担不同角色

- GRAM 同时具备条件推理和无条件生成能力：在数独生成任务中，10.9M 参数用 16 步达到 99.05% 有效率，远超 55M 参数扩散模型 1000 步的 91.33%

- 训练采用 [深度监督](concepts/深度监督.md) 与 [截断梯度传播](concepts/截断梯度传播.md) 结合的有偏近似方法，论文也承认这限制了 GRAM 向更大基础模型扩展的速度

## 提取的概念

- [GRAM](concepts/GRAM.md)

- [多轨迹推理](concepts/多轨迹推理.md)

- [推理时计算扩展](concepts/推理时计算扩展.md)

- [随机引导](concepts/随机引导.md)

- [截断梯度传播](concepts/截断梯度传播.md)

- [深度监督](concepts/深度监督.md)

## 原始文章信息

- **作者**：PaperWeekly

- **来源**：微信

- **发布时间**：2026-05-22

- **原文链接**：[https://mp.weixin.qq.com/s?__biz=MzIwMTc4ODE0Mw==&mid=2247720447&idx=1&sn=da4ef5443c5505210f780251e893d488&chksm=9762df2a6aefb0d9bed05dc587b9abce39e573e094c876354f67e008cf28e5ad947df9f9f4a7#rd](https://mp.weixin.qq.com/s?__biz=MzIwMTc4ODE0Mw%3D%3D&mid=2247720447&idx=1&sn=da4ef5443c5505210f780251e893d488&chksm=9762df2a6aefb0d9bed05dc587b9abce39e573e094c876354f67e008cf28e5ad947df9f9f4a7#rd)

- **论文**：[http://arxiv.org/abs/2605.19376](http://arxiv.org/abs/2605.19376)

## 个人评注

GRAM 的「多轨迹推理」思路对 HITL/AI Agent 工作流有启发意义。在 OpenClaw 等 Agent 框架中，单次推理可能陷入局部最优或约束冲突，多轨迹采样 + 奖励模型择优的模式可以类比为 Agent 的「推理时搜索」。另外，10M 参数级别的轻量模型在受控推理任务中击败大模型 zero-shot 的结果，也提示了「小模型 + 推理时计算」路线在结构化任务中的潜力。
