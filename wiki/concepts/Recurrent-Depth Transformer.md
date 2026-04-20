---
title: Recurrent-Depth Transformer
type: concept
tags:
- LLM
status: 草稿
confidence: high
last_compiled: '2026-04-20'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/0f221fd4a663429e9ade667689cee399
notion_id: 0f221fd4-a663-429e-9ade-667689cee399
---

## 定义

Recurrent-Depth Transformer 是一种在同一组 Transformer 层上重复执行计算的架构，用循环计算替代单纯堆叠更多独立层，从而在不显著增加参数的前提下提升推理深度。

## 关键要点

- 核心思想是“参数复用 + 多轮迭代计算”。

- 它特别适合需要多步组合、逐步 refinement 的任务。

- 这类架构把“推理深度”部分转移到循环次数上，而不完全依赖模型规模。

- 推理时可通过增加循环次数提升处理更深链式问题的能力。

## 关联概念

- [OpenMythos](entities/OpenMythos.md)

- [Claude Mythos](entities/Claude Mythos.md)

- [MoE 架构](concepts/MoE 架构.md)

- [隐式思维链](concepts/隐式思维链.md)

## 来源引用

- [摘要：OpenMythos：社区用开源代码重建 Claude Mythos 的循环深度 Transformer 假说](summaries/摘要：OpenMythos：社区用开源代码重建 Claude Mythos 的循环深度 Transformer 假说.md)（[原文](https://x.com/KyeGomezB/status/2045659150340723107)）

- [摘要：Loop, Think, & Generalize：循环深度 Transformer 的隐式推理](summaries/摘要：Loop, Think, & Generalize：循环深度 Transformer 的隐式推理.md)（[原文](https://x.com/yuekun_yao/status/2044229171627639004)）
