---
title: AutoHarness
type: concept
tags:
- Harness 工程
- 代码生成
- Agent 安全
status: 草稿
confidence: high
last_compiled: '2026-04-25'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/03d9b6b149ab42abb24dd99d0c410c28
notion_id: 03d9b6b1-49ab-42ab-b24d-d99d0c410c28
---

## 定义

AutoHarness 是一种自动生成代码级 Harness 的方法，用来为 Agent 或语言模型生成动作过滤器、动作验证器或策略代码，从而降低非法动作并提升任务执行表现。

## 关键要点

- 把 Harness 设计建模为程序搜索问题，而不是手工规则编写问题

- 可在 action-filter、action-verifier、policy 三种模式下工作

- 通过环境反馈、错误案例和代码修复循环不断优化约束代码

- 说明专用 Harness 能显著提升模型在严格环境中的稳定性与胜率

## 来源引用

- [摘要：分享2篇最新Harness论文，一篇谷歌，一篇微软](summaries/摘要：分享2篇最新Harness论文，一篇谷歌，一篇微软.md)

## 关联概念

- [Harness Engineering](concepts/Harness Engineering.md)
