---
title: Dual-kernel
type: concept
tags:
- 推理优化
status: 草稿
confidence: medium
last_compiled: '2026-04-28'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/9cb55f74c416417ebeb35ca8ed3eabfc
notion_id: 9cb55f74-c416-417e-beb3-5ca8ed3eabfc
---

## 定义

Dual-kernel 是 DeepSeek 在 V4 模型中提出的注意力解码策略，为同一个注意力解码任务准备**两套计算程序**（kernel），分别处理「GPU 利用率高」和「GPU 利用率低」两种负载场景，同时保证两套程序算出的结果逐比特一致。

## 关键要点

- **解决的问题**：传统 split-KV 优化将单条序列的注意力计算分摊到多个 SM 以提高 GPU 利用率，但会改变并行归约路径，破坏 Batch Invariance

- **设计思路**：不用 split-KV，而是根据负载情况选择合适的 kernel，在性能和确定性之间取得平衡

- **核心约束**：两套 kernel 在任何输入下必须产生逐比特完全一致的结果

- **首次应用**：DeepSeek V4

## 来源引用

- [摘要：DeepSeek不惜代价保住它！V4关键特性被挖出来了](summaries/摘要：DeepSeek不惜代价保住它！V4关键特性被挖出来了.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzIzNjc1NzUzMw%3D%3D&mid=2247887476&idx=1&sn=0ae5c990a3f2376794effe890264a4cf&chksm=e90f4689c3631f787a3d75e7836cc7206e8ee5fa3f2182a39b1e5dbb15dc71b0f5c72dc6ab75#rd)）

## 关联概念

- [Batch Invariance](concepts/Batch Invariance.md)

- [DeepGEMM](entities/DeepGEMM.md)

- [DeepSeek V4](entities/DeepSeek V4.md)
