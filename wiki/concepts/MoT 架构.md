---
title: MoT 架构
type: concept
tags:
- 多模态
- 推理优化
status: 草稿
confidence: medium
last_compiled: '2026-04-29'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/f4b3dd31a7ca45c1b52169ac8a4b0900
notion_id: f4b3dd31-a7ca-45c1-b521-69ac8a4b0900
---

## 定义

MoT（Mixed of Transformer，混合 Transformer）是 NEO-Unify 架构中采用的原生混合 Transformer 设计，将理解分支和生成分支集成在同一个骨干网络内协同工作，实现多模态理解与生成的统一。

## 关键要点

- 在同一个 Transformer 骨干中同时容纳理解和生成能力

- SenseNova U1 提供两种 MoT 变体：稠密骨干（8B）和 MoE 骨干（A3B）

- 统一学习框架下，文本走自回归交叉熵路径，视觉走像素流匹配路径

- 架构使得理解和生成共享上下文，确保连续图文输出的一致性

## 关联概念

- [SenseNova U1](entities/SenseNova U1.md)

- [NEO-Unify](concepts/NEO-Unify.md)

- [图文交错思维链](concepts/图文交错思维链.md)

- [flow matching](concepts/flow matching.md)

## 来源引用

- [摘要：GPT-Image-2平替！最强开源生图模型来了](summaries/摘要：GPT-Image-2平替！最强开源生图模型来了.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzI3MTA0MTk1MA%3D%3D&mid=2652696301&idx=1&sn=40a255d23a8b0edaf8771b3799ad8304&chksm=f0f20c3245e872ed1063892734d3175e6fb20478e0bf12f8d4e99578455024aa9f648e6a7a31#rd)）
