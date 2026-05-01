---
title: Context DAG
type: concept
tags: []
status: 审核中
confidence: medium
last_compiled: '2026-04-20'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/35e1247fe19d45a8a6d386927eb14424
notion_id: 35e1247f-e19d-45a8-a6d3-86927eb14424
---

## 定义

Context DAG 是一种用于组织与裁剪 AI 推理轨迹的上下文结构方法，核心目标是在尽量不丢失关键依赖关系的前提下，对长链路上下文进行可追溯的压缩与重组。

## 关键要点

- 它把上下文视为带依赖关系的有向无环图，而不是简单的线性日志。

- 价值在于支持更细粒度的“保留什么、裁掉什么”，从而兼顾上下文成本与可恢复性。

- 在本文语境中，Context DAG 被用来描述 h5i 对 AI 编程轨迹的无损裁剪思路。

- 它代表了 AI 编程工作流里“上下文治理”从经验技巧走向结构化方法的一类方向。

## 来源引用

- [摘要：rtk：给 AI 编码工具装上「信息压缩阀」，Token 消耗最高降 90%](summaries/摘要：rtk：给 AI 编码工具装上「信息压缩阀」，Token 消耗最高降 90%.md)（[原文](https://x.com/laogui/status/2045677115341934867)）

## 关联概念

- [h5i](entities/h5i.md)

- [上下文压缩](concepts/上下文压缩.md)

- [RTK](entities/RTK.md)
