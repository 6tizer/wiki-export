---
title: Parcae 架构
type: concept
tags:
- 训练/微调
- 推理优化
status: 审核中
confidence: medium
last_compiled: '2026-04-20'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/a1f144a1d72f42c59b2cd9e637aa4c10
notion_id: a1f144a1-d72f-42c5-9b2c-d9e637aa4c10
---

## 定义

Parcae 架构是文中用于解释循环模型稳定性的一类设计思路，通过 LTI 注入与谱半径约束控制递归更新过程，降低循环网络在训练时出现发散或残差爆炸的风险。

## 关键要点

- 核心目标不是提升模型花样，而是让循环式深度扩展具备可训练性与可控性。

- 通过约束状态转移矩阵的谱半径，可以把递归更新限制在更稳定的动态范围内。

- 在 OpenMythos 里，Parcae / LTI 注入是把“可循环推理”变成“可稳定训练”的关键补丁。

- 这类稳定化方法对任何希望做测试时加深、递归推理的模型都具有参考价值。

## 关联概念

- [OpenMythos](entities/OpenMythos.md)

- [Recurrent-Depth Transformer](concepts/Recurrent-Depth Transformer.md)

- [Claude Mythos](entities/Claude Mythos.md)

- [MoE 架构](concepts/MoE 架构.md)

## 来源引用

- 摘要：OpenMythos：开源复现 Claude Mythos！想研究"推理时可以深入思考"的模型？也许这是你最好的开源选择！（[原文](https://mp.weixin.qq.com/s?__biz=MzY5NzIxODM2MQ%3D%3D&mid=2247484602&idx=1&sn=48770b7f95580e4cee6d0027db347794&chksm=f53c2679a92de78400c852ff7bc6114b837ef81101bec148324968db0ce2f6ec182eac20d190#rd)）
