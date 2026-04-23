---
title: LLM-as-judge
type: concept
tags:
- LLM
- 工作流
status: 草稿
confidence: high
last_compiled: '2026-04-20'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/747d27deec3b4ee8b935a3bdabfb21df
notion_id: 747d27de-ec3b-4ee8-b935-a3bdabfb21df
---

## 定义

LLM-as-judge 是一种让大模型充当评审器的评估方法：当目标无法只靠单一硬指标衡量时，由模型依据明确标准对候选结果进行比较、打分或排序。在 Compound Engineering 的 /ce:optimize 中，它被用来评估聚类质量、搜索相关性等偏定性的优化目标。

## 关键要点

- 适合“有质量差异，但难以直接写成唯一数值指标”的任务

- 通常要配合清晰的评审标准、对照样本或成对比较，避免模型随意打分

- 可与构建耗时、测试覆盖率等硬指标并行使用，形成混合评估回路

- 结合分层采样后，更适合长时间自动优化，减少被局部样本误导的风险

## 来源引用

- [摘要：Compound Engineering - 4/17/2026](summaries/摘要：Compound Engineering - 4-17-2026.md)（[原文](https://x.com/trevin/status/2045245249392607443)）

- [摘要：CrabTrap: an LLM-as-a-judge HTTP proxy to secure agents in production](summaries/摘要：CrabTrap- an LLM-as-a-judge HTTP proxy to secure agents in production.md)（[原文](https://x.com/pedroh96/status/2046604993982009825)）

## 关联概念

- [autoresearch](entities/autoresearch.md)

- [Compound Engineering](concepts/Compound Engineering.md)

- [Human in the Loop](concepts/Human in the Loop.md)

- [CrabTrap](entities/CrabTrap.md)

- [TLS 拦截](concepts/TLS 拦截.md)

- [流量归纳策略](concepts/流量归纳策略.md)

- [策略回放评测](concepts/策略回放评测.md)
