---
title: 可插拔世界模型架构（WA）
type: concept
tags:
- LLM
status: 审核中
confidence: high
last_compiled: '2026-04-23'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/6870a402c1ca4ee28b3479e6d8f14940
notion_id: 6870a402-c1ca-4ee2-8b34-79e6d8f14940
---

## 定义

可插拔世界模型架构（WA）是 AlphaBrain Platform 中用于统一接入不同世界模型 Backbone 的架构设计，使同一套动作解码和实验流程能够在多种世界模型之间切换与比较。

## 关键要点

- 它的核心价值是把世界模型从单一实现变成可替换组件，方便横向评估不同路线。

- 文中提到该架构可接入 V-JEPA、Cosmos Predict、Wan 等不同世界模型 Backbone。

- 统一动作解码器与配置入口，让开发者更容易复现、比较并迁移实验。

- 它体现的是工程化平台思路，而不是只追求某一个世界模型的最佳单点性能。

## 来源引用

- [摘要：特斯拉开源硬件，中国公司回应来了：直接把机器人大脑开源了](summaries/摘要：特斯拉开源硬件，中国公司回应来了：直接把机器人大脑开源了.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzIzNjc1NzUzMw%3D%3D&mid=2247885437&idx=1&sn=6a4c424526417657d528b8bfa9d0c200&chksm=e9963f58459d6d389133ac94bd91c6f2c51c8c7cc4fba208ced0e1d73052dc4d5db0a7661e16#rd)）

## 关联概念

- [AlphaBrain Platform](entities/AlphaBrain Platform.md)

- [NeuroVLA](entities/NeuroVLA.md)

- [RL Token](concepts/RL Token.md)

- [智平方](entities/智平方.md)
