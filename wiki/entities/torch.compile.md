---
title: torch.compile
type: entity
tags:
- 推理优化
- 模型部署
status: 草稿
confidence: high
last_compiled: '2026-04-29'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/d670159c315248249d6946368f6fea76
notion_id: d670159c-3152-4824-9d69-46368f6fea76
---

## 定义

torch.compile 是 PyTorch 2.0 引入的编译优化工具，通过将 Python 层面的逐操作解释执行转换为整体编译执行，消除 Python 开销和算子调度时间，显著提升模型推理和训练性能。

## 关键要点

- 传统 PyTorch 代码每执行一个操作都需要 Python 解释器调度，产生大量零碎小任务，GPU 频繁启停

- torch.compile 将整个计算图整体分析，把相邻的、可合并的运算融合成一个大的优化内核，一次性编译

- 从逐条解释执行变为连续编译程序运行，省去大量 Python 开销和算子调度时间

- 在实时图像生成等延迟敏感场景下效果显著

- 通常与激活缓存、量化、CUDA Graph（内存快照）等技术组合使用

## 关联概念

- 激活缓存

- Flipbook

- CUDA Graph

## 来源引用

- [摘要：最近刷屏的Flipbook，想把互联网彻底变成实时生成的无限世界](summaries/摘要：最近刷屏的Flipbook，想把互联网彻底变成实时生成的无限世界.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzkyNjU2ODM2NQ%3D%3D&mid=2247628305&idx=1&sn=1634861c0bf7ef88e8ea3c207591936f&chksm=c3b497c9c9527e8822c484d33b554e86ada2fad94d08f10aee624de72a30655b90d22527cb33#rd)）
