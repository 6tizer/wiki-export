---
title: Visual Primitives
type: concept
tags:
- 多模态
- 推理优化
status: 草稿
confidence: high
last_compiled: '2026-04-30'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/bcfe0552cb2d414d8cc3a17976023631
notion_id: bcfe0552-cb2d-414d-8cc3-a17976023631
---

## 定义

Visual Primitives（视觉原语）是 DeepSeek 在论文《Thinking with Visual Primitives》中提出的概念，指在多模态模型的思维链（CoT）推理过程中嵌入的坐标标记 token，作为「思考的最小单位」。

包含两种原语：

- **Bounding Box**：用于锚定物体位置，格式为 `<|ref|>object<|/ref|><|box|>[[x1,y1,x2,y2]]<|/box|>`

- **Point**：用于描述轨迹和路径，格式为 `<|point|>[[x1,y1],[x2,y2]]<|/point|>`

## 关键要点

- 灵感来自人类行为：数密集物体时用手指点，走迷宫时目光在交叉口停顿

- 解决的核心问题是 Reference Gap（引用差距）——自然语言无法在连续视觉空间中精确锚定物体

- 在拓扑推理任务（迷宫导航、路径追踪）上大幅超越 GPT-5.4 等前沿模型

- 通过「先专家、再合并」的训练流程：分别训练 box 专家和 point 专家，再统一蒸馏

## 关联概念

- Reference Gap

- KV Cache 压缩

- GRPO

- On-Policy Distillation

## 来源引用

- [摘要：刚刚，DeepSeek最新成果，节前发布！](summaries/摘要：刚刚，DeepSeek最新成果，节前发布！.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzIyNjM2MzQyNg%3D%3D&mid=2247722411&idx=1&sn=bdec00adace587c9737956cd7554bdb4&chksm=e900cea0128d25e4398f9e439ce550cf8de63aabb709f43fd4040baeceb7cd184cf5104f51f7#rd)）
