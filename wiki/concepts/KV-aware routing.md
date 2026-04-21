---
title: KV-aware routing
type: concept
tags:
- LLM
status: 草稿
confidence: medium
last_compiled: '2026-04-21'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/6f4f631b7c554836b83d864221c4c979
notion_id: 6f4f631b-7c55-4836-b83d-864221c4c979
---

## 定义

KV-aware routing 是一种在推理请求分发时感知 KV cache 状态的路由策略，用来优先复用已有上下文缓存，减少重复计算与首 token 延迟。

## 关键要点

- 核心目标是提升缓存命中率与吞吐效率。

- 它更偏向推理服务层优化，而不是模型本身的能力改进。

## 来源引用

- 摘要：Kimi K2.6 has landed, and it is live on Baseten!（[原文](https://x.com/baseten/status/2046263526281576573)）

## 关联概念

- Kimi K2.6
