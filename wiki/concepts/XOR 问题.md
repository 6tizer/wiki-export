---
title: XOR 问题
type: concept
tags:
- 训练/微调
status: 审核中
confidence: high
last_compiled: '2026-04-20'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/69890533b3f14550a0c9fa268bb64f46
notion_id: 69890533-b3f1-4550-a0c9-fa268bb64f46
---

## 定义

XOR 问题是神经网络和机器学习教学中的经典最小案例，用来说明线性可分限制：单层感知机无法正确表示异或关系，因此需要至少一层隐藏层。

## 关键要点

- 输入为两个二值变量，输出满足“不同为 1，相同为 0”。

- 它常被用作神经网络的“Hello World”，因为规模足够小，但又能体现非线性建模的必要性。

- 文章选择 2→2→1 的网络结构来学习 XOR，是为了把前向传播和反向传播压缩到最容易手工实现的规模。

## 适用边界

- 适合作为教学、验证训练循环和演示网络结构作用的入门问题。

- 不代表真实世界任务复杂度，但能很好地暴露实现正确性。

## 来源引用

- [摘要：Building a Neural Network from Scratch in Pure x86-64 Assembly](summaries/摘要：Building a Neural Network from Scratch in Pure x86-64 Assembly.md)
