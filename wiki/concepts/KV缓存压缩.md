---
title: KV缓存压缩
type: concept
tags:
- LLM
- 记忆系统
status: 已审核
confidence: high
last_compiled: '2026-04-18'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/f2c7110132bf4ecc8855583db9113412
notion_id: f2c71101-32bf-4ecc-8855-583db9113412
---

## 定义

通过量化和压缩语言模型推理过程中的Key-Value缓存（KV Cache）来降低内存占用的技术。在长上下文推理场景中效果尤为显著。

## KV Cache简介

Transformer模型在处理长上下文时，需要存储大量Key和Value张量。KV Cache大小与上下文长度成正比，是长上下文推理的内存瓶颈。

## 主要实现

- **TurboQuant**：谷歌开发，支持Apple Silicon（oMLX）

- 各种量化方案：q4_0、q8_0等

## 应用场景

- 本地运行大模型（Mac用户尤其受益）

- 长文档解析（128K+上下文）

- RAG向量检索优化

## 来源引用

- [摘要：Mac用户可以在oMLX中使用TurboQuant了，搭配Gemma-4-31B实测](summaries/摘要：Mac用户可以在oMLX中使用TurboQuant了，搭配Gemma-4-31B实测.md)

- [摘要：7天用Claude+Codex实现谷歌 TurboQuant 算法（已开源）](summaries/摘要：7天用Claude+Codex实现谷歌 TurboQuant 算法（已开源）.md)

- Latent Briefing：让多智能体系统共享「潜在记忆」，Token 消耗直降 49%

- Latent Briefing：让 AI Agent 直接共享记忆，省掉 31% 的 Token

## 关联概念

- [Latent Briefing](concepts/Latent Briefing.md)

- [Attention Matching](concepts/Attention Matching.md)

- [Recursive Language Model](concepts/Recursive Language Model.md)

- [MAD-normalized thresholding](concepts/MAD-normalized thresholding.md)

- [KV Prefix Caching](concepts/KV Prefix Caching.md)

- [Shared global mask](concepts/Shared global mask.md)
