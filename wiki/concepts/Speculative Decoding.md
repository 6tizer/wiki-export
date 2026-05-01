---
title: Speculative Decoding
type: concept
tags: []
status: 审核中
confidence: high
last_compiled: '2026-04-23'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/c372aca9314a459ebcba3c8f7f5bb922
notion_id: c372aca9-314a-459e-bcba-3c8f7f5bb922
---

## 定义

Speculative Decoding 是一种大模型推理加速范式。它先由更快的 draft model 生成候选 token，再由更强的 target model 批量验证并提交正确前缀。

## 关键要点

- 核心目标是减少 target model 逐 token 自回归解码的次数

- 加速收益取决于草稿模型质量、验证开销与可提交前缀长度

- DFlash 和 DDTree 都可以视为这一范式下的具体实现路径

- 在工程实践中，batch size、任务类型和命中率都会显著影响真实收益

## 来源引用

- [原文链接](https://x.com/nash_su/status/2043924682802712600)｜《Qwen 推理性能最高提升8倍！》｜项目页：[DDTree](https://liranringel.github.io/ddtree/)｜源文章：DDTree：在 DFlash 基础上再提速，Qwen3 推理性能最高飙升 8 倍

- [摘要：Tree-based speculative decoding for Apple Silicon.](summaries/摘要：Tree-based speculative decoding for Apple Silicon.md)（[原文](https://x.com/QingQ77/status/2045500092527087861)）

- [摘要：Worklanes, not just tabs.](summaries/摘要：Worklanes, not just tabs.md)（[原文](https://x.com/iotcoi/status/2046950805568164168)）

## 关联概念

- [DDTree](concepts/DDTree.md)

- [DFlash](concepts/DFlash.md)

- [Tree Attention](concepts/Tree Attention.md)

- [Block Diffusion](concepts/Block Diffusion.md)

- [ddtree-mlx](entities/ddtree-mlx.md)

- [Qwen3.5-27B](entities/Qwen3.5-27B.md)

- [vLLM](entities/vLLM.md)

- [Qwen3.6-27B](entities/Qwen3.6-27B.md)
