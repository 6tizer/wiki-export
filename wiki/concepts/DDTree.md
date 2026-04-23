---
title: DDTree
type: concept
tags:
- LLM
status: 草稿
confidence: medium
last_compiled: '2026-04-23'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/5a39bafe59f84227b8c2c08f6c6c2c4c
notion_id: 5a39bafe-59f8-4227-b8c2-c08f6c6c2c4c
---

## 定义

DDTree 是建立在 block diffusion speculative decoding 之上的草稿树方法。它把单链式 draft 扩展为树状候选，并让 target model 用一次前向计算验证整棵树。

## 关键要点

- 草稿模型一次生成一个 block 内多个位置的候选分布，再组织成 draft tree

- 验证阶段借助 Tree Attention 一次评分整棵树，而不是逐 token 线性确认

- 提交阶段沿最长匹配路径前进，把下一个未匹配 token 作为新的 bonus token

- 目标是减少 branching point 处被浪费的候选预测，提高推理吞吐

## 来源引用

- [原文链接](https://x.com/nash_su/status/2043924682802712600)｜《Qwen 推理性能最高提升8倍！》｜项目页：[DDTree](https://liranringel.github.io/ddtree/)｜源文章：DDTree：在 DFlash 基础上再提速，Qwen3 推理性能最高飙升 8 倍

- [摘要：Tree-based speculative decoding for Apple Silicon.](summaries/摘要：Tree-based speculative decoding for Apple Silicon.md)（[原文](https://x.com/QingQ77/status/2045500092527087861)）

- [摘要：Worklanes, not just tabs.](summaries/摘要：Worklanes, not just tabs.md)（[原文](https://x.com/iotcoi/status/2046950805568164168)）

## 关联概念

- [DFlash](concepts/DFlash.md)

- [Speculative Decoding](concepts/Speculative Decoding.md)

- [Tree Attention](concepts/Tree Attention.md)

- [Block Diffusion](concepts/Block Diffusion.md)

- [ddtree-mlx](entities/ddtree-mlx.md)

- [MLX 框架](entities/MLX 框架.md)

- [Qwen3.5-27B](entities/Qwen3.5-27B.md)

- [GatedDeltaNet](concepts/GatedDeltaNet.md)

- [vLLM](entities/vLLM.md)

- [Qwen3.6-27B](entities/Qwen3.6-27B.md)
