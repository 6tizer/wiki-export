---
title: 长时运行 Agent
type: concept
tags:
- Harness 工程
status: 草稿
confidence: medium
last_compiled: '2026-04-28'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/f7c5e006da714a82992bab327f7827cd
notion_id: f7c5e006-da71-4a82-992b-ab327f7827cd
---

## 定义

长时运行 Agent（Long-running Agents）是指需要持续运行 20 小时以上的 AI Agent 系统。在金融、研究等场景中，Agent 需要长时间自主执行任务，面临鲁棒性、状态管理和自我纠错等核心挑战。

## 关键要点

- Abundance 团队将 20+ 小时 Agent 运行的鲁棒性列为核心技术挑战之一

- 长时运行中 Agent 可能偏离目标、陷入循环、与自身之前推理矛盾

- 需要解决的问题包括：状态持久化、上下文窗口管理、错误恢复、Token 消耗控制

- PranaAlpha 等公司也在研究 Agent 系统的可靠性（reliability）、确定性（determinism）、自纠错（self-correction）和演化（evolution）四大属性

## 来源引用

- [摘要：Abundance: Building an AI Capital Allocator](summaries/摘要：Abundance- Building an AI Capital Allocator.md)（[原文](https://x.com/apoorva_mehta/status/2047709094048657713)）
