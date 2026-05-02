---
title: Mixture-of-Judges
type: concept
tags:
- 模型评测
- 多Agent协作
status: 草稿
confidence: medium
last_compiled: '2026-05-02'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/40f112dd4b63438ca62d91366cd06ab2
notion_id: 40f112dd-4b63-438c-a62d-91366cd06ab2
---

## 定义

Mixture-of-Judges 是 RouteMoA 框架中提出的一种轻量级后验修正机制，用于在先验筛选之后对已生成的模型输出进行低成本评审和纠错，而不引入额外的推理调用。

## 关键要点

- 包含两种评估方式：

  - **Self-assessment**：模型对自己的答案打分

  - **Cross-assessment**：高质量模型评估其他模型的输出

- 所有评估仅基于已经生成的输出，不触发新的推理调用

- 作为先验筛选的补充，修正初筛误差

- 本质是用已有信息进行「纠错」而非「重算」

## 关联概念

- [RouteMoA](entities/RouteMoA.md)

- [Mixture-of-Agents](concepts/Mixture-of-Agents.md)

- [Aggregation Drift](concepts/Aggregation Drift.md)

- [模型路由](concepts/模型路由.md)

## 来源引用

- [摘要：ACL 2026 | RouteMoA：无需预推理的动态路由，实现高效多智能体混合](summaries/摘要：ACL 2026  RouteMoA：无需预推理的动态路由，实现高效多智能体混合.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzA3MzI4MjgzMw%3D%3D&mid=2651031297&idx=2&sn=6249a28de4fdf4debab54dbc8eb7bc8c&chksm=85f146469ec1be7ded1742857bf2ce206c251d0b8c485e70ff50b670f8a815337b8c573e2931#rd)）
