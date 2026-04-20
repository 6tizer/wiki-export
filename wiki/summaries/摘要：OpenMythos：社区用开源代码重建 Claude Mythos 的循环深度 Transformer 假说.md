---
title: 摘要：OpenMythos：社区用开源代码重建 Claude Mythos 的循环深度 Transformer 假说
type: summary
tags:
- LLM
- 开发工具
status: 已审核
confidence: high
last_compiled: '2026-04-20'
source_tags: LLM, Claude, 开源
source_article_url: https://www.notion.so/348701074b688177a655e838e2f7a1ce
notion_url: https://www.notion.so/fd3e0669b6df4647b00b878ada9cf9c2
notion_id: fd3e0669-b6df-4647-b00b-878ada9cf9c2
---

## 一句话摘要

OpenMythos 以可运行的开源工程形式，提出了“Claude Mythos 可能采用循环深度 Transformer + MoE”的具体架构假说，并把循环推理的研究方向转化为开发者可复现的实验对象。

## 关键洞察

- 用 Prelude → Recurrent Block → Coda 的三段式结构，把“深度”从固定层数改为推理时的循环次数。

- 循环块每轮都重新注入原始输入，缓解多轮递归中的信息漂移问题。

- 在循环块中结合 MoE，让模型以较少激活参数获得更高的单位算力产出。

- 通过连续负对角矩阵与谱半径约束增强训练稳定性，降低循环模型发散风险。

- 即便 Mythos 真相未明，OpenMythos 仍把“测试时计算扩展 + 隐式思维链”的设计空间带入了开源社区视野。

## 提取的概念

- [OpenMythos](entities/OpenMythos.md)

- [Claude Mythos](entities/Claude Mythos.md)

- [Recurrent-Depth Transformer](concepts/Recurrent-Depth Transformer.md)

- [MoE 架构](concepts/MoE 架构.md)

- [隐式思维链](concepts/隐式思维链.md)

## 原始文章信息

- 作者：@KyeGomezB

- 来源：X书签

- 发布时间：2026-04-19

- 原文链接：[https://x.com/KyeGomezB/status/2045659150340723107](https://x.com/KyeGomezB/status/2045659150340723107)

- 源文章页面：OpenMythos：社区用开源代码重建 Claude Mythos 的循环深度 Transformer 假说

## 个人评注

这类“可运行的假说”对 Tizer 的内容流水线很有价值：一方面它能把前沿模型研究拆成可沉淀的 Wiki 概念节点，另一方面也适合用作后续 HITL 评审的素材来源。对于 OpenClaw 或其他 Agent 系统而言，循环推理、测试时计算扩展与隐式思维链，也都是值得持续追踪的上游能力方向。
