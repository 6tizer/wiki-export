---
title: K 线语言建模
type: concept
tags: []
status: 审核中
confidence: high
last_compiled: '2026-04-12'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/a5e38723e0ae402e9e6473bebb44c4e4
notion_id: a5e38723-e0ae-402e-9e64-73bebb44c4e4
---

**定义**

K 线语言建模是一种把 OHLCV 等金融序列视为可被 token 化和建模的“语言”来处理的方法，用序列建模去学习价格形态、波动结构与市场节奏。

### 关键要点

- 将连续 K 线序列转换为离散 token 序列，再交给自回归模型学习。

- 核心假设是金融市场同样存在可被模型捕捉的局部模式与时序依赖。

- 相比通用时序预测，这一路线更强调金融市场自身的结构特征与噪声属性。

### 来源引用

- 《first open-source foundation model》｜Notion 源文章：Kronos：清华开源的首个金融K线基础模型，「93%准确率」到底是什么意思？｜原文链接：[X 帖子](https://x.com/DtDt666/status/2042957736342618147)
