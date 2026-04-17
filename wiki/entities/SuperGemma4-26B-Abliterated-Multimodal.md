---
title: SuperGemma4-26B-Abliterated-Multimodal
type: entity
tags:
- LLM
- 开发工具
status: 草稿
confidence: medium
last_compiled: '2026-04-15'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/de67774b07654b449a86c9f566da0df6
notion_id: de67774b-0765-4b44-9a86-c9f566da0df6
---

## 定义

SuperGemma4-26B-Abliterated-Multimodal 是基于 Google Gemma 4 26B 派生的社区版多模态模型，主打低拒绝率、本地运行和 Apple Silicon 友好部署。

## 关键要点

- 文章聚焦 MLX 4bit 版本，磁盘占用约 15GB，更适合 M 系列 Mac 本地部署

- 同一模型线还提供 GGUF 4bit 形态，便于 llama.cpp、LM Studio、Ollama 等生态调用

- 保留图像 + 文本多模态能力，并与 mlx_vlm 工具链兼容

- “Abliterated” 表示弱化或移除部分安全对齐约束，更接近无审查模型路线

## 来源引用

- [原文链接](https://x.com/berryxia/status/2043918551552274690)｜《卧槽！本地 AI 又出神器了 🔥》｜源文章：SuperGemma4-26B：本地跑起来的无审查多模态神器，Mac 用户专属

## 关联概念

- [Gemma 4](entities/Gemma 4.md)

- [Abliteration](concepts/Abliteration.md)

- [MLX 框架](concepts/MLX 框架.md)

- [mlx_vlm](entities/mlx_vlm.md)

- [GGUF](concepts/GGUF.md)
