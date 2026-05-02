---
title: RouteMoA
type: entity
tags:
- 推理优化
- 多Agent协作
status: 草稿
confidence: high
last_compiled: '2026-05-02'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/6d3a5b0b17dd4571a61c220b5bb6e726
notion_id: 6d3a5b0b-17dd-4571-a61c-220b5bb6e726
---

## 定义

RouteMoA 是上海交通大学 IWIN 团队提出的高效多智能体混合（Mixture-of-Agents）框架，被 ACL 2026 接收。其核心创新是将模型选择从「后验判断」前移到「先验预测 + 轻量修正」，通过推理前进行模型能力预测，避免对所有模型进行无效推理，从而在保持甚至提升性能的同时大幅降低成本和延迟。

别名：Route-MoA

## 关键要点

- **先验筛选**：引入轻量级 scorer，仅根据用户 query 预测每个模型的潜在表现，无需调用大模型推理即可缩小模型池

- **后验修正**：通过 Mixture-of-Judges 机制（self-assessment + cross-assessment）基于已有输出做低成本评审

- **多目标优化**：综合考虑输出质量、token 成本、推理延迟进行模型选择

- 实验结果：在 15 模型池中，成本降低 89.8%，延迟降低 63.6%，准确率相对 MoA/SMoA 有所提升

- Scorer 在 Top-3 内命中正确模型的概率接近 98%

## 档案信息

- **团队**：上海交通大学 IWIN 中心（关新平教授团队）

- **合作方**：南洋理工大学、腾讯、上海人工智能实验室、香港中文大学

- **第一作者**：王骥泽（上海交通大学博士生）

- **论文**：[arxiv.org/abs/2601.18130](http://arxiv.org/abs/2601.18130)

- **代码**：[github.com/Jize-W/RouteMoA](http://github.com/Jize-W/RouteMoA)

- **发表**：ACL 2026

## 关联概念

- [Mixture-of-Agents](concepts/Mixture-of-Agents.md)

- [Mixture-of-Judges](concepts/Mixture-of-Judges.md)

- [Aggregation Drift](concepts/Aggregation Drift.md)

- [模型路由](concepts/模型路由.md)

## 来源引用

- [摘要：ACL 2026 | RouteMoA：无需预推理的动态路由，实现高效多智能体混合](summaries/摘要：ACL 2026  RouteMoA：无需预推理的动态路由，实现高效多智能体混合.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzA3MzI4MjgzMw%3D%3D&mid=2651031297&idx=2&sn=6249a28de4fdf4debab54dbc8eb7bc8c&chksm=85f146469ec1be7ded1742857bf2ce206c251d0b8c485e70ff50b670f8a815337b8c573e2931#rd)）
