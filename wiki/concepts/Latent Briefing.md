---
title: Latent Briefing
type: concept
tags:
- Agent 编排
- 记忆系统
status: 草稿
confidence: medium
last_compiled: '2026-04-12'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/466738e1b9d246dbbaf31b56f9aae775
notion_id: 466738e1-b9d2-46db-baf3-1b56f9aae775
---

**定义**

Latent Briefing 是一种面向多 Agent 系统的跨代理记忆共享方法。它不把 orchestrator 的历史轨迹重新写成文本，而是直接在 worker 模型的 KV cache 表征层面做压缩，把与当前子任务最相关的上下文传给 worker。

### 关键要点

- 目标是缓解分层多 Agent 架构里的 token 爆炸问题。

- 用当前 worker 任务提示生成 query，反向挑出 orchestrator 轨迹里最相关的 token。

- 共享全局 mask，让不同 layer 和 head 可以批量执行 compaction，显著降低延迟。

- 相比 LLM 摘要或 RAG，它更像“表示层记忆共享”而不是“文本层记忆共享”。

- 在长文档和复杂问题场景下，可以同时优化 token 成本与效果。

### 来源引用

- [Latent Briefing: Efficient Memory Sharing for Multi-Agent Systems via KV Cache Compaction](https://x.com/RampLabs/status/2042660310851449223)｜源文章：Latent Briefing：让多智能体系统共享「潜在记忆」，Token 消耗直降 49%｜作者：@RampLabs｜发布日期：2026-04-10

- [Introducing Latent Briefing, a way for agents to quickly share their relevant memory directly. Result: 31% fewer tokens used, same accuracy.](https://x.com/RampLabs/status/2042672773747589588)｜源文章：Latent Briefing：让 AI Agent 直接共享记忆，省掉 31% 的 Token｜作者：@RampLabs｜发布日期：2026-04-10

### 关联概念

- [Attention Matching](concepts/Attention Matching.md)

- [Recursive Language Model](concepts/Recursive Language Model.md)

- KV Cache Compaction

- [MAD-normalized thresholding](concepts/MAD-normalized thresholding.md)

- [KV Prefix Caching](concepts/KV Prefix Caching.md)

- [Shared global mask](concepts/Shared global mask.md)
