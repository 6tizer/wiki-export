---
title: ACT-R 激活模型
type: concept
tags:
- 长期记忆
status: 草稿
confidence: high
last_compiled: '2026-04-29'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/0a3f4269d1904cfc8e3b3fa072bed128
notion_id: 0a3f4269-d190-4cfc-8e3b-3fa072bed128
---

## 定义

ACT-R（Adaptive Control of Thought—Rational）是 John Anderson 于 1993 年在卡内基梅隆大学提出的认知架构，其核心的基线激活方程用于模拟人类记忆的提取概率。在 Agent 记忆系统中，ACT-R 的幂律衰减模型被用来计算记忆激活度，使「最近且频繁使用」的记忆优先被检索，而长期未访问的记忆逐渐沉默但不会突然消失。

## 核心公式

`B(t) = ln( Σ t_k^{-d} )`

- `t_k` = 距第 k 次访问的时间（秒）

- `d` = 衰减率（默认 0.5，幂律）

- 对所有访问时间戳求和后取对数

## 关键要点

- **幂律衰减而非指数衰减**：旧记忆不会突然消失，只是变得更安静

- **频率+近因双因素**：10 分钟前访问 1 次 > 10 天前访问 1 次；但几个月内访问 50 次 > 昨天访问 2 次

- **随机噪声**：默认 0.4 的检索噪声，模拟人类提取的变异性

- **检索阈值**：低于阈值（默认 0.0）的记忆不可检索

- **时间戳压缩**：保留最近 50 个独立时间戳，更早的做压缩处理

- 在 CerebroCortex 中，ACT-R 激活占最终检索评分的 30%，与向量相似度（35%）、FSRS 可检索性（20%）和显著性（15%）加权融合

## 与 FSRS 的互补

ACT-R 提供基于访问历史的激活度，FSRS 提供基于间隔重复的可检索性曲线，两者结合使记忆系统既能捕捉「最近常用」信号，也能维护长期稳定性。

## 关联概念

- [CerebroCortex](entities/CerebroCortex.md)

- [FSRS-6](concepts/FSRS-6.md)

- [Agent 记忆基础设施](concepts/Agent 记忆基础设施.md)

## 来源引用

- [摘要：Why Karpathy's Second Brain Breaks at Agent Scale. How Mercury Solves It.](summaries/摘要：Why Karpathy's Second Brain Breaks at Agent Scale. How Mercury Solves It.md)（[原文](https://x.com/Ctrl_Alt_Zaid/status/2049082538686382397)）
