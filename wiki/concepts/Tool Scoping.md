---
title: Tool Scoping
type: concept
tags:
- Harness 工程
- 上下文管理
status: 草稿
confidence: medium
last_compiled: '2026-04-27'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/0c8366ec57074ce3bb4d36caa19d573c
notion_id: 0c8366ec-5707-4ce3-bb4d-36caa19d573c
---

## 定义

Tool Scoping 是 Agent Harness 设计中的一项核心原则：限制每一步暴露给模型的工具数量，只提供当前步骤真正需要的工具，而非一次性加载全部工具集。

## 关键要点

- **少即是多**：每个暴露给模型的工具都占用上下文窗口、增加决策分支、提高模型选错工具的概率；Vercel 砍掉 v0 中 80% 的工具后 Agent 性能反而提升

- **动态加载**：Claude Code 按当前步骤动态加载所需工具，将上下文占用降低 95%

- **认知负荷 vs 能力错觉**：工具多看似能力强，实际上是给模型增加认知负荷（cognitive load），表现为更多的幻觉和错误调用

- **实现方式**：按任务阶段分组工具、按角色/权限过滤工具、运行时根据上下文动态注入工具

## 关联概念

- [Agent Harness](concepts/Agent Harness.md)

- [Context Engineering](concepts/Context Engineering.md)

## 来源引用

- [摘要：Design principles for building an Agent harness](summaries/摘要：Design principles for building an Agent harness.md)（[原文](https://x.com/akshay_pachaar/status/2047671145475068038)）
