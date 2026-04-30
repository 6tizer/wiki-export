---
title: Spec and Verify
type: concept
tags:
- Harness 工程
- 代码生成
status: 草稿
confidence: medium
last_compiled: '2026-04-30'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/074930debd5347109f179b628bdf5a06
notion_id: 074930de-bd53-4710-9f17-9b628bdf5a06
---

## 定义

Spec and Verify 是一种 Agent 代码生产流程：先由 Agent 根据规格说明（Spec）生成实现代码，再通过自动化验证（Verify）确认代码行为符合预期。Warp 创始人 Zach Lloyd 认为，经过良好调优的 Agent 基础设施（如 Oz）在长期内将比人类更好地管理代码质量。

## 关键要点

- 核心思想：将软件开发拆分为「规格定义」和「行为验证」两个阶段，中间由 Agent 完成实现

- 在 Open Agentic Development 场景下，Spec and Verify 是保障公开协作代码质量的关键机制

- Zach Lloyd 表示，有了该流程后，他对公开构建的信心超过了纯人工开源协作

- 与传统 TDD（测试驱动开发）的区别：Spec 层面更偏向产品行为描述，而非单元测试

## 关联概念

- [Open Agentic Development](concepts/Open Agentic Development.md)：该流程是 Open Agentic Development 的质量保障环节

- [Oz](entities/Oz.md)：执行 Spec and Verify 的 Agent 基础设施

- [Warp](entities/Warp.md)：首个大规模实践该流程的产品

## 来源引用

- [摘要：The open agentic development loop](summaries/摘要：The open agentic development loop.md)（[原文](https://x.com/zachlloydtweets/status/2049562997551694113)）
