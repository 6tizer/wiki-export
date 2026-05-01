---
title: 摘要：Mythos is a looped transformer!? 😳 Should be a Mixture-of-Recursions (MoR)
  — 2× faster, controlled effort.
type: summary
tags:
- 推理优化
- 训练/微调
status: 已审核
confidence: medium
last_compiled: '2026-04-20'
source_tags: ''
source_article_url: https://www.notion.so/348701074b6881d6a03dfdea0760a61c
notion_url: https://www.notion.so/Tizer/59811fb9aef948ddb9d1ebb46c5e06d4
notion_id: 59811fb9-aef9-48dd-b9d1-ebb46c5e06d4
---

## 一句话摘要

这篇线程把 Mythos 所体现的循环式 Transformer 放进递归模型的发展脉络里，核心主张是用 **Mixture-of-Recursions（MoR）** 为不同 token 分配不同递归深度，把固定循环升级为可控计算量的稀疏架构。

## 关键洞察

- 作者把 **Dense → Sparse MoE** 的效率跃迁类比到 **Uniform Loops → MoR**，强调递归模型也需要从“平均算力”走向“按需算力”。

- **Looped Transformer** 的价值不只是参数共享，更在于把迭代过程本身变成推理归纳偏置，让模型可以“多想几步”。

- **MoR** 通过轻量路由器让简单 token 提前退出、困难 token 继续递归，从而在相近质量下提升吞吐并减少无效计算。

- 线程串起 **Universal Transformers、latent reasoning、pause tokens、Coconut、Ouro** 等工作，说明“潜空间思考 + 动态深度”正在形成一条连续的研究路线。

- 真正的工程难点不只在速度提升，还在于 **递归深度学习、停止条件与路由稳定性** 的训练和推理表现。

## 提取的概念

- [Mixture-of-Recursions](concepts/Mixture-of-Recursions.md)

- [Looped Transformer](concepts/Looped Transformer.md)

- [Latent Reasoning](concepts/Latent Reasoning.md)

- [Adaptive Token Routing](concepts/Adaptive Token Routing.md)

- [Universal Transformer](concepts/Universal Transformer.md)

## 原始文章信息

- 作者：@reza_byt

- 来源：X书签

- 发布时间：2026-04-17

- 原文链接：[https://x.com/reza_byt/status/2045168844658950392](https://x.com/reza_byt/status/2045168844658950392)

## 个人评注

- 对 Tizer 的启发是：知识编译和 Agent 工作流也可以借鉴这种“按难度分配算力”的思路，把有限预算优先给高复杂度任务，而不是对所有输入一视同仁。
