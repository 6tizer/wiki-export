---
title: token效率
type: concept
tags:
- 推理优化
- 上下文管理
- Agent 协作模式
status: 审核中
confidence: medium
last_compiled: '2026-04-16'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/caf041a254eb407a8805b96c2c925a4c
notion_id: caf041a2-54eb-407a-8805-b96c2c925a4c
---

## 定义

token效率 是指模型在完成同类任务时，以更少 token 消耗达成目标输出的能力，直接影响调用成本、上下文预算和多轮 Agent 工作流的可持续性。

## 关键要点

- 同样任务下 token 消耗越低，成本和延迟压力通常越小

- 在多轮规划、工具调用和观察循环中，token效率 会被快速放大为工程成本差异

- 适合用于评估 to-C 场景、重复性任务和长链路 Agent 系统的模型选型

## 来源引用

- [原文链接](https://mp.weixin.qq.com/s?__biz=MzA4MTQ4NjQzMw%3D%3D&mid=2652801118&idx=1&sn=f40df183d831b17f5f8dcc100fb9c9a3&chksm=85f152316f89ca9f6eaec156d55adaa7df30ec97ff2d436b45e2f918da524206b3b000e6dc21#rd)｜《匿名模型“大象”搅局OpenRouter：100B参数冲到热榜第一，实测结果如何》｜源文章：匿名模型“大象”搅局OpenRouter：100B参数冲到热榜第一，实测结果如何
