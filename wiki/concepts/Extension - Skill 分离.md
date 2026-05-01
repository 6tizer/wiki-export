---
title: Extension / Skill 分离
type: concept
tags:
- Harness 工程
- 链上协议
- 上下文管理
status: 审核中
confidence: high
last_compiled: '2026-04-26'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/f744898cf33044db960d20c1491f2da4
notion_id: f744898c-f330-44db-960d-20c1491f2da4
---

## 定义

Extension / Skill 分离是一种 Coding Agent 架构思路：把**可复用的执行基础设施**沉淀为 extension，把**面向具体任务的领域知识与操作策略**放进 skill，从而让同一套实验引擎可以服务多个优化场景。

## 关键要点

- extension 负责通用能力，如运行实验、记录结果、显示仪表盘等基础设施

- skill 负责领域语义，如目标指标、文件范围、候选优化方向与上下文约束

- 这种拆分让工具层更稳定，任务层更易迁移，也更方便在不同项目间复用

- 对长期运行的 Agent 系统来说，这有助于降低上下文耦合，提升可维护性

## 来源引用

- [摘要：Shopify 开源 pi-autoresearch，用自主实验循环持续挖掘性能优化](summaries/摘要：Shopify 开源 pi-autoresearch，用自主实验循环持续挖掘性能优化.md)（[原文](https://x.com/ShopifyEng/status/2044477537200550383)）

## 关联概念

- [autoresearch](entities/autoresearch.md)
