---
title: GraphWalks BFS
type: concept
tags:
- LLM
status: 草稿
confidence: medium
last_compiled: '2026-04-13'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/4cd2ccb2746742e09e5805554cc6bcdf
notion_id: 4cd2ccb2-7467-42e0-9e58-05554cc6bcdf
---

## 定义

GraphWalks BFS 是文中重点引用的图搜索测试，用来衡量模型在图结构上执行广度优先搜索这类迭代算法的能力。

## 关键要点

- 它要求模型沿图的层级逐步访问节点，本质上考察图遍历与搜索能力

- 文中将 Mythos 在该测试上的异常高分视为架构创新的重要线索

- 这类任务对标准一次性前向传播架构并不友好，却更符合循环式计算的归纳偏置

## 关联概念

- [Claude Mythos](entities/Claude Mythos.md)

## 来源引用

- [原文链接](https://mp.weixin.qq.com/s?__biz=MzIzNjc1NzUzMw%3D%3D&mid=2247882749&idx=1&sn=2c5b489ce91054109b22b36188b08e7d&chksm=e912871f3bcec6edb33f9d3bbe2448cd2e302161209286bca16ddf778484c2f0d06c176fa3a7#rd)｜《Claude强到不敢发的Mythos，被质疑用了字节Seed技术》｜源文章：Claude强到不敢发的Mythos，被质疑用了字节Seed技术
