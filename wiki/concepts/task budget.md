---
title: task budget
type: concept
tags:
- Coding Agent
status: 审核中
confidence: medium
last_compiled: '2026-04-23'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/a26cfca5fb9f45c6a71b0627ea53601a
notion_id: a26cfca5-fb9f-45c6-a71b-0627ea53601a
---

## 定义

task budget 是 Claude Code 里把任务可用 token 预算显式暴露给 Agent 的控制机制，让模型在执行过程中感知剩余预算，并据此调整搜索、规划与执行强度。

## 关键要点

- 它把原本隐性的 token 消耗约束前置到 Agent 决策层，使模型不只是被人监督，也开始“自我约束”。

- 在产品哲学上，task budget 延续了 Claude Code 的副驾驶路线：核心不是放权给 Agent，而是让 Agent 在人的边界内更稳定地工作。

- 它适合被理解为一种执行治理机制，而不只是计费显示功能，因为预算感知会直接影响任务拆解与策略选择。

## 来源引用

- [摘要：【万字】CC vs OpenClaw vs Hermes：一文深入拆解三大 Agent 框架](summaries/摘要：【万字】CC vs OpenClaw vs Hermes：一文深入拆解三大 Agent 框架.md)（[原文](https://mp.weixin.qq.com/s?__biz=MjM5NjE3NjYzMw%3D%3D&mid=2247496422&idx=1&sn=811535695480b3dedead76bdd49ebfc0&chksm=a707de0ce8531ae0d9d8a14dd5c1029fc10a9cf68cd3421d8de580646f70da173af4f671ec62#rd)）

## 关联概念

- [Claude Code](entities/Claude Code.md)

- [记忆分层架构](concepts/记忆分层架构.md)
