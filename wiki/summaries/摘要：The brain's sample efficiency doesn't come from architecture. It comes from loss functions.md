---
title: 摘要：The brain's sample efficiency doesn't come from architecture. It comes from
  loss functions.
type: summary
tags:
- 训练/微调
- 模型评测
- Harness 工程
status: 已审核
confidence: medium
last_compiled: '2026-04-29'
source_tags: ''
source_article_url: https://www.notion.so/351701074b6881369b52f6a5f642ce4b
notion_url: https://www.notion.so/Tizer/7ff1637e288744f7bdddc1253fbd3a61
notion_id: 7ff1637e-2887-44f7-bddd-c1253fbd3a61
---

## 一句话摘要

大脑的样本效率优势不在于架构，而在于皮质下结构编码的丰富损失函数/奖励信号——AI Agent 同样可以通过多轴评估而非单一 pass/fail 来提升学习效率。

## 关键洞察

- **损失函数 > 架构**：人类大脑的样本效率来源于皮质下结构编码的多维度评估信号，而非皮层架构本身

- **基因组高效编码**：人类基因组仅约 3GB，却能编码高效学习者——复杂损失函数可能只需几百行代码表达

- **进化的课程学习**：婴儿的「9 个月训练」实际上是 5 亿年进化课程的延续，进化同时优化了架构和奖励塑形

- **Fat Skill 假说**：Garry Tan 在 gstack /review 上实验——拥有 fat、multi-axis 评估技能的 Agent 是否能比更大模型 + thin 反馈收敛更快

- **奖励信号密度瓶颈**：token 级反馈每步约 1 个信号，而大脑每秒处理数百万个多维度信号，这个差距比架构差异更关键

## 提取的概念

- [样本效率](concepts/样本效率.md)

- [多轴评估](concepts/多轴评估.md)

- [奖励函数设计](concepts/奖励函数设计.md)

- [gstack](entities/gstack.md)

## 原始文章信息

- **作者**：@garrytan（Garry Tan）

- **来源**：X 书签

- **发布时间**：2026-04-29

- **链接**：[原文推文](https://x.com/garrytan/status/2049485192411377759)

- **引用推文**：@dwarkesh_sp（Dwarkesh Patel）采访 Adam Marblestone 关于大脑样本效率的讨论

## 个人评注

这篇讨论直接关联 OpenClaw 的 skill 设计哲学。Garry Tan 的「fat skill vs thin feedback」假说与 Tizer 工作流中的 Harness 工程理念高度一致——skill/harness 层的评估质量比底层模型能力更重要。如果多轴评估确实能压缩搜索空间，那么为 OpenClaw 的 coding agent 设计更丰富的 review skill（不只是 test pass/fail，而是代码风格、性能、边界覆盖等多维度打分）可能是比换更大模型更高效的投入方向。
