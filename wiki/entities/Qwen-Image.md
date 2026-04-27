---
title: Qwen-Image
type: entity
tags:
- 图像生成
- AI 产品
- 多模态
status: 草稿
confidence: medium
last_compiled: '2026-04-28'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/5f6a9c95e84542b39c83295d3607e125
notion_id: 5f6a9c95-e845-42b3-9c83-295d3607e125
---

## 定义

Qwen-Image 是阿里巴巴通义千问团队推出的文本到图像（Text-to-Image）生成模型系列，基于 MMDiT 扩散架构。该系列包括生成、编辑、分层编辑等多个子模型。

## 版本历史

- **Qwen-Image**（2025-08）：初代 T2I 模型，20B 参数，开源权重（HuggingFace）

- **Qwen-Image-Edit**（2025-08/09）：图像编辑模型，支持自然语言指令编辑

- **Qwen-Image-Edit-2511**（2025-11）：编辑模型升级版

- **Qwen-Image-2512**（2025-12）：生成模型升级版

- **Qwen-Image-Layered**（2025-12）：支持图层分解的可编辑图像生成

- **Qwen-Image-2.0-Pro**（2026-04-22）：最新旗舰版，Arena T2I 排名 #9（1168 Elo）；强项为多语言文本渲染、指令遵循、风格一致性

## 关键特性

- **多语言文本渲染**：在图像中准确渲染中文、英文及其他语言文字，是相比竞品的核心差异化能力

- **指令遵循**：复杂多对象构图的 prompt 遵循度高

- **风格一致性**：跨风格生成的质量更稳定

- **Arena 细分排名**：肖像 #6、写实/电影 #7、艺术 #7

## 平台与 API

- ModelScope Demo：[modelscope.ai/studios/Qwen/Qwen-Image-2.0-pro](http://modelscope.ai/studios/Qwen/Qwen-Image-2.0-pro)

- 阿里云 Model Studio API

- 早期版本开源权重：HuggingFace Qwen/Qwen-Image 系列

## 社区反馈

- 社区高度关注开源权重发布，2.0-Pro 目前仅提供 API 访问

- 与 GPT-Image-2（#1, 1507 Elo）差距明显，但在多语言和非英语场景有独特优势

- 业界观点：开源+企业 API 的组合策略是全球化扩展路径

## 来源引用

- [摘要：Qwen-Image-2.0-Pro 发布](summaries/摘要：Qwen-Image-2.0-Pro 发布.md)（[原文](https://x.com/Alibaba_Qwen/status/2048022731548229869)）
