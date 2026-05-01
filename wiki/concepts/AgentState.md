---
title: AgentState
type: concept
tags: []
status: 审核中
confidence: medium
last_compiled: '2026-04-26'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/6c379df202d14a338d00a5f346a6d64a
notion_id: 6c379df2-02d1-4a33-8d00-a5f346a6d64a
---

## 定义

AgentState 是多 Agent 系统中用于共享上下文与中间结果的统一状态容器。不同 Agent 通过读写同一份状态，在节点之间传递分析结果、决策线索与执行进度。

## 关键要点

- 让多 Agent 工作流具备统一上下文，而不是各自孤立运行

- 适合在图式编排框架中作为节点之间的数据交换层

- 在 AI Hedge Fund 中，各 Agent 共享同一个 AgentState 数据字典，以保证状态一致并支持下游引用上游结果

## 来源引用

- [原文链接](https://mp.weixin.qq.com/s?__biz=MzIzNjc1NzUzMw%3D%3D&mid=2247882749&idx=2&sn=2d4f10773aa251563dacfab3852c341d&chksm=e90834c479dc425ef1224f6ce2a17375a87c3e52109831d2865c2e45b32888aa931ce30fa9e0#rd)｜[摘要：有人把巴菲特芒格炼化成Agent，然后开源了…](summaries/摘要：有人把巴菲特芒格炼化成Agent，然后开源了….md)

## 关联概念

- [LangGraph](entities/LangGraph.md)

- [多 Agent 投研框架](concepts/多 Agent 投研框架.md)
