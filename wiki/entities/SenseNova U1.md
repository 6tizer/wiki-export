---
title: SenseNova U1
type: entity
tags:
- 多模态
- 图像生成
- AI 产品
status: 草稿
confidence: high
last_compiled: '2026-04-30'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/20adbc7ceeeb4c8ea1d2e1746d6dc03c
notion_id: 20adbc7c-eeeb-4c8e-a1d2-e1746d6dc03c
---

## 定义

SenseNova U1 是商汤科技（SenseTime）推出的多模态理解生成统一模型，基于自研 NEO-Unify 架构，将图像理解、视觉推理和图像生成融合在同一个模型中，无需依赖独立的视觉编码器（VE）或变分自编码器（VAE）。

别名：商汤日日新 U1

## 关键要点

- 开源轻量版 U1 Lite 包含两个规格：SenseNova-U1-8B-MoT（稠密骨干）和 SenseNova-U1-A3B-MoT（MoE 骨干）

- 在图像理解、图像生成、视觉推理基准测试中达到同量级开源 SOTA

- 部分指标超越商业闭源模型

- 支持连续图文创作输出——「边想边画」，依托图文交错思维链技术

- 可生成高密度信息图、漫画分镜、多风格艺术画、结构爆炸图等

- 已在 GitHub 和 Hugging Face 全面开源

## 技术架构

- 核心架构：NEO-Unify，原生混合 Transformer（MoT）

- 统一表征同时保留语义丰富性和像素级保真度

- 文本采用自回归交叉熵目标，视觉通过像素流匹配（Pixel Flow Matching）优化

- 冻结理解分支后，生成分支仍可从统一表征恢复细粒度视觉细节

- NEO-Unify（2B）在 MS COCO 2017 上取得 31.56 PSNR 和 0.85 SSIM

## 关联概念

- [NEO-Unify](concepts/NEO-Unify.md)

- [MoT 架构](concepts/MoT 架构.md)

- [图文交错思维链](concepts/图文交错思维链.md)

- [GPT-Image-2](entities/GPT-Image-2.md)

- [flow matching](concepts/flow matching.md)

- [原生多模态](concepts/原生多模态.md)

- [多模态理解生成统一](concepts/多模态理解生成统一.md)

- [统一表征空间](concepts/统一表征空间.md)

## 来源引用

- [摘要：GPT-Image-2平替！最强开源生图模型来了](summaries/摘要：GPT-Image-2平替！最强开源生图模型来了.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzI3MTA0MTk1MA%3D%3D&mid=2652696301&idx=1&sn=40a255d23a8b0edaf8771b3799ad8304&chksm=f0f20c3245e872ed1063892734d3175e6fb20478e0bf12f8d4e99578455024aa9f648e6a7a31#rd)）

- [摘要：一个小众模型突然火了，可能代表新的范式。](summaries/摘要：一个小众模型突然火了，可能代表新的范式。.md)（[原文](https://mp.weixin.qq.com/s?__biz=Mzg5Mjc3MjIyMA%3D%3D&mid=2247582218&idx=1&sn=80e51d048b9e02606c43a77e3c0b589f&chksm=c1cd10627ff5918ae2643086d387145791783dbd62a0220175d65b37279c38433ed239e1cd53#rd)）
