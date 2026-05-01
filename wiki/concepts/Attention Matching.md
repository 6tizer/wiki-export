---
title: Attention Matching
type: concept
tags:
- 知识管理
- 推理优化
- 上下文管理
status: 审核中
confidence: medium
last_compiled: '2026-04-12'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/75220918b2cf48799d8fe41597b59b6e
notion_id: 75220918-b2cf-4879-9d8f-e41597b59b6e
---

**定义**

Attention Matching 是一种 KV cache 压缩框架，目标是为每个 attention head 构造更小的缓存，同时让压缩后的注意力输出尽可能逼近原始结果。

### 关键要点

- 先选出高注意力 key 位置作为压缩后的保留集合。

- 再通过偏置修正项 β 去逼近原始 softmax 分布。

- 最后用 ridge regression 重建 value 向量，尽量保留原始 attention 结果。

- 原始算法按 layer 和 head 独立求解，压缩质量高，但推理时延较大。

- Latent Briefing 以它为基础，进一步做了任务引导和批处理改造。

### 来源引用

- [Latent Briefing: Efficient Memory Sharing for Multi-Agent Systems via KV Cache Compaction](https://x.com/RampLabs/status/2042660310851449223)｜源文章：Latent Briefing：让多智能体系统共享「潜在记忆」，Token 消耗直降 49%｜作者：@RampLabs｜发布日期：2026-04-10

- [Introducing Latent Briefing, a way for agents to quickly share their relevant memory directly. Result: 31% fewer tokens used, same accuracy.](https://x.com/RampLabs/status/2042672773747589588)｜源文章：Latent Briefing：让 AI Agent 直接共享记忆，省掉 31% 的 Token｜作者：@RampLabs｜发布日期：2026-04-10

### 关联概念

- [Latent Briefing](concepts/Latent Briefing.md)

- KV Cache Compaction

- [MAD-normalized thresholding](concepts/MAD-normalized thresholding.md)

- [Shared global mask](concepts/Shared global mask.md)
