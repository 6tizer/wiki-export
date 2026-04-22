---
title: Agent 可观测性
type: concept
tags:
- Agent 编排
status: 审核中
confidence: high
last_compiled: '2026-04-22'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/581efb118b0049588f2192179d5458cf
notion_id: 581efb11-8b00-4958-8f21-92179d5458cf
---

## 定义

Agent 可观测性是指主动了解和监控 AI Agent 运行状态、行为和输出质量的能力，包括日志、健康检查、告警和仪表盘等手段。

## 关键要点

- **日志位置**：Session 日志在 `~/.openclaw/agents/<agentId>/`，Cron 日志在 `~/.openclaw/cron/runs/`

- **健康检查 Agent**：配置每天 8 点的 Cron job，检查磁盘、Cron 执行状态、活跃 session 和频道连接

- **`sessions_history`**** 的深度用法**：不仅查进度，还能发现 prompt 问题、分析决策质量、找静默失败根因

- **告警设计关键**：「没有问题不要发消息」——避免告警疲劳

- **Canvas 仪表盘**：将 Cron 执行率、token 趋势、失败摘要等集中展示

## 来源引用

- [摘要：OpenClaw 进阶手册 Vol.3：跑稳之后，才是真的开始](summaries/摘要：OpenClaw 进阶手册 Vol.3：跑稳之后，才是真的开始.md)（[请致天下.AI](http://xn--ghqv4yd56a5mi.ai/)，2026-02-28）

- [摘要：像素风 AI 办公室——Agent 可视化状态监控](summaries/摘要：像素风 AI 办公室——Agent 可视化状态监控.md)（文本分析实验室，2026-03-03）

- [摘要：Driftwatch：30 秒看透你的 OpenClaw 智能体架构](summaries/摘要：Driftwatch：30 秒看透你的 OpenClaw 智能体架构.md)（GitHubDaily，2026-03-08）

- [摘要：ClawPort：为 OpenClaw 多智能体团队打造的可视化指挥中心](summaries/摘要：ClawPort：为 OpenClaw 多智能体团队打造的可视化指挥中心.md)（GitHub_Daily，X书签）

- [摘要：一个冷门无人提的冷知识却又是程序员常识：](summaries/摘要：一个冷门无人提的冷知识却又是程序员常识：.md)（X书签）

- [摘要：一个冷门无人提的冷知识却又是程序员常识：](summaries/摘要：一个冷门无人提的冷知识却又是程序员常识：.md)（[原文](https://x.com/LawrenceW_Zen/status/2044437995269591195)，LawrenceW_Zen，2026-04）

## 关联概念

- [ClawPort](entities/ClawPort.md)

- [OpenClaw](entities/OpenClaw.md)

- [可追溯日志体系](concepts/可追溯日志体系.md)
