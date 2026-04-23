---
title: OpenAI Privacy Filter
type: entity
tags:
- LLM
- 安全/隐私
status: 草稿
confidence: high
last_compiled: '2026-04-23'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/46b72a0a67884ffa8f8c16e7b6362fb0
notion_id: 46b72a0a-6788-4ffa-8f8c-16e7b6362fb0
---

## 定义

OpenAI Privacy Filter 是 OpenAI 发布的一个轻量级隐私过滤模型，基于与 gpt-oss 相近的架构改造而来，专门用于在大规模文本数据中识别并遮蔽个人敏感信息。

## 核心要点

- 属于面向数据清洗场景的专用模型，而非通用聊天或生成模型。

- 采用 1.5B 总参数、50M 激活参数的 MoE 设计，在成本与吞吐之间取得平衡。

- 支持最长 128k 上下文，适合处理长文档、长日志与大规模语料清洗。

- 作为双向 token 分类器运行，可在单次前向推理中完成标签预测与敏感片段解码。

- Apache 2.0 许可和可本地部署特性，适合企业内部训练前脱敏与合规流程。

## 来源引用

- [摘要：OpenAI Privacy Filter：1.5B MoE 隐私脱敏模型支持 128k 上下文](summaries/摘要：OpenAI Privacy Filter：1.5B MoE 隐私脱敏模型支持 128k 上下文.md)（[原文](https://x.com/eliebakouch/status/2046979020890198503)）

## 关联概念

- [长上下文](concepts/长上下文.md)

- [MoE 架构](concepts/MoE 架构.md)

- [隐私脱敏](concepts/隐私脱敏.md)
