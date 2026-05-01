---
title: AOT 编译
type: concept
tags:
- Harness 工程
- 推理优化
status: 草稿
confidence: high
last_compiled: '2026-04-26'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/57ff6d6163af45eeb9f67c028cf791c3
notion_id: 57ff6d61-63af-45ee-b9f6-7c028cf791c3
---

## 定义

AOT 编译（Ahead-of-Time Compilation）指在 Skill 真正执行前，先根据目标模型、Harness 与宿主环境，对自然语言 Skill 做静态分析、改写与优化。

## 关键要点

- 它把失败模式前移到安装阶段处理，而不是留给运行时临场补救。

- 在 SkVM 中，AOT 阶段负责能力适配、环境绑定与并发机会提取。

- AOT 的目标不是追求最强推理，而是提高跨模型、跨 Harness 的稳定性与可重复性。

## 来源引用

- [摘要：SkVM：优化你的Skills能够跨模型、跨Harness、跨环境稳定运行 ｜SJTU最新](summaries/摘要：SkVM：优化你的Skills能够跨模型、跨Harness、跨环境稳定运行 ｜SJTU最新.md)（[原文](https://mp.weixin.qq.com/s?__biz=Mzg4MzYxODkzMg%3D%3D&mid=2247508119&idx=1&sn=8576b881967cee0b33dc2c424c9853a5&chksm=ce7a42ad8a773a9cdc3297389c1915b62ee8ee06d86ae09cbf47c11c9141230f4f6a7f8916f7#rd)）
