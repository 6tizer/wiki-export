---
title: 摘要：Tree-based speculative decoding for Apple Silicon.
type: summary
tags:
- LLM
- 开发工具
status: 已审核
confidence: high
last_compiled: '2026-04-23'
source_tags: ''
source_article_url: https://www.notion.so/34b701074b6881b68b62d9858854016e
notion_url: https://www.notion.so/da351956854c4aa6b9eb1589b09ff925
notion_id: da351956-854c-4aa6-b9eb-1589b09ff925
---

## 一句话摘要

DDTree-MLX 把 DFlash 的单链式草稿扩展成可一次性验证的树状候选，在 Apple Silicon 上为 Qwen 3.5 27B 带来比自回归约 1.5 倍、比 DFlash 再快约 10–15% 的无损推理加速。

## 关键洞察

- 这套方案的核心不是换模型，而是把 speculative decoding 的草稿阶段从“单条候选序列”升级为“多分支草稿树”，让 target model 一次前向就能验证更多可能路径。

- 在 M3 Ultra 上，Qwen 3.5 27B 4-bit 的实测速度从自回归 27.9 tok/s 提升到 DFlash + DDTree 的 42.3 tok/s，说明 Apple Silicon 本地推理仍有明显的工程优化空间。

- DDTree 的收益高度依赖 draft model 的接受率，因此它更适合代码生成、结构化输出等高命中任务；对开放式创作文本，增益可能接近于零。

- 为了支持 Qwen 3.5 27B 这类混合架构，项目在 MLX/Metal 上实现了 tree attention、parent-indexed recurrence 和 tree-aware commit，说明本地推理优化已经深入到内核与缓存管理层。

## 提取的概念

- [ddtree-mlx](entities/ddtree-mlx.md)

- [DDTree](concepts/DDTree.md)

- [DFlash](concepts/DFlash.md)

- [Speculative Decoding](concepts/Speculative Decoding.md)

- [Tree Attention](concepts/Tree Attention.md)

- [MLX 框架](entities/MLX 框架.md)

- [Qwen3.5-27B](entities/Qwen3.5-27B.md)

- [GatedDeltaNet](concepts/GatedDeltaNet.md)

## 原始文章信息

- 作者：@QingQ77

- 来源：X书签

- 发布时间：2026-04-18

- 原文链接：[X 线程](https://x.com/QingQ77/status/2045500092527087861)

## 个人评注

这条资料对 Tizer 的启发在于：如果后续要在 Mac 本地承载内容整理、代码生成或 Agent 辅助执行，性能提升不一定只能依赖更强硬件，也可以来自推理链路优化本身。对内容管线和 Coding Agent 来说，这类“高接受率任务优先加速”的思路尤其值得关注；但如果任务是开放式写作或强创造性输出，就要警惕把代码场景下的收益直接外推。
