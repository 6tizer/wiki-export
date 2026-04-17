---
title: Knowledge Insulation
type: concept
tags:
- LLM
status: 草稿
confidence: medium
last_compiled: '2026-04-17'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/a4502803a7b64b0db19618dc90bce432
notion_id: a4502803-a7b6-4b0d-b196-18dc90bce432
---

### 定义

Knowledge Insulation 是文中提到的一种训练策略，用来保护 VLM 骨干从互联网学到的语义知识，避免被机器人动作数据过度污染。

### 关键要点

- 通过训练时的梯度隔离，让 action expert 的更新不直接回传到 VLM 骨干

- 目标是在保留通用语义能力的同时，补上机器人动作控制能力

- 这种做法体现了“知识保真 + 能力外挂”的工程思路

### 来源引用

- [π0.7发布，VLA押出了机器人的GPT-3时刻](https://mp.weixin.qq.com/s?__biz=MzIzNjc1NzUzMw%3D%3D&mid=2247884140&idx=2&sn=a26f0706c04bc3c8dd53f152e4133e38&chksm=e98d64f1cb9afef869d1774c4600f92227b8c887705347a50408a07afa2befe699960bb212b7#rd)｜量子位｜2026-04-17｜源页面：π0.7发布，VLA押出了机器人的GPT-3时刻

### 备注

这是一个偏训练机制的术语，后续可与 adapter、冻结骨干等做法一起归档。
