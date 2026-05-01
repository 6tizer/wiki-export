---
title: Outbox 模式
type: concept
tags:
- 知识管理
- 上下文管理
status: 审核中
confidence: high
last_compiled: '2026-04-16'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/2240f5a11f124351b6b6b15c9e521b24
notion_id: 2240f5a1-1f12-4351-b6b6-b15c9e521b24
---

## 定义

Outbox 模式是一种保证业务状态写入与事件投递能够协同完成的工程模式。系统先把状态变更与待发送事件一起可靠落地，再由独立消费者按偏移量增量读取和确认，从而降低分布式事件丢失或重复处理带来的风险。

## 核心要点

- **状态先落地，事件后外发**：适合需要可靠事件流的知识系统与多组件架构

- **支持幂等消费**：消费端可以按 offset 拉取、ack 确认，便于增量同步

- **增强可观测性**：每次 ingest、更新、查询或写页都能沉淀为可追踪事件

- **适合桥接外部系统**：可把知识库变化同步到知识图谱、分析系统或其他消费者

## 关联概念

- [llm-wiki](entities/llm-wiki.md)

- [异步事件驱动编排](concepts/异步事件驱动编排.md)

- [Karpathy LLM Wiki 方法论](concepts/Karpathy LLM Wiki 方法论.md)

## 来源引用

- [原文链接](https://mp.weixin.qq.com/s?__biz=MzkxNzY0OTA4Mg%3D%3D&mid=2247493206&idx=1&sn=7080809308368860641fd4df6601bef9&chksm=c0a8ea2ad24191e6e6e084a08eacab4b318f12dd484d75fe35bb554e96c6e9906e407e998911#rd)｜《Karpathy 提出了 LLM Wiki，我用 Rust 把它造出来了，还打通了 MemPalace 知识图谱》｜源文章：Karpathy 提出了 LLM Wiki，我用 Rust 把它造出来了，还打通了 MemPalace 知识图谱
