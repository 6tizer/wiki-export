---
title: CerebroCortex
type: entity
tags:
- 长期记忆
- MCP 协议
status: 草稿
confidence: medium
last_compiled: '2026-04-29'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/c9ecf21d45204f139d0ab58f15e5cd08
notion_id: c9ecf21d-4520-4f13-9d0a-b58f15e5cd08
---

## 定义

CerebroCortex 是一个仿生记忆系统（brain-analogous memory system），为 AI Agent 提供持久化、关联性、带情绪权重的记忆能力。它不是简单的向量数据库，而是模拟人脑海马体、杏仁核、前额叶等 9 个脑区的认知架构，支持记忆编码、关联、整合和「做梦」（离线巩固）。

别名：Cerebro、CerebroCore

## 关键要点

- **三后端存储**：SQLite（持久化图）+ igraph（内存图遍历）+ ChromaDB（向量搜索），无需 Neo4j，可在 Raspberry Pi 5 上运行

- **9 大脑区引擎**：丘脑（门控过滤）、杏仁核（情感分析）、颞叶（语义提取）、海马体（情景绑定）、联合皮层（自动关联）、小脑（程序性记忆）、前额叶（排序晋升）、新皮层（图式形成）、默认模式网络（Dream Engine）

- **6 种记忆类型**：情景记忆、语义记忆、程序性记忆、情感记忆、前瞻记忆、图式记忆

- **4 层记忆晋升**：感官层（6h 半衰期）→ 工作层（72h）→ 长期层（30 天）→ 皮层（永久）

- **动态激活系统**：结合 ACT-R 基线激活（幂律衰减）和 FSRS 可检索性（间隔重复曲线），加上向量相似度和显著性，四信号加权评分

- **Dream Engine**：6 阶段离线巩固——慢波睡眠回放、模式提取、图式形成、情绪再处理、修剪、REM 重组

- **多 Agent 支持**：SHARED / PRIVATE / THREAD 三种可见性，每个 Agent 独立做梦周期

- **MCP 原生**：40 个 MCP 工具，支持 Hermes Agent、Claude Code、OpenClaw 等框架

- MIT 许可，1639 Stars（截至 2026-04-29）

## 关联概念

- [ACT-R 激活模型](concepts/ACT-R 激活模型.md)

- [FSRS-6](concepts/FSRS-6.md)

- [Agent 记忆基础设施](concepts/Agent 记忆基础设施.md)

- [Karpathy LLM Wiki 方法论](concepts/Karpathy LLM Wiki 方法论.md)

- [Mercury](entities/Mercury.md)

- [Hermes Agent](entities/Hermes Agent.md)

## 来源引用

- [摘要：Why Karpathy's Second Brain Breaks at Agent Scale. How Mercury Solves It.](summaries/摘要：Why Karpathy's Second Brain Breaks at Agent Scale. How Mercury Solves It.md)（[原文](https://x.com/Ctrl_Alt_Zaid/status/2049082538686382397)）
