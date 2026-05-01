---
title: '摘要：Latent Briefing: Efficient Memory Sharing for Multi-Agent Systems via KV
  Cache Compaction'
type: summary
tags:
- Agent 协作模式
- 多Agent协作
- 上下文管理
status: 已审核
confidence: high
last_compiled: '2026-04-27'
source_tags: ''
source_article_url: https://www.notion.so/341701074b68817799e4ffcb4c6a2ae0
notion_url: https://www.notion.so/Tizer/f0595210767c49b08b1d44f4871f430c
notion_id: f0595210-767c-49b0-8b1d-44f4871f430c
---

**一句话摘要**

Latent Briefing 通过直接压缩并共享多 Agent 系统中的 KV cache 表征，在尽量不损失准确率的前提下，把跨 agent 的记忆传递从文本层搬到表示层，显著降低了长上下文协作的 token 成本。

### 关键洞察

- 它瞄准的是分层多 Agent 架构中的 **token explosion**，尤其是 orchestrator 多轮推理轨迹不断膨胀后，worker 无法高效继承上下文的问题。

- 方法核心不是做文本摘要或 RAG 检索，而是基于任务提示生成 query，对轨迹 KV cache 做任务相关压缩。

- 论文在 Attention Matching 基础上做了三项关键工程改造，包括任务引导查询、Shared global mask，以及基于 MAD 的自适应阈值选择。

- 共享全局掩码让原本需要按 layer 和 head 串行执行的大量求解可批处理化，把 compaction 开销压到约 1.7 秒量级，更接近生产可用。

- 在 LongBench v2 上，该方法在不同条件下取得了与基线相当或更优的准确率，并带来明显 token 节省，尤其对中长文档和复杂问题更有价值。

- 结合另一篇同源解读中的量化结果看，worker token 消耗可降低约 42% 到 57%，说明“更少但更相关的上下文”优于盲目传递全部轨迹。

### 提取的概念

- [Latent Briefing](concepts/Latent Briefing.md)

- [Recursive Language Model](concepts/Recursive Language Model.md)

- [Attention Matching](concepts/Attention Matching.md)

- KV Cache Compaction

- [MAD-normalized thresholding](concepts/MAD-normalized thresholding.md)

- [KV Prefix Caching](concepts/KV Prefix Caching.md)

- [Shared global mask](concepts/Shared global mask.md)

### 原始文章信息

- 作者：@RampLabs

- 来源：X书签

- 发布日期：2026-04-10

- 原文链接：[https://x.com/RampLabs/status/2042660310851449223](https://x.com/RampLabs/status/2042660310851449223)

- Notion 源页面：Latent Briefing：让多智能体系统的「工作记忆」压缩传递，Token 消耗直降 65%

### 个人评注

这篇文章对 Tizer 的多阶段内容处理与 Agent 编排很有参考价值。若未来在 OpenClaw、HITL 审核链路或研究型内容流水线中采用 orchestrator + specialist worker 的协作模式，Latent Briefing 这类“表示层记忆共享”方案，可能比反复拼接长 prompt、做文本摘要或外挂 RAG 更省 token，也更适合高频调用场景。
