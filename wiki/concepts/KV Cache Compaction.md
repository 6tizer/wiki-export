---
title: KV Cache Compaction
type: concept
tags:
- LLM
- 记忆系统
status: 草稿
confidence: medium
last_compiled: '2026-04-12'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/f99ccf34321f47f9a30338e4fe4f2dc3
notion_id: f99ccf34-321f-47f9-a303-38e4fe4f2dc3
---

**定义**

KV Cache Compaction 是一种压缩模型注意力缓存的方法，目标是在保留主要注意力行为的前提下，把更小的 key-value 表征传给后续推理过程，从而降低长上下文成本。

### 关键要点

- 核心目标是在压缩后尽量保持原始 attention 输出不变。

- 不是做文本摘要，而是直接在模型内部的表示层做裁剪与重建。

- 适合长上下文推理、多轮调用，以及多 Agent 之间的记忆传递场景。

- 在本文里，它被进一步改造成任务引导式压缩，用于 worker 继承 orchestrator 的有效记忆。

### 来源引用

- [Latent Briefing: Efficient Memory Sharing for Multi-Agent Systems via KV Cache Compaction](https://x.com/RampLabs/status/2042660310851449223)｜源文章：Latent Briefing：让多智能体系统共享「潜在记忆」，Token 消耗直降 49%｜作者：@RampLabs｜发布日期：2026-04-10

- [Introducing Latent Briefing, a way for agents to quickly share their relevant memory directly. Result: 31% fewer tokens used, same accuracy.](https://x.com/RampLabs/status/2042672773747589588)｜源文章：Latent Briefing：让 AI Agent 直接共享记忆，省掉 31% 的 Token｜作者：@RampLabs｜发布日期：2026-04-10

### 关联概念

- [Latent Briefing](concepts/Latent Briefing.md)

- [Attention Matching](concepts/Attention Matching.md)

- [Recursive Language Model](concepts/Recursive Language Model.md)

- [MAD-normalized thresholding](concepts/MAD-normalized thresholding.md)

- [KV Prefix Caching](concepts/KV Prefix Caching.md)

- [Shared global mask](concepts/Shared global mask.md)
