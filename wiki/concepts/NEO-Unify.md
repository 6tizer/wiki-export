---
title: NEO-Unify
type: concept
tags:
- 多模态
- 图像生成
status: 草稿
confidence: high
last_compiled: '2026-04-30'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/5ff31822131e4de0908444334ee89dab
notion_id: 5ff31822-131e-4de0-9084-44334ee89dab
---

## 定义

NEO-Unify 是商汤科技提出的原生多模态统一架构，从第一性原理出发，完全摒弃传统的视觉编码器（VE）和变分自编码器（VAE），将语言和视觉信息作为统一复合体直接建模。

## 关键要点

- 引入近似无损的视觉接口，统一图像的输入与输出表示

- 采用原生混合 Transformer（MoT）架构，理解分支和生成分支在同一骨干网络内协同

- 文本用自回归交叉熵目标训练，视觉用像素流匹配（Pixel Flow Matching）优化

- 冻结理解分支后，生成分支仍能恢复细粒度视觉细节——证明统一表征同时保留了语义丰富性和像素级保真度

- NEO-Unify（2B）预训练 9 万步后，在 MS COCO 2017 上达到 31.56 PSNR / 0.85 SSIM，接近 Flux VAE 的 32.65 / 0.91

- 被认为是第一个真正意义上「全扔掉」VE 和 VAE 的原生统一架构

## 与传统范式的对比

传统做法：VE（看）+ LLM（想）+ VAE（画），三模块独立训练后拼接，感知和创造割裂。

NEO-Unify：单一模型同时处理理解与生成，无需中间「翻译」环节。

## 关联概念

- [SenseNova U1](entities/SenseNova U1.md)

- [MoT 架构](concepts/MoT 架构.md)

- [图文交错思维链](concepts/图文交错思维链.md)

- [flow matching](concepts/flow matching.md)

- [原生多模态](concepts/原生多模态.md)

- [多模态理解生成统一](concepts/多模态理解生成统一.md)

- [统一表征空间](concepts/统一表征空间.md)

## 来源引用

- [摘要：GPT-Image-2平替！最强开源生图模型来了](summaries/摘要：GPT-Image-2平替！最强开源生图模型来了.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzI3MTA0MTk1MA%3D%3D&mid=2652696301&idx=1&sn=40a255d23a8b0edaf8771b3799ad8304&chksm=f0f20c3245e872ed1063892734d3175e6fb20478e0bf12f8d4e99578455024aa9f648e6a7a31#rd)）

- [摘要：一个小众模型突然火了，可能代表新的范式。](summaries/摘要：一个小众模型突然火了，可能代表新的范式。.md)（[原文](https://mp.weixin.qq.com/s?__biz=Mzg5Mjc3MjIyMA%3D%3D&mid=2247582218&idx=1&sn=80e51d048b9e02606c43a77e3c0b589f&chksm=c1cd10627ff5918ae2643086d387145791783dbd62a0220175d65b37279c38433ed239e1cd53#rd)）
