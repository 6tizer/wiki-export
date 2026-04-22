---
title: Pass^3
type: concept
tags:
- Agent 编排
status: 草稿
confidence: high
last_compiled: '2026-04-20'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/925878b8f4ca4094a32bbfad12c68a6d
notion_id: 925878b8-f4ca-4094-a32b-bfad12c68a6d
---

## 定义

Pass^3 是 Claw-Eval 采用的核心稳定性指标，要求同一任务在三次独立运行中全部通过，才视为真正完成。

## 关键要点

- 它不是只看单次最好成绩，而是强调结果的可复现性与稳定交付能力。

- 这个指标能过滤掉依赖随机性、偶然跑通或仅在个别样本上表现亮眼的 Agent。

- 相比传统 pass@1 一类指标，Pass^3 更接近真实业务里对“连续可用”的要求。

## 关联概念

- [Claw-Eval](concepts/Claw-Eval.md)

- [Meta Muse Spark](entities/Meta Muse Spark.md)

## 来源引用

- [摘要：Claw-Eval：衡量 AI Agent「真实能力」的新基准，Muse Spark 凭什么排第三](summaries/摘要：Claw-Eval：衡量 AI Agent「真实能力」的新基准，Muse Spark 凭什么排第三.md)（[原文](https://x.com/alexandr_wang/status/2045348588734066794)）
