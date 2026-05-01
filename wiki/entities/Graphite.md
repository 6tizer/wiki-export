---
title: Graphite
type: entity
tags:
- 加密资产
- Agent 安全
status: 审核中
confidence: high
last_compiled: '2026-04-15'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/2aad0cc114e94355b7212c8f611ab584
notion_id: 2aad0cc1-14e9-4355-b721-2c8f611ab584
---

## 定义

Graphite 是一类面向高频协作开发的 PR 工作流工具，用于管理分支、堆叠 PR 和合并队列，帮助团队在高吞吐交付下保持审查与合并秩序。

## 关键要点

- 通过 merge queue 在合并前自动 rebase 到 main 并重跑 CI，降低主干污染风险

- 支持 stacked PR，让大改动可以拆成连续的小提交，便于 AI 与人工协同审查

- 适合与确定性 CI/CD 流水线配合，提升高频发布场景下的稳定性

- 在本文案例里，它承担的是“把大量变更安全并回主干”的执行层职责

## 来源引用

- [原文链接](https://mp.weixin.qq.com/s?__biz=MzA4ODg0NDkzOA%3D%3D&mid=2247513974&idx=1&sn=1e142be25de6da66b34468c27c35885e&chksm=91c1bf78a361ff3f5a8ca448d82101f6ea0af2facd8dc130189e8816899ac0a780e3f1fb1705#rd)｜微信文章：从六周一版本到一天八部署：一家25人公司的AI重构全记录
