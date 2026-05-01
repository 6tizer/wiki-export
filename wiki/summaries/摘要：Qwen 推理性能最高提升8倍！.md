---
title: 摘要：Qwen 推理性能最高提升8倍！
type: summary
tags: []
status: 已审核
confidence: medium
last_compiled: '2026-04-15'
source_tags: ''
source_article_url: https://www.notion.so/343701074b6881489e0efe23aa0b0549
notion_url: https://www.notion.so/Tizer/8ae16cecdb7d4511bea340774e8cfb6f
notion_id: 8ae16cec-db7d-4511-bea3-40774e8cfb6f
---

## 一句话摘要

DDTree 在 DFlash 与 speculative decoding 的基础上，把单链草稿扩展为可一次性验证的树状草稿结构，从而让 Qwen3-30B-MoE 在 HumanEvalT 上实现最高 8.22 倍推理加速。

## 关键洞察

- DDTree 的核心改进是把单链 draft 改成树状 draft，减少分叉点候选被浪费的问题

- target model 借助 Tree Attention 一次验证整棵草稿树，不再只做线性逐段确认

- 它延续了 speculative decoding 的“草稿模型 + 验证模型”思路，但把草稿生成升级为 block diffusion + 多分支树搜索

- 帖子中给出的代表性结果是 Qwen3-30B-MoE 在 HumanEvalT 上最高 8.22 倍加速，但回复里也提醒真实收益会受命中率、batch size 和任务类型影响

## 提取的概念

- [DDTree](concepts/DDTree.md)

- [DFlash](concepts/DFlash.md)

- [Speculative Decoding](concepts/Speculative Decoding.md)

- [Tree Attention](concepts/Tree Attention.md)

- [Block Diffusion](concepts/Block Diffusion.md)

## 原始文章信息

- 作者：@nash_su

- 来源：X书签

- 发布时间：2026-04-14

- 原文链接：[https://x.com/nash_su/status/2043924682802712600](https://x.com/nash_su/status/2043924682802712600)

- 项目页：[DDTree](https://liranringel.github.io/ddtree/)

## 个人评注

这类工作对 Tizer 的价值不在于单纯追求 benchmark 数字，而在于提示一条更实际的内容方向：把推理优化、模型结构和工程部署串成可复用知识卡片。后续如果 Tizer 在本地部署、Coding Agent 或高频工作流里持续跟踪推理加速路线，DDTree 可以作为 speculative decoding 演进链条中的一个关键节点。
