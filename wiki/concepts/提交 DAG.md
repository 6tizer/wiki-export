---
title: 提交 DAG
type: concept
tags:
- 多Agent协作
- Agent 协作模式
- Harness 工程
status: 审核中
confidence: medium
last_compiled: '2026-05-03'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/976aa243a0284e15a173085900cf3934
notion_id: 976aa243-a028-4e15-a173-085900cf3934
---

## 定义

提交 DAG 指由多个提交节点组成的有向无环图结构，用来表达并行实验、分叉结果与后续承接关系，而不强制收敛到单一主分支。

## 关键要点

- 适合 Agent 并行试验和异步提交结果

- 降低人工审核和手动合并的依赖

- 是 AgentHub 这类 Agent 原生协作工具的核心数据结构

## 来源引用

- [原文链接](https://x.com/Gorden_Sun/status/2031377609213530311)｜《AgentHub：Karpathy 为 AI Agent 重新设计的「GitHub」》｜来源条目：AgentHub：Karpathy 为 AI Agent 重新设计的「GitHub」
