---
title: Review-Apply 双车道架构
type: concept
tags:
- Harness 工程
status: 草稿
confidence: high
last_compiled: '2026-04-28'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/ca127d1c25084d3f83c6b42bc048993f
notion_id: ca127d1c-2508-4d3f-83c6-b42bc048993f
---

## 定义

Review-Apply 双车道架构是一种将「审查/提案」与「执行/变更」严格分离的自动化维护模式。Review Lane 只生成建议和报告，不触碰生产状态；Apply Lane 根据已存储的审查结果，在条件仍然成立时才执行实际变更。这种分离确保了审计追踪的完整性和操作的安全性。

## 关键要点

- **Review 只读不写**：审查阶段生成 Markdown 报告和置信度评分，不执行任何关闭/合并操作

- **Apply 验证后执行**：执行阶段重新校验报告是否仍然有效（未被修改），只处理高置信度提案

- **审计友好**：每个决策都有对应的持久化报告文件，支持事后回溯

- **幂等与安全**：Apply 可重复运行，已处理的条目自动归档

- **独立节奏**：两个 Lane 可以不同频率运行（如 Review 每日、Apply 每 15 分钟）

## 典型应用

- ClawSweeper：OpenClaw 的 GitHub Issue/PR 自动维护

- 适用于任何需要大规模自动化决策但要求人工可审计的场景

## 来源引用

- [摘要：Workflow status](summaries/摘要：Workflow status.md)（[原文](https://x.com/steipete/status/2047982647264059734)）

## 关联概念

- [ClawSweeper](entities/ClawSweeper.md)

- [Codex](entities/Codex.md)

- [OpenClaw](entities/OpenClaw.md)
