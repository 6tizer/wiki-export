---
title: One-Eval
type: entity
tags:
- 模型评测
- AI 设计
- Agent 协作模式
status: 审核中
confidence: high
last_compiled: '2026-04-24'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/28b74f199e5947efbd09507b9571e375
notion_id: 28b74f19-9e59-47ef-bd09-507b9571e375
---

## 定义

One-Eval 是北京大学 DCAI 团队开源的交互式大模型自动化评测系统，能够从自然语言需求出发自动规划 benchmark、准备数据、执行评测并生成分析报告。

## 关键要点

- 它把评测从“手工配配置”升级为“需求驱动的工作流执行”。

- 支持在关键节点暂停并等待用户确认，体现 Human-In-The-Loop 设计。

- 强调全链路可追溯，便于定位 Prompt、解析、裁判和结果异常。

- 适用于代码、数学、RAG、长上下文与 Agent 任务等多类评测场景。

## 关联概念

- [DataFlow](entities/DataFlow.md)

- [Human-In-The-Loop](concepts/Human-In-The-Loop.md)

- [Global State 数据总线架构](concepts/Global State 数据总线架构.md)

- [Benchmark Gallery](concepts/Benchmark Gallery.md)

- [Metric Library](concepts/Metric Library.md)

## 来源引用

- [摘要：DeepSeek-V4 发布 10 小时，北大开源项目实现了自动化评测！](summaries/摘要：DeepSeek-V4 发布 10 小时，北大开源项目实现了自动化评测！.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzIyNjM2MzQyNg%3D%3D&mid=2247722249&idx=1&sn=7e9f29cb43e6948fe35c0a1435f013d8&chksm=e909fc8f9ecba3b58d11840fbdb88bf7db327e9a06421ac4903412691391c0edb1ef97cc7696#rd)）
