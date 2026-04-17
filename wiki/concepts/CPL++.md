---
title: CPL++
type: concept
tags:
- LLM
status: 草稿
confidence: high
last_compiled: '2026-04-16'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/e13337ff59cc40eb97a7de06a90f4fee
notion_id: e13337ff-59cc-40eb-97a7-de06a90f4fee
---

### 定义

CPL++ 是面向弱监督视觉定位的进阶伪标签学习框架，在初始伪标签生成基础上，加入**自监督关联校正**与**自监督关联验证**机制，使模型能够在训练过程中动态发现并修正错误的区域—文本关联。

### 关键要点

- 在 CPL 的基础上，从“过滤错误标签”升级为“过滤 + 纠正错误标签”。

- 通过语义感知候选池综合类别、属性、空间关系与检测器置信度，评估候选区域质量。

- 当模型预测与候选最优区域存在明显偏差时，会动态融合生成更精确的新伪标签。

- 利用训练损失对样本进行动态加权，降低噪声样本对训练的干扰。

### 来源引用

- [TPAMI 2026 | 北大彭宇新团队提出CPL++框架，实现视觉定位模型的「自知之明」和「自我纠错」](https://mp.weixin.qq.com/s?__biz=MzA3MzI4MjgzMw%3D%3D&mid=2651028135&idx=3&sn=7ba2faf4b884a950dd1aa45a46ffaf9e&chksm=853fcc0a960e083801be3e3f2cf9093f68e8f8ab0a951c7dbea3f06cba32d533df7b4b8460fe#rd)｜机器之心｜2026-04-16

### 关联概念

- CPL

- 弱监督视觉定位

- 自监督关联校正

- 自监督关联验证
