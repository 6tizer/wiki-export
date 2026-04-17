---
title: '摘要：Now in research preview: routines in Claude Code.'
type: summary
tags:
- Coding Agent
- Agent 编排
status: 已审核
confidence: medium
last_compiled: '2026-04-15'
source_tags: ''
source_article_url: https://www.notion.so/343701074b68814e9813c8d270913160
notion_url: https://www.notion.so/7062762165d14794826f3563865835cf
notion_id: 70627621-65d1-4794-826f-3563865835cf
---

## 一句话摘要

Claude Code 推出了处于 research preview 阶段的 Routines，把 prompt、代码仓库和连接器配置成可在云端按计划、API 调用或事件触发自动运行的任务。

## 关键洞察

- 这次更新把 Claude Code 从本地交互式编程助手，进一步扩展成可异步执行的自动化工作流入口。

- Routine 的核心配置单元是 prompt、repo 和 connectors，强调“一次配置，多次复用”。

- 触发方式覆盖定时调度、API 调用和事件响应，说明它不仅是定时任务，也面向事件驱动场景。

- 任务运行在 Anthropic 的 web 基础设施上，不再依赖用户本地电脑持续在线。

## 提取的概念

- [Claude Code](entities/Claude Code.md)

- [Claude Code Routines](concepts/Claude Code Routines.md)

- [托管 Agent](concepts/托管 Agent.md)

## 原始文章信息

- 作者：@claudeai

- 来源：X书签

- 发布时间：2026-04-14

- 原文链接：[https://x.com/claudeai/status/2044095086460309790](https://x.com/claudeai/status/2044095086460309790)

## 个人评注

这条更新对 Tizer 的意义，不是单一功能点，而是说明 **Coding Agent 正在从“手动调用的工具”走向“可托管的异步执行层”**。如果后续支持更稳定的事件源、审计和回滚，它会很适合接入代码巡检、定时报表、Webhook 触发修复这类 HITL 工作流。
