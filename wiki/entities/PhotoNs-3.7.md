---
title: PhotoNs-3.7
type: entity
tags:
- 算力基础设施
- AI 设计
- 链上协议
status: 审核中
confidence: high
last_compiled: '2026-04-26'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/a843fdee7e2b410a8819ab68678cba88
notion_id: a843fdee-7e2b-410a-8819-ab68678cba88
---

## 定义

PhotoNs-3.7 是国家天文台团队自主开发、面向国产超算优化的宇宙学数值模拟代码，用于支撑“千衍”等超大规模引力计算任务。

## 关键要点

- 它采用 PM（粒子网格）与 FMM（快速多极展开）的混合方案计算引力，相比传统 PM-Tree 方法更适合超大规模并行场景。

- 在“千衍”项目中，团队针对“东方”超算进一步重写计算核函数，并重构域分解与 MPI 通信机制。

- 该代码充分利用 CPU-GPU 异构架构，将最耗时的粒子间直接作用计算卸载到 GPU。

- 团队还引入混合精度策略，在保证误差可控的前提下降低内存压力。

## 来源引用

- [摘要：中国科学家用4.2万亿粒子构建虚拟宇宙，以“大衍之数”推演万物](summaries/摘要：中国科学家用4.2万亿粒子构建虚拟宇宙，以“大衍之数”推演万物.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzA3NTIyODUzNA%3D%3D&mid=2649795623&idx=1&sn=5c59215d07a7859ae045830e33f7179e&chksm=8634c6853fe8b94f48810fcb4a0f98abee3f451fa6f9fe0b8705f9798f52dd56d2ce68b975c0#rd)）
