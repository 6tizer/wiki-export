---
title: Shared global mask
type: concept
tags:
- LLM
- Agent 编排
status: 草稿
confidence: high
last_compiled: '2026-04-13'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/a726a4af90e049e4b658714b822d748d
notion_id: a726a4af-90e0-49e4-b658-714b822d748d
---

**定义**

Shared global mask 是 Latent Briefing 中用于把各层与各 attention head 的相关性评分汇总为单一保留掩码的压缩策略。它让所有 head 共享同一组被保留的上下文位置，从而把原本分散的 KV compaction 求解改造成可批处理的张量操作。

### 关键要点

- 不再让每个 attention head 各自保留不同 token 子集，而是先做跨层、跨 head 的全局评分。

- 共享掩码让原本需要串行执行的大量小型求解可以堆叠成批处理，显著降低 GPU kernel launch 开销。

- 它牺牲了一部分 head 级别的个性化选择空间，但换来了实时可部署的推理性能。

- 这是 Latent Briefing 从学术可行走向工程可用的关键改造之一。

### 来源引用

- [Latent Briefing: Efficient Memory Sharing for Multi-Agent Systems via KV Cache Compaction](https://x.com/RampLabs/status/2042660310851449223)｜源页面：Latent Briefing：让多智能体系统的「工作记忆」压缩传递，Token 消耗直降 65%｜作者：@RampLabs｜发布日期：2026-04-10

### 关联概念

- [Latent Briefing](concepts/Latent Briefing.md)

- [Attention Matching](concepts/Attention Matching.md)

- [Recursive Language Model](concepts/Recursive Language Model.md)

- KV Cache Compaction

- [MAD-normalized thresholding](concepts/MAD-normalized thresholding.md)

- [KV Prefix Caching](concepts/KV Prefix Caching.md)
