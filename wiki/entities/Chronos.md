---
title: Chronos
type: entity
tags:
- AI 产品
- 训练/微调
status: 草稿
confidence: medium
last_compiled: ''
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/48a873ef8439470f9ff9c72955a8a679
notion_id: 48a873ef-8439-470f-9ff9-c72955a8a679
---

**定义**

Chronos 是 Amazon 推出的时序基础模型，基于 T5 架构，将连续时序值 tokenize 后以语言模型方式做概率预测。

### 关键要点

- 核心思路：把连续时序数据通过 scaling + quantization 映射为离散 token，然后用预训练语言模型（T5）做自回归生成。

- 属于通用时序预测模型，与 Kronos 共享「时序 → token → Transformer」的大框架，但 Kronos 在 tokenizer 设计上做了金融专用优化（分层 BSQ 量化）。

- 是 Kronos 论文中的 baseline 之一。

- 开源，有多种参数规模可选。

### 与知识库其他条目的关系

- 与 [Kronos](entities/Kronos.md) 共享「tokenize 连续值 → 语言模型式预训练」的技术基因

- 与 [K 线语言建模](concepts/K 线语言建模.md) 方法论相关

- 同属通用时序底座阵营，与 TimesFM、MOIRAI 并列
