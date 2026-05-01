---
title: mHC
type: concept
tags:
- 训练/微调
status: 草稿
confidence: medium
last_compiled: '2026-04-27'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/38d57d9d0a8f4a82b46e79b86bcb9255
notion_id: 38d57d9d-0a8f-4a82-b46e-79b86bcb9255
---

## 定义

mHC（Manifold Hyper-Connections）是 DeepSeek 在 V4 模型中提出的架构创新，基于字节跳动此前提出的 Hyper-Connections（HC）思路，在其基础上增加了流形约束（manifold constraint），以改善深层网络中的信息流动和训练稳定性。

## 关键要点

- 字节跳动最早提出 Hyper-Connections 方法，用于增强 Transformer 层之间的信息传递

- DeepSeek 在 HC 基础上加入流形约束，形成 mHC，属于渐进式创新

- mHC 是 DeepSeek V4 论文的三大创新之一（另外两个是混合注意力机制和 Muon 优化器）

- 体现了国内 AI 公司「咬合式创新」的协作模式——前一家的成果成为后一家的起点

## 关联概念

- Hyper-Connections（字节跳动提出的原始方法）

- DeepSeek V4（首次采用 mHC 的模型）

- Muon 优化器（V4 同期采用的另一项创新）

## 来源引用

- [摘要：聊几句 DeepSeek V4 的体感。](summaries/摘要：聊几句 DeepSeek V4 的体感。.md)（[原文](https://mp.weixin.qq.com/s?__biz=Mzg5Mjc3MjIyMA%3D%3D&mid=2247582111&idx=1&sn=a4c61d4001c76f54e9f8203e84c223f4&chksm=c1b21cecf8ff7060b60328b74bcb9760f3878a2f81ff10dcb20da58dc509fc7954f851074859#rd)）
