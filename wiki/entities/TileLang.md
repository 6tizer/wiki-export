---
title: TileLang
type: entity
tags:
- 推理优化
status: 草稿
confidence: medium
last_compiled: '2026-04-29'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/f884e9a9f141480bbcdd1361a8d0091d
notion_id: f884e9a9-f141-480b-bcdd-1361a8d0091d
---

## 定义

TileLang 是一个用于编写高性能 GPU 内核的编程框架，支持融合 warp-specialized 内核的构建。FlashQLA 等项目基于 TileLang 实现了线性注意力内核的深度优化。

## 核心要点

- 支持构建融合的 warp-specialized GPU 内核

- 能够实现数据搬运、Tensor Core 计算与 CUDA Core 计算的流水线重叠

- 被 FlashQLA 用于构建 GDN Chunked Prefill 的高性能前向和反向内核

- GitHub：[https://github.com/tile-ai/tilelang](https://github.com/tile-ai/tilelang)

## 关联概念

- [FlashQLA](entities/FlashQLA.md)

- [GDN Chunked Prefill](concepts/GDN Chunked Prefill.md)

- [Warp Specialization](concepts/Warp Specialization.md)

## 来源引用

- [摘要：Recipes for serving LLMs locally on RTX 3090s.](summaries/摘要：Recipes for serving LLMs locally on RTX 3090s.md)（[原文](https://x.com/Alibaba_Qwen/status/2049462758211772663)）
