---
title: Lifecycle Hooks
type: concept
tags:
- Harness 工程
- Agent 协作模式
- 知识管理
status: 审核中
confidence: high
last_compiled: '2026-04-23'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/29bf93a3a4674b9d85b08a7177795166
notion_id: 29bf93a3-a467-4b9d-85b0-8a7177795166
---

## 定义

Lifecycle Hooks 是 Harness 在关键执行节点注入自定义逻辑的扩展机制，允许团队在不改动核心运行时的前提下，把审计、审批、策略控制与工作流自动化挂接到 Agent 生命周期中。

## 关键要点

- 常见触发时机包括工具执行前、工具执行后、会话恢复前后等阶段。

- 它让企业可以把合规、安全、日志与组织规则外接到 Harness，而不必 fork 整套系统。

- Hook 通常通过结构化输入输出协议工作，因此能够用不同语言实现并独立演化。

## 来源引用

- [摘要：What is an Agent Harness](summaries/摘要：What is an Agent Harness.md)（[原文](https://x.com/aparnadhinak/status/2046980769747533830)）

## 关联概念

- [Agent Harness](concepts/Agent Harness.md)

- [Agent Hooks](concepts/Agent Hooks.md)

- [Command Hooks](concepts/Command Hooks.md)

- [Prompt Hooks](concepts/Prompt Hooks.md)
