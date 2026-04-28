---
title: Agent 可观测性
type: concept
tags:
- Agent 协作模式
- Agent 安全
- OpenClaw
status: 审核中
confidence: high
last_compiled: '2026-04-28'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/581efb118b0049588f2192179d5458cf
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

- [摘要：OpenAI 刚发的 Workspace Agent，开源版来了](summaries/摘要：OpenAI 刚发的 Workspace Agent，开源版来了.md)（[原文](https://x.com/xiaohu/status/2047521587122106376)）

- [摘要：Goodbye agents that silently hallucinate in production.](summaries/摘要：Goodbye agents that silently hallucinate in production.md)（[X Thread](https://x.com/hasantoxr/status/2047636566680760576)）

- [摘要：OpenClaw大更新，AI智能体不再是黑箱！官方口号：少点神秘](summaries/摘要：OpenClaw大更新，AI智能体不再是黑箱！官方口号：少点神秘.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzI3MTA0MTk1MA%3D%3D&mid=2652695800&idx=2&sn=a3ceb186e13822d88ac69f6d18f3243c&chksm=f0662743dcb86ac6d163039eca81d628426e080671ef217bbb3f8aa2380e9ae8e88b90685cf7#rd)）

## 关联概念

- [ClawPort](entities/ClawPort.md)

- [OpenClaw](entities/OpenClaw.md)

- [可追溯日志体系](concepts/可追溯日志体系.md)

- [OpenTelemetry](concepts/OpenTelemetry.md)

- [插件冷查找表](concepts/插件冷查找表.md)
