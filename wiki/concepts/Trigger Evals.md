---
title: Trigger Evals
type: concept
tags: []
status: 审核中
confidence: medium
last_compiled: '2026-04-20'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/ba410b58d7e94022b80902d7de08b098
notion_id: ba410b58-d7e9-4022-b809-02d7de08b098
---

## 定义

Trigger Evals 是针对 Agent 路由层设计的一类评测方法：通过一组真实用户输入样本，验证 resolver 是否会把任务派发到正确的 skill、角色或上下文入口。

## 关键要点

- 它评测的重点不是输出内容本身，而是“是否由正确能力被触发”

- 能同时发现 **false negative**（该触发却没触发）和 **false positive**（触发了错误技能）两类路由问题

- 相比修改代码，很多问题只需要调整 markdown 描述、触发词或 resolver 表即可修复

- 适合在技能数量变多、用户表达方式持续变化的系统里做持续回归测试

## 关联概念

- [Resolver](concepts/Resolver.md)

- [Thin Harness, Fat Skills](concepts/Thin Harness, Fat Skills.md)

- [Context Rot](concepts/Context Rot.md)

## 来源引用

- [摘要：Resolvers: The Routing Table for Intelligence](summaries/摘要：Resolvers- The Routing Table for Intelligence.md)（[原文](https://x.com/garrytan/status/2044479509874020852)）
