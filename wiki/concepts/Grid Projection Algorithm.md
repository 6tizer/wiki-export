---
title: Grid Projection Algorithm
type: concept
tags:
- 开发工具
status: 审核中
confidence: high
last_compiled: '2026-04-23'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/fc2ae7d7c28145748d1158b85e4d05fe
notion_id: fc2ae7d7-c281-4574-8d11-58b85e4d05fe
---

## 定义

Grid Projection Algorithm 是 LiteParse 用来重建 PDF 版式结构的核心算法。它通过识别文本锚点并把文本项投影到统一网格中，尽量保留多栏布局、对齐关系与表格结构。

## 关键要点

- 先按相近 Y 坐标组织文本行。

- 再抽取左、右、中的锚点并对文本项分类。

- 随后把文本投影到网格列中，让空间关系转化为可处理的结构。

- 该方法适合规则较强的文档版式，兼顾结构保真与速度。

## 来源引用

- [摘要：fast and light](summaries/摘要：fast and light.md)（[原文](https://x.com/jerryjliu0/status/2047041129326194882)）
