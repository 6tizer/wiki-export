---
title: KV Cache 压缩
type: concept
tags:
- 推理优化
- 算力基础设施
status: 草稿
confidence: high
last_compiled: '2026-04-30'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/f3a52894e8e44945ab3c864b69c91f81
notion_id: f3a52894-e8e4-4945-ab3c-864b69c91f81
---

## 定义

KV Cache 压缩是指在大模型推理过程中，通过架构设计减少 Key-Value 缓存占用的技术方法，直接影响推理速度、显存效率和并发能力。

## 关键要点

- DeepSeek 在多模态领域实现了极致压缩：一张 756×756 图片从 ViT 输出 2916 个 patch token，经 3×3 通道压缩和 CSA 注意力后，最终只剩 81 条视觉 KV cache 条目，端到端压缩比达 7,056 倍

- DeepSeek 的压缩演进路线：OCR（16× token 压缩）→ V3.2（Sparse Attention）→ OCR 2（双流注意力）→ V4（KV 缓存压到 V3.2 的 7%）

- 核心架构组件：CSA（Cross-layer Shared Attention）+ HCA（Hybrid Cross Attention）

- 设计哲学：「先把省 token 做到极致，再把省下来的预算塞进更贵的能力」

## 关联概念

- Visual Primitives

- DeepSeek Sparse Attention

## 来源引用

- [摘要：刚刚，DeepSeek最新成果，节前发布！](summaries/摘要：刚刚，DeepSeek最新成果，节前发布！.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzIyNjM2MzQyNg%3D%3D&mid=2247722411&idx=1&sn=bdec00adace587c9737956cd7554bdb4&chksm=e900cea0128d25e4398f9e439ce550cf8de63aabb709f43fd4040baeceb7cd184cf5104f51f7#rd)）
