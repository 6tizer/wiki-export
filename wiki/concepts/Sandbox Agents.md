---
title: Sandbox Agents
type: concept
tags:
- Agent 安全
- Harness 工程
status: 审核中
confidence: high
last_compiled: '2026-04-20'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/96a940e45234480780da7e43537732aa
notion_id: 96a940e4-5234-4807-80da-7e43537732aa
---

## 定义

Sandbox Agents 是 OpenAI Agents SDK 中为 Agent 提供可控计算环境的一种能力形态，让 Agent 在独立沙盒里访问文件系统、运行命令、保留工作区状态，并把真实产物留在环境中。

## 关键要点

- 它把 Agent 编排层与实际执行环境拆开，让“思考”和“动手”分离

- 适合需要文件、进程、浏览器、凭证或持久工作区的长时任务

- 重点价值不是单纯执行命令，而是让 Agent 能留下可检查、可恢复、可继续的工作产物

- 安全隔离是核心前提，避免把执行边界绑定到宿主机的偶然环境

## 来源引用

- [原文链接](https://x.com/jxnlco/status/2044469127696556153)｜《Sandboxes are coming to the Agents SDK》｜源文章：OpenAI Agents SDK 沙盒：让 AI Agent 真正「留下工作成果」

- [摘要：OpenAI Agents SDK：三个原语，搭出你的多 Agent 系统](summaries/摘要：OpenAI Agents SDK：三个原语，搭出你的多 Agent 系统.md)（[原文](https://x.com/_vmlops/status/2045533747857240290)）

## 关联概念

- [OpenAI Agents SDK](entities/OpenAI Agents SDK.md)

- [Sandbox 抽象](concepts/Sandbox 抽象.md)

- [Agent Harness](concepts/Agent Harness.md)

- [Compaction](concepts/Compaction.md)

- [Agent Handoff](concepts/Agent Handoff.md)

- [Agent Traces](concepts/Agent Traces.md)

- [会话记忆](concepts/会话记忆.md)
