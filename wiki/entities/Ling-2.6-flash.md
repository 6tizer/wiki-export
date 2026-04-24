---
title: Ling-2.6-flash
type: entity
tags:
- LLM
status: 审核中
confidence: medium
last_compiled: '2026-04-24'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/51cc8c9db6054aafa1c319956cdb774b
notion_id: 51cc8c9d-b605-4aaf-a1c3-19956cdb774b
---

## 定义

Ling-2.6-flash 是蚂蚁集团 AGI 团队推出的执行型大模型，早期曾以 Elephant / Elephant Alpha 的匿名身份在 OpenRouter 上盲测，主打高 token 效率、低延迟，以及面向轻量级 Agent 场景的高频交互能力。

## 关键要点

- 支持 256k 上下文和 32k 输出

- 采用 104B 总参数、7.4B 激活参数的 MoE 路线，强调执行层的低成本高吞吐

- 适合代码补全、调试、长文档处理和轻量级 Agent 交互

- 文章作者将其定位为“规划层之外的执行层模型”，适合承接高频、可拆解、低风险任务

- 其匿名测试期的 Elephant / Elephant Alpha 身份，现已被指向蚂蚁集团 AGI 团队的 Ling-2.6-flash

## 关联概念

- [MoE 架构](concepts/MoE 架构.md)

- [线性注意力](concepts/线性注意力.md)

- [Multi-Token Prediction](concepts/Multi-Token Prediction.md)

## 来源引用

- [摘要：匿名模型“大象”搅局OpenRouter：100B参数冲到热榜第一，实测结果如何](summaries/摘要：匿名模型“大象”搅局OpenRouter：100B参数冲到热榜第一，实测结果如何.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzA4MTQ4NjQzMw%3D%3D&mid=2652801118&idx=1&sn=f40df183d831b17f5f8dcc100fb9c9a3&chksm=85f152316f89ca9f6eaec156d55adaa7df30ec97ff2d436b45e2f918da524206b3b000e6dc21#rd)）

- [摘要：后续来了兄弟们，卧槽真的太炸了，同样的任务，同样的配置，速度比Claude Sonnet 4.6还快 6 倍，成本低约 50 倍，](summaries/摘要：后续来了兄弟们，卧槽真的太炸了，同样的任务，同样的配置，速度比Claude Sonnet 4.6还快 6 倍，成本低约 50 倍，.md)（[原文](https://x.com/AYi_AInotes/status/2047364394229850188)）
