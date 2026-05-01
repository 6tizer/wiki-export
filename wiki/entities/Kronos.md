---
title: Kronos
type: entity
tags:
- 量化交易
- 训练/微调
- 模型评测
status: 审核中
confidence: high
last_compiled: '2026-04-27'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/2f1c813fa34b432380e9007ad52be093
notion_id: 2f1c813f-a34b-4323-80e9-007ad52be093
---

**定义**

Kronos 是一个面向金融市场 K 线序列的开源基础模型，目标是把价格预测、波动率预测等量化任务统一到同一套预训练框架里。

### 关键要点

- 以 45 家交易所、120 亿+ 条 K 线记录作为预训练数据基础。

- 采用两阶段框架，先将连续金融数据离散化，再进行自回归 Transformer 预训练。

- 提供多种参数规模，从可在笔记本运行的小模型到更大容量版本。

- 项目强调零样本适配，但 benchmark 提升并不等于真实交易中可稳定获利。

### 来源引用

- [摘要：first open-source foundation model](summaries/摘要：first open-source foundation model.md)｜Notion 源文章：Kronos：清华开源的首个金融K线基础模型，「93%准确率」到底是什么意思？｜原文链接：[X 帖子](https://x.com/DtDt666/status/2042957736342618147)

- [摘要：有人开发出了一款 AI，它解读 K 线图的方式就像 GPT 阅读英文一样。该模型基于来自 45 个交易所的 120 亿条记录训练而成。其表现优于所有其他模型 93%。提供 BTC 实盘演示。免费。](summaries/摘要：有人开发出了一款 AI，它解读 K 线图的方式就像 GPT 阅读英文一样。该模型基于来自 45 个交易所的 120 亿条记录训练而成。其表现优于所有其他模型 93%。提供 BTC 实盘演示。免费。.md)（[原文](https://x.com/billtheinvestor/status/2047000405448802358)）
