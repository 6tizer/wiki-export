---
title: Adaptive Token Routing
type: concept
tags:
- 推理优化
- 链上协议
status: 审核中
confidence: medium
last_compiled: '2026-04-20'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/b64b45a27d7e4889b5cc51dd485e1a8f
notion_id: b64b45a2-7d7e-4889-b5cc-51dd485e1a8f
---

## 定义

**Adaptive Token Routing** 是一种按 token 难度或状态动态分配计算路径的机制，让不同 token 接受不同深度、不同专家或不同递归次数的处理。

## 关键要点

- 它的目标是避免所有 token 消耗同样多的算力。

- 在 MoR 里，这种路由体现为决定 token 继续递归还是提前退出。

- 该机制直接影响推理效率、停止条件与训练稳定性。

- 它把“受控 effort”从口号变成可执行的架构策略。

## 来源引用

- [摘要：Mythos is a looped transformer!? 😳 Should be a Mixture-of-Recursions (MoR) — 2× faster, controlled effort.](summaries/摘要：Mythos is a looped transformer! 😳 Should be a Mixture-of-Recursions (MoR) — 2× faster, controlled effort.md)

## 关联概念

- [Mixture-of-Recursions](concepts/Mixture-of-Recursions.md)

- [Looped Transformer](concepts/Looped Transformer.md)

- [Latent Reasoning](concepts/Latent Reasoning.md)

- [Universal Transformer](concepts/Universal Transformer.md)

## 备注

- 这是把固定深度模型改造成弹性算力模型的关键组件。
