---
title: 摘要：DeepSeek不惜代价保住它！V4关键特性被挖出来了
type: summary
tags:
- 推理优化
- 训练/微调
status: 已审核
confidence: high
last_compiled: '2026-04-28'
source_tags: ''
source_article_url: https://www.notion.so/350701074b6881caaa28e6cc116ae578
notion_url: https://www.notion.so/Tizer/5a8fea3181f24552b07100e3bc857595
notion_id: 5a8fea31-81f2-4552-b071-00e3bc857595
---

## 一句话摘要

DeepSeek V4 为保留 Batch Invariance（批次不变性）这一核心工程约束，不惜牺牲 GPU 利用率和推理速度，通过 Dual-kernel 和自研 DeepGEMM 实现全流程逐比特可复现。

## 关键洞察

- **Batch Invariance 的定义**：同一 token 无论在批次中的位置、批次大小、与谁一起批处理，输出逐比特完全一致，是 DeepSeek V4 全链路可复现性的底座

- **四大工程价值**：线上推理结果稳定、预训练/后训练/推理三阶段对齐、复杂组件系统（MoE/稀疏注意力/FP4/FP8）的数值确定性底座、后训练（RL/蒸馏）稳定性

- **代价不小**：不能使用 split-KV 和 split-K 等常见 GPU 性能优化，导致 GPU 利用率下降、小批量速度降低、工程复杂度上升

- **两个关键解法**：attention 侧的 Dual-kernel（双 kernel 策略，保证不同负载场景下逐比特一致）和 GEMM 侧的 DeepGEMM（自研 kernel 库，替代 cuBLAS）

- **技术报告持续被深挖**：还包含 10+ 专家教师模型蒸馏为单一学生模型等亮点，每个问题背后都有坚实的数学解释

## 提取的概念

- [Batch Invariance](concepts/Batch Invariance.md)

- [DeepGEMM](entities/DeepGEMM.md)

- [Dual-kernel](concepts/Dual-kernel.md)

- [DeepSeek V4](entities/DeepSeek V4.md)

## 原始文章信息

- **作者**：鱼羊（量子位）

- **来源**：微信公众号 QbitAI

- **发布时间**：2026-04-28

- **链接**：[原文链接](https://mp.weixin.qq.com/s?__biz=MzIzNjc1NzUzMw%3D%3D&mid=2247887476&idx=1&sn=0ae5c990a3f2376794effe890264a4cf&chksm=e90f4689c3631f787a3d75e7836cc7206e8ee5fa3f2182a39b1e5dbb15dc71b0f5c72dc6ab75#rd)

## 个人评注

Batch Invariance 是一个值得 OpenClaw 参考的工程理念——在复杂的多阶段管线（训练→RL→推理）中，数值确定性是可调试性和可复现性的前提。对于 OpenClaw 的 content pipeline 和 HITL 工作流，类似的「底层确定性约束」思路可以帮助定位问题来源（是数据变了还是系统行为变了），提高自动化管线的可信度。
