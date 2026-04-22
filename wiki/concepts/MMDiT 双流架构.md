---
title: MMDiT 双流架构
type: concept
tags:
- 内容创作
- LLM
status: 草稿
confidence: medium
last_compiled: '2026-04-11'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/939ef73baad34e59a629de33366418ae
notion_id: 939ef73b-aad3-4e59-a629-de33366418ae
---

## 定义

MMDiT（Multi-Modal Diffusion Transformer）双流架构是一种原生音视频联合生成的扩散模型架构，将音频流与视频流在同一语义空间中同步建模，取代传统的「先生成视频再叠加音频」串行方式。

## 设计要点

- **对称双分支**：音频分支与视频分支共享同一文本编码器，在统一语义空间中完成理解与生成

- **口型-动作-声音对齐**：联合训练确保三者在生成阶段就保持协同，无需后期对齐

- **独立文本控制**：额外文本控制增强视频语义稳定性

## 应用

首次在 SkyReels V4 中大规模应用，实现了 AI 视频从「多模态拼接」到「原生一体生成」的范式跃迁。

## 来源引用

- 摘要：昆仑万维连发3个王炸模型，亮出2026年AGI战略
