---
title: 分层离散 Tokenizer
type: concept
tags:
- LLM
status: 审核中
confidence: high
last_compiled: '2026-04-12'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/7d31a550785a4fde9589c00fe7d92dda
notion_id: 7d31a550-785a-4fde-9589-c00fe7d92dda
---

**定义**

分层离散 Tokenizer 是一种把连续、多维的金融 K 线数据量化为层次化离散 token 的表示机制，用于把市场数据转换成适合基础模型预训练的输入格式。

### 关键要点

- 面向 open、high、low、close、volume 等连续变量，而不是自然语言文本。

- 作为两阶段框架的第一步，为后续 Transformer 预训练提供统一离散表示。

- 这类设计决定了模型能否在多资产、多周期数据之间复用表征能力。

### 来源引用

- 《first open-source foundation model》｜Notion 源文章：Kronos：清华开源的首个金融K线基础模型，「93%准确率」到底是什么意思？｜原文链接：[X 帖子](https://x.com/DtDt666/status/2042957736342618147)
