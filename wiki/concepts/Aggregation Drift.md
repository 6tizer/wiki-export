---
title: Aggregation Drift
type: concept
tags:
- 多Agent协作
status: 草稿
confidence: medium
last_compiled: '2026-05-02'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/1c649797e41146ac8c4b06944cb9ecd2
notion_id: 1c649797-e411-46ac-8c4b-06944cb9ecd2
---

## 定义

Aggregation Drift（聚合漂移）是多模型协作系统中的一种失败模式，指在将多个模型输出融合为最终答案的过程中，正确信号被稀释或偏移，导致最终答案出错。

## 关键要点

- 在 RouteMoA 的失败案例分析中，超过 50% 的错误来自 Aggregation Drift

- 因模型选择错误导致的失败比例远低于聚合阶段的失败

- 说明多模型系统的瓶颈正在从「选谁来回答」转向「如何整合多个答案」

- 这一发现暗示未来研究方向应更关注聚合策略的优化

## 关联概念

- [RouteMoA](entities/RouteMoA.md)

- [Mixture-of-Agents](concepts/Mixture-of-Agents.md)

- [Mixture-of-Judges](concepts/Mixture-of-Judges.md)

- [模型路由](concepts/模型路由.md)

## 来源引用

- [摘要：ACL 2026 | RouteMoA：无需预推理的动态路由，实现高效多智能体混合](summaries/摘要：ACL 2026  RouteMoA：无需预推理的动态路由，实现高效多智能体混合.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzA3MzI4MjgzMw%3D%3D&mid=2651031297&idx=2&sn=6249a28de4fdf4debab54dbc8eb7bc8c&chksm=85f146469ec1be7ded1742857bf2ce206c251d0b8c485e70ff50b670f8a815337b8c573e2931#rd)）
