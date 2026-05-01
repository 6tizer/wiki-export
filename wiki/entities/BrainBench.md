---
title: BrainBench
type: entity
tags:
- Harness 工程
- 模型评测
status: 草稿
confidence: medium
last_compiled: '2026-04-27'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/43882e8e53934bfb88cfc296e7bd2777
notion_id: 43882e8e-5393-4bfb-88cf-c296e7bd2777
---

## 定义

BrainBench 是 Garry Tan 为 GBrain 构建的公开评测基准，用于衡量个人知识 Agent 检索栈的质量。项目开源于 [garrytan/gbrain-evals](https://github.com/garrytan/gbrain-evals)。

**别名**：gbrain-evals

## 关键要点

- 在 240 页虚构语料（world-v1 + amara-life-v1）上并行评测 4 种适配器：GBrain 全栈、仅 Grep、仅 Vector、GBrain 去图层

- 采用标准 IR 指标：Precision@5、Recall@5，与 Google 搜索质量指标一致

- v0.12.1 基线：P@5 49.1%、R@5 97.9%，图层贡献 +31.4 P@5

- 12 个 Cat 评测维度覆盖检索、身份解析、时序查询、溯源、鲁棒性、多模态等

- 反作弊设计：密封 qrels、容差带、judge 版本锁定、随机查询顺序

## 技术架构

- 依赖 GBrain 核心模块（pglite-engine、operations、link-extraction）

- 使用 Haiku 作为 judge，结构化证据契约

- 支持自定义适配器接入评测

## 来源引用

- [摘要：hybrid GraphRAG memory system](summaries/摘要：hybrid GraphRAG memory system.md)（[原文](https://x.com/garrytan/status/2048503081911128119)）
