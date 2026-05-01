---
title: In Distribution
type: concept
tags:
- Harness 工程
- 提示工程
- Agent 协作模式
status: 审核中
confidence: high
last_compiled: '2026-04-16'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/6014b4e3a1ff48dfa55cacaa6fa07e5c
notion_id: 6014b4e3-a1ff-48df-a55c-acaa6fa07e5c
---

## 定义

In Distribution 指的是 Agent 所依赖的工具形态、输出接口与运行路径，恰好落在模型训练和强化过程中已经熟悉的分布内，因此行为更稳定、可靠，也更少依赖提示词“硬拽”出来。

## 关键要点

- 从“乞求模型吐 JSON”到 function calling，本质上是把输出放进模型更熟悉的接口里

- 内建 shell、memory、compaction、prompt caching 等能力之所以更稳，关键在于它们是模型已经理解的工具形状

- 它不是单个 prompt 技巧，而是一种围绕模型分布构建系统接口的工程思路

## 来源引用

- [原文链接](https://x.com/jxnlco/status/2044469127696556153)｜《Sandboxes are coming to the Agents SDK》｜源文章：OpenAI Agents SDK 沙盒：让 AI Agent 真正「留下工作成果」

## 关联概念

- [OpenAI Agents SDK](entities/OpenAI Agents SDK.md)

- [Agent Harness](concepts/Agent Harness.md)

- [Compaction](concepts/Compaction.md)

- [Prompt Caching](concepts/Prompt Caching.md)
