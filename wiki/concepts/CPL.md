---
title: CPL
type: concept
tags:
- 多模态
- 训练/微调
status: 草稿
confidence: high
last_compiled: '2026-04-16'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/63e1a8a8e4a1492dafa95225ddfb2acb
notion_id: 63e1a8a8-e4a1-492d-afa9-5225ddfb2acb
---

### 定义

CPL（Confidence-aware Pseudo-label Learning）是一个面向弱监督视觉定位的伪标签学习框架，核心目标是在训练前识别并过滤不可靠的区域—文本关联，减少错误伪标签对模型训练的污染。

### 关键要点

- 通过启发式增强、对象中心描述、关系感知描述三条生成管线，为候选区域生成高质量伪查询。

- 用单模态文本特征匹配代替直接跨模态对齐，降低异构鸿沟带来的误匹配问题。

- 通过冻结的预训练视觉语言模型对区域—查询对进行静态跨模态验证。

- 为 CPL++ 提供了基础伪标签构造与置信度过滤框架。

### 来源引用

- [TPAMI 2026 | 北大彭宇新团队提出CPL++框架，实现视觉定位模型的「自知之明」和「自我纠错」](https://mp.weixin.qq.com/s?__biz=MzA3MzI4MjgzMw%3D%3D&mid=2651028135&idx=3&sn=7ba2faf4b884a950dd1aa45a46ffaf9e&chksm=853fcc0a960e083801be3e3f2cf9093f68e8f8ab0a951c7dbea3f06cba32d533df7b4b8460fe#rd)｜机器之心｜2026-04-16

### 关联概念

- CPL++

- 弱监督视觉定位

- 自监督关联验证
