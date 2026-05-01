---
title: Contemplating 模式
type: concept
tags:
- 多Agent协作
- 推理优化
- 模型评测
status: 审核中
confidence: high
last_compiled: '2026-04-17'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/1050886363524e2b91f7c465fd8389f6
notion_id: 10508863-6352-4e2b-91f7-c465fd8389f6
---

## 定义

Contemplating 模式是 Meta Muse Spark 中的多 Agent 并行推理架构：让多个 Agent 同时从不同角度思考同一问题，然后协同得出答案，而非让单个 Agent 延长推理链。

## 与传统测试时缩放的对比

| 方式 | 机制 | 延迟 | 性能 |

| --- | --- | --- | --- |

| 传统测试时缩放 | 单 Agent 延长推理链 | 线性增长 | 对数增长 |

| Contemplating 模式 | 多 Agent 并行推理 | 几乎不变 | 显著提升 |

## 基准表现

- Humanity's Last Exam：58%

- FrontierScience Research：38%

- 直接对标 Gemini Deep Think 和 GPT Pro 的极端推理模式

## 核心思想

承认单个 Agent 推理能力存在天花板，多视角并行 > 单视角深度延伸。类比：三个人各想 20 分钟再讨论 > 一个人想 1 小时。

## 来源引用

- [摘要：开源旗手的闭源豪赌：Meta Muse Spark 背后的战略转向（翻译转写）](summaries/摘要：开源旗手的闭源豪赌：Meta Muse Spark 背后的战略转向（翻译转写）.md)（@berryxia，X书签，2026-04-10）
