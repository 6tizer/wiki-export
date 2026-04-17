---
title: KV Prefix Caching
type: concept
tags:
- LLM
status: 草稿
confidence: medium
last_compiled: '2026-04-12'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/ed578041b1ef478488dc0114f2f29e53
notion_id: ed578041-b1ef-4784-88dc-0114f2f29e53
---

**定义**

KV Prefix Caching 是一种推理优化技术，用来复用多轮调用之间没有变化的前缀表征，只对新增 token 重新做 forward pass。

### 关键要点

- 适合上下文逐步增长、但大部分前缀保持不变的调用模式。

- 可以显著减少重复计算，降低多轮推理的额外开销。

- 在本文的实验设置里，orchestrator 轨迹跨调用高度重用，因此它是实现实时 compaction 的关键配套技术之一。

- 它解决的是重复计算问题，和 Latent Briefing 解决的记忆压缩问题互补。

### 来源引用

- [Latent Briefing: Efficient Memory Sharing for Multi-Agent Systems via KV Cache Compaction](https://x.com/RampLabs/status/2042660310851449223)｜源文章：Latent Briefing：让多智能体系统共享「潜在记忆」，Token 消耗直降 49%｜作者：@RampLabs｜发布日期：2026-04-10

### 关联概念

- [Latent Briefing](concepts/Latent Briefing.md)

- [Recursive Language Model](concepts/Recursive Language Model.md)

- [Shared global mask](concepts/Shared global mask.md)
