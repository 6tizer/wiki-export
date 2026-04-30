---
title: Reference Gap
type: concept
tags:
- 多模态
- 推理优化
status: 草稿
confidence: high
last_compiled: '2026-04-30'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/ec969da5b96d4b13bb75e400e685c2ac
notion_id: ec969da5-b96d-4b13-bb75-e400e685c2ac
---

## 定义

Reference Gap（引用差距）是 DeepSeek 论文《Thinking with Visual Primitives》中提出的概念，指多模态模型在推理过程中，自然语言无法精确指代视觉空间中具体物体或位置的能力缺口。

与 Perception Gap（感知差距，即「看不见」）不同，Reference Gap 描述的是「看得见但指不准」的问题。

## 关键要点

- 自然语言天然是模糊的指代工具，「左边那只白狗」在连续视觉空间中无法精确锚定

- 当 CoT 推理链变长时，语言会逐渐失去对视觉实体的追踪，导致幻觉

- 在密集计数、多步空间推断、拓扑导航等任务上，Reference Gap 是主要瓶颈

- 解决方案：在思维链中嵌入坐标 token（Visual Primitives），让模型一边「指」一边「想」

## 与 Perception Gap 的区别

- **Perception Gap**：模型看不清细节 → 通过高分辨率裁剪、动态 patch 解决

- **Reference Gap**：模型看得清但无法精确引用 → 通过 Visual Primitives 解决

## 关联概念

- Visual Primitives

- Perception Gap

## 来源引用

- [摘要：刚刚，DeepSeek最新成果，节前发布！](summaries/摘要：刚刚，DeepSeek最新成果，节前发布！.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzIyNjM2MzQyNg%3D%3D&mid=2247722411&idx=1&sn=bdec00adace587c9737956cd7554bdb4&chksm=e900cea0128d25e4398f9e439ce550cf8de63aabb709f43fd4040baeceb7cd184cf5104f51f7#rd)）
