---
title: Recursive Language Model
type: concept
tags:
- Agent 协作模式
- 多Agent协作
- 推理优化
- 上下文管理
- 长期记忆
status: 审核中
confidence: medium
last_compiled: '2026-04-12'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/edd6310271ec49658bc7dd5c508a339e
notion_id: edd63102-71ec-4965-8bc7-dd5c508a339e
---

**定义**

Recursive Language Model 是一种分层多 Agent 推理范式，由更强的 orchestrator 拆解任务，再通过多次调用 worker 模型去分析文档、验证假设或提取信息。

### 关键要点

- orchestrator 负责任务拆解与总体推理轨迹。

- worker 处理更具体的子任务或局部分析。

- 优势是更强的分工和长上下文管理能力。

- 代价是 orchestrator 轨迹会在多次调用中不断膨胀，带来明显的 token 爆炸问题。

- Latent Briefing 主要就是为这类架构解决跨 agent 的记忆传递成本。

### 来源引用

- [Latent Briefing: Efficient Memory Sharing for Multi-Agent Systems via KV Cache Compaction](https://x.com/RampLabs/status/2042660310851449223)｜源文章：Latent Briefing：让多智能体系统共享「潜在记忆」，Token 消耗直降 49%｜作者：@RampLabs｜发布日期：2026-04-10

### 关联概念

- [Latent Briefing](concepts/Latent Briefing.md)

- KV Cache Compaction

- [KV Prefix Caching](concepts/KV Prefix Caching.md)

- [Shared global mask](concepts/Shared global mask.md)
