---
title: Sigmoid 激活函数
type: concept
tags:
- LLM
status: 草稿
confidence: high
last_compiled: '2026-04-20'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/d264c1396b2b461d9798997013dbbb28
notion_id: d264c139-6b2b-461d-9798-997013dbbb28
---

## 定义

Sigmoid 激活函数是一种将输入压缩到 0 到 1 区间的非线性函数，形式为 σ(x)=1/(1+e^-x)，常用于早期神经网络和二分类输出层。

## 关键要点

- 它为网络提供非线性能力，使多层网络能够拟合线性不可分问题。

- 导数可以写成 σ(x)·(1-σ(x))，因此在反向传播里实现相对方便。

- 文章中它既用于隐藏层也用于输出层，并通过 x87 FPU 指令组合手工实现指数计算。

## 适用边界

- 概念清晰、教学友好，但在深层网络中容易出现梯度饱和。

- 更现代的网络常在中间层使用 ReLU 等替代方案。

## 来源引用

- [摘要：Building a Neural Network from Scratch in Pure x86-64 Assembly](summaries/摘要：Building a Neural Network from Scratch in Pure x86-64 Assembly.md)
