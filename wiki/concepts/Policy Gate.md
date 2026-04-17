---
title: Policy Gate
type: concept
tags:
- 安全/隐私
- Agent 编排
status: 草稿
confidence: high
last_compiled: '2026-04-16'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/c54f5b4deac644aba0dccbfe93ab356a
notion_id: c54f5b4d-eac6-44ab-a0dc-cbfe93ab356a
---

## 定义

Policy Gate 是按角色设置的权限门控机制，用来限制不同 Agent profile 的可读范围、可写范围、可执行动作和审批边界，确保研究、写作、工程、编排等职责各自运行在最小必要权限内。

## 关键要点

- 研究型 profile 应偏只读

- 写作型 profile 应限制输出目录和敏感数据访问

- 工程型 profile 可执行测试，但关键提交仍需上级审批

- 编排型 profile 负责扩权、审批和高成本动作的最终把关

## 来源引用

- [原文链接](https://x.com/nyk_builderz/status/2044472463279710344)｜《The Ultimate Hermes Guide - from one agent to a 4-profile team that still feels coherent on day 30》｜源文章：Hermes 多 Agent 团队：如何让四个角色在第 30 天还保持分工清晰

## 关联概念

- [Hermes Agent](entities/Hermes Agent.md)

- [AGENTS.md](concepts/AGENTS.md.md)

- [Handoff 文档](concepts/Handoff 文档.md)
