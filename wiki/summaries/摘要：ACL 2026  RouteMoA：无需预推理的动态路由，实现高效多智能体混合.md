---
title: 摘要：ACL 2026 | RouteMoA：无需预推理的动态路由，实现高效多智能体混合
type: summary
tags:
- 推理优化
- 多Agent协作
status: 已审核
confidence: high
last_compiled: '2026-05-02'
source_tags: ''
source_article_url: https://www.notion.so/354701074b688168aa91fbb6b867cd4e
notion_url: https://www.notion.so/Tizer/406aef54f8804babaaf27f8329b86c54
notion_id: 406aef54-f880-4bab-aaf2-7f8329b86c54
---

## 一句话摘要

RouteMoA 通过将多模型协作中的模型选择从「后验判断」前移到「先验预测 + 轻量修正」，在 15 模型池中实现成本降低 89.8%、延迟降低 63.6% 的同时保持甚至提升准确率。

## 关键洞察

- **效率瓶颈在全量推理而非融合**：现有 MoA 和 Sparse MoA 都需要所有模型先推理一遍才能决定选谁，选之前已经太贵了

- **先验预测可行**：轻量级 scorer 仅根据 query 即可预测模型表现，Top-3 命中率接近 98%，说明不需要看所有答案也能选对模型

- **Mixture-of-Judges 实现低成本纠错**：通过 self-assessment 和 cross-assessment 基于已有输出做后验修正，不引入额外推理调用

- **多模型系统本质是稀疏的**：大多数 query 上真正关键的模型只占少数，关键是别漏掉对的模型

- **失败瓶颈转移**：超过 50% 的错误来自 Aggregation Drift（聚合漂移），而非模型选择错误，暗示未来研究方向应关注聚合策略优化

## 提取的概念

- [RouteMoA](entities/RouteMoA.md)：本文提出的高效 MoA 框架（entity）

- [Mixture-of-Agents](concepts/Mixture-of-Agents.md)：多模型并行生成、逐层融合的协作架构范式

- [Mixture-of-Judges](concepts/Mixture-of-Judges.md)：RouteMoA 中的轻量级后验评审机制

- [Aggregation Drift](concepts/Aggregation Drift.md)：多模型融合阶段的失败模式

- [模型路由](concepts/模型路由.md)：根据任务特征将请求分配给不同模型的调度策略（已有概念）

## 原始文章信息

- **作者**：机器之心

- **来源**：微信公众号

- **发布时间**：2026-05-02

- **原文链接**：[微信文章](https://mp.weixin.qq.com/s?__biz=MzA3MzI4MjgzMw%3D%3D&mid=2651031297&idx=2&sn=6249a28de4fdf4debab54dbc8eb7bc8c&chksm=85f146469ec1be7ded1742857bf2ce206c251d0b8c485e70ff50b670f8a815337b8c573e2931#rd)

- **论文**：[arxiv.org/abs/2601.18130](http://arxiv.org/abs/2601.18130)

- **代码**：[github.com/Jize-W/RouteMoA](http://github.com/Jize-W/RouteMoA)

## 个人评注

RouteMoA 的核心思路——「先判断谁值得参与，再让它们协作」——与 OpenClaw 的 Agent 调度思路有直接映射关系。在 content pipeline 中，不同 Agent/模型各有所长（如摘要、翻译、分类），如果每次都全量调用所有模型再筛选，成本会随 Agent 池规模线性增长。RouteMoA 的先验 scorer 思路可以作为 HITL 系统中模型选择的参考：用轻量级信号（如 query 类型、历史表现）预判最优模型，而非盲目并行。同时，Aggregation Drift 的发现也提醒我们，在多 Agent 输出合并时需要更精细的融合策略，而不仅仅是简单的投票或拼接。
