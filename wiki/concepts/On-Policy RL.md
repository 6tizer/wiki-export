---
title: On-Policy RL
type: concept
tags:
- LLM
status: 审核中
confidence: high
last_compiled: '2026-04-23'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/773ca3f12a754a7bba6bbcf491ae3c18
notion_id: 773ca3f1-2a75-4a7b-ba6b-bcf491ae3c18
---

## 定义

On-Policy RL 是一种在模型当前策略产生的轨迹上继续优化策略的强化学习方式。在搜索增强模型里，它适合直接根据模型真实搜索轨迹、答案正确性和工具效率进行迭代改进。

## 核心要点

- 它优化的是“模型实际会怎么搜、怎么答”，而不是脱离真实轨迹的静态样本。

- 用在搜索 Agent 上，可以更自然地把检索行为、引用行为和回答质量联动起来。

- 相比只做离线微调，On-Policy RL 更适合修正复杂多步工具使用中的行为细节。

## 来源引用

- [摘要：We've published new research on how we post-train models for accurate search-augmented answers.](summaries/摘要：We've published new research on how we post-train models for accurate search-augmented answers.md)（[原文](https://x.com/perplexity_ai/status/2047016400292839808)）

## 关联概念

- [搜索增强语言模型](concepts/搜索增强语言模型.md)

- [监督微调](concepts/监督微调.md)

- [正确性门控奖励](concepts/正确性门控奖励.md)

- [Qwen3.5](entities/Qwen3.5.md)
