---
title: Mixture-of-Agents
type: concept
tags:
- 多Agent协作
status: 草稿
confidence: high
last_compiled: '2026-05-02'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/c183d9333b834410a46a997cd38722f1
notion_id: c183d933-3b83-4410-a46a-997cd38722f1
---

## 定义

Mixture-of-Agents（MoA）是一种多大语言模型协作架构范式，通过让多个模型并行生成、逐层交互、反复融合来获得比单一模型更强的结果。核心思想是利用不同模型的互补优势（如数学、代码、医学等专长）实现集体智能。

别名：MoA

## 关键要点

- 多个 LLM 并行生成响应，再通过聚合层融合为最终答案

- 标准 MoA 每层调用所有模型，成本和延迟随模型数量线性增长

- Sparse MoA 在全量推理后通过评审筛选，但仍需所有模型先推理一遍

- 关键瓶颈在于「全量推理」而非「融合」——选模型之前已经太贵

- 多模型系统的本质是稀疏的：大多数 query 上真正关键的模型只占少数

## 变体

- **标准 MoA**：全量推理 → 融合

- **Sparse MoA (SMoA)**：全量推理 → 评审筛选 → 融合

- **RouteMoA**：先验预测 → 选择性推理 → 轻量修正 → 融合

## 关联概念

- [RouteMoA](entities/RouteMoA.md)

- [Mixture-of-Judges](concepts/Mixture-of-Judges.md)

- [Aggregation Drift](concepts/Aggregation Drift.md)

- [模型路由](concepts/模型路由.md)

## 来源引用

- [摘要：ACL 2026 | RouteMoA：无需预推理的动态路由，实现高效多智能体混合](summaries/摘要：ACL 2026  RouteMoA：无需预推理的动态路由，实现高效多智能体混合.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzA3MzI4MjgzMw%3D%3D&mid=2651031297&idx=2&sn=6249a28de4fdf4debab54dbc8eb7bc8c&chksm=85f146469ec1be7ded1742857bf2ce206c251d0b8c485e70ff50b670f8a815337b8c573e2931#rd)）
