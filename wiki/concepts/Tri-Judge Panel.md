---
title: Tri-Judge Panel
type: concept
tags:
- 模型评测
status: 草稿
confidence: high
last_compiled: '2026-04-29'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/68d27d4e96424f4e9df28861377fdc5e
notion_id: 68d27d4e-9642-4f4e-9df2-8861377fdc5e
---

## 定义

Tri-Judge Panel 是一种使用来自不同模型家族的三个 LLM 评审官并行评分 Agent 回复质量的评测方法。通过跨家族多样性减轻模型自我偏好偏差（self-preference bias），通过数学共识（均值而非投票）将粗糙的四级量表转换为连续指标。

该方法由 CREAO 平台在 Self-Healing Agent Harness 中实践。

## 关键要点

- 三个评审官分别来自 Anthropic、OpenAI、Google 模型家族，并行调用

- 每个评审官通过 schema-locked tool call 返回结构化输出：reasoning、category、quality（excellent/good/acceptable/poor）、issues（9 项分类法）、confidence（0-1）

- 质量映射为 1-4 数值后取均值，而非多数投票——使连续指标（如 3.33 vs 2.66）在小样本下就能检测趋势

- 单个评审官失败不阻塞裁决，仅降低该行的 quorum 大小

- 定期抽样部分裁决回传人工校准，若评审共识与人工评审持续偏差，视为评分标准 Bug

- 同家族自评可能膨胀约 0.3 分，但被其他两个家族的评审冲洗掉

- 每个评审官的独立评分持久化存储，支持事后审计和权重调整

## 分类条件化评分

- 评分前由轻量分类器（Job 0）将交互映射到 12 个核心领域之一

- 每个评审官看到相同的对话记录，但按领域特定的红旗列表评分

- 领域包括：coding、research、data analysis、task automation、agent building 等

## 采样策略

- 按模型差异化采样，而非扁平采样

- 主力生产模型（如 Sonnet）：10%

- 少数/实验模型：100%

- 目的是让少数模型在数小时内达到统计显著性

## 关联概念

- [Self-Healing Agent Harness](concepts/Self-Healing Agent Harness.md)

- [AI-Gated Grey Rollout](concepts/AI-Gated Grey Rollout.md)

- [Agent Harness](concepts/Agent Harness.md)

- [CREAO](entities/CREAO.md)

## 来源引用

- [摘要：The Self-Healing Agent Harness](summaries/摘要：The Self-Healing Agent Harness.md)（[原文](https://x.com/intuitiveml/status/2048912026018484317)）
