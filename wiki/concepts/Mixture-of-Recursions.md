---
title: Mixture-of-Recursions
type: concept
tags:
- LLM
status: 审核中
confidence: high
last_compiled: '2026-04-20'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/ca995efb6794436a988c199fbe11925b
notion_id: ca995efb-6794-436a-988c-199fbe11925b
---

## 定义

**Mixture-of-Recursions（MoR）** 是一种递归式 Transformer 架构，在共享参数的循环计算基础上加入轻量路由机制，为不同 token 动态分配不同递归深度，从而实现按需计算。

## 关键要点

- 它把参数共享与自适应计算放进同一套框架里。

- 简单 token 可以提前退出，复杂 token 可以继续递归，从而减少平均计算量。

- 相比固定循环深度，MoR 更强调 token 级别的算力调度与吞吐效率。

- 这类设计可视为递归模型世界里从“稠密计算”走向“稀疏计算”的一次升级。

## 来源引用

- [摘要：Mythos is a looped transformer!? 😳 Should be a Mixture-of-Recursions (MoR) — 2× faster, controlled effort.](summaries/摘要：Mythos is a looped transformer! 😳 Should be a Mixture-of-Recursions (MoR) — 2× faster, controlled effort.md)

## 关联概念

- [Looped Transformer](concepts/Looped Transformer.md)

- [Latent Reasoning](concepts/Latent Reasoning.md)

- [Adaptive Token Routing](concepts/Adaptive Token Routing.md)

- [Universal Transformer](concepts/Universal Transformer.md)

## 备注

- 适合放入 LLM 架构演化脉络中，与 Looped Transformer、Latent Reasoning 一起理解。
