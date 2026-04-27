---
title: flow matching
type: concept
tags:
- 训练/微调
- 多模态
status: 草稿
confidence: medium
last_compiled: '2026-04-17'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/0cf590256ed44c63be00d5aa33215ffd
notion_id: 0cf59025-6ed4-4c63-be00-d5aa33215ffd
---

### 定义

flow matching 是一种用于生成连续动作轨迹的建模方法，文章中被用于 action expert 生成动作 chunk，以支持高频控制。

### 关键要点

- 相比把动作离散成 token 的方案，更适合连续控制场景

- 在 π 系列架构中，它承担从理解到动作执行之间的生成桥梁

- 文章将其视作第二代 VLA 架构的重要实现细节之一

### 来源引用

- [π0.7发布，VLA押出了机器人的GPT-3时刻](https://mp.weixin.qq.com/s?__biz=MzIzNjc1NzUzMw%3D%3D&mid=2247884140&idx=2&sn=a26f0706c04bc3c8dd53f152e4133e38&chksm=e98d64f1cb9afef869d1774c4600f92227b8c887705347a50408a07afa2befe699960bb212b7#rd)｜量子位｜2026-04-17｜源页面：π0.7发布，VLA押出了机器人的GPT-3时刻

### 备注

后续可与 diffusion policy、离散动作 token 化路线做对比整理。
