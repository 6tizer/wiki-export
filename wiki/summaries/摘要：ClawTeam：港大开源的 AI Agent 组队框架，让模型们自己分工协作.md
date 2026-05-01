---
title: 摘要：ClawTeam：港大开源的 AI Agent 组队框架，让模型们自己分工协作
type: summary
tags:
- 多Agent协作
- Agent 协作模式
- OpenClaw
status: 已审核
confidence: medium
last_compiled: '2026-04-11'
source_tags: Agent, OpenClaw, 自动化, LLM
source_article_url: https://www.notion.so/335701074b688169b177fafc872450a2
notion_url: https://www.notion.so/Tizer/bd159121319c443da263f4f7ea8e2767
notion_id: bd159121-319c-443d-a263-f4f7ea8e2767
---

### 一句话摘要

ClawTeam 的核心主张是让系统根据目标自动组建多 Agent 团队，而不是让用户手工定义全部角色和协作结构。

### 关键洞察

- 它通过 TaskBoard、InboxSystem 和 TeamRegistry 一类组件把协作流程显式化。

- 文件系统式通信让多 Agent 协作更接近结构化交接，而不是随意聊天。

- 这种框架在 ML 搜索和任务边界清晰的并行开发场景里更有优势。

- 真正的难点仍在冲突管理、上下文同步和任务拆分质量。

### 提取的概念

- [ClawTeam](entities/ClawTeam.md)

- [Agent Swarm Intelligence](concepts/Agent Swarm Intelligence.md)

- [TaskBoard](concepts/TaskBoard.md)

- [InboxSystem](concepts/InboxSystem.md)

### 原始文章信息

- 作者：Saccc_c

- 来源：X书签

- 发布时间：未明确披露

- 链接：[原文链接](https://x.com/Saccc_c/status/2034219625815347204)

### 个人评注

这篇内容和 Tizer 的多阶段内容流水线很契合。它提醒我们，真正可规模化的不是“一个更聪明的 Agent”，而是任务拆分、状态追踪和交接结构本身。 
