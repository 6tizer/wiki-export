---
title: AgentOS
type: entity
tags:
- Harness 工程
- AI 产品
status: 草稿
confidence: high
last_compiled: '2026-04-29'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/b924f7559d504b03aa3c77b3e8246da6
notion_id: b924f755-9d50-4b03-aa3c-77b3e8246da6
---

## 定义

AgentOS 是由 Agno 团队开发的 Agent 生产服务平台，为多种 Agent 框架（Agno、Claude Agent SDK、LangGraph、DSPy）提供统一的生产级运行环境。它将 Agent 循环（harness）、沙箱（代码执行环境）和会话存储三层解耦，支持水平扩展、多租户认证、RBAC、调度、可观测性和 HITL 审批门控。

别名：Agno AgentOS

## 关键要点

- **统一多框架**：在同一个 AgentOS 实例中同时运行 Agno Agent、Claude Code Agent、LangGraph Agent 和 DSPy Agent，共享数据库、API 和 UI

- **三层分离架构**：Agent 循环（harness）、沙箱（sandbox）、会话存储（session storage）各自独立，可独立伸缩

- **生产级能力**：内置多用户 JWT 认证、RBAC、cron/事件驱动调度、全链路 tracing（含成本和工具调用）、流式/后台/批处理模式

- **HITL 审批门控**：通过 /run 和 /continue API 端点实现敏感工具调用的人工审批暂停/恢复

- **FastAPI 后端**：底层基于 FastAPI，支持云部署、水平扩展

## 适用场景

- 面向终端用户的 Agentic 产品（需要多用户、多租户、RBAC）

- 企业内部 Agent 平台（如 Slack/Discord/Telegram 集成）

- 需要在云环境中大规模并行运行 Agent 的团队

## 来源引用

- [摘要：AgentOS now supports Claude Code, LangGraph, and DSPy](summaries/摘要：AgentOS now supports Claude Code, LangGraph, and DSPy.md)（[原文](https://x.com/ashpreetbedi/status/2049511642946249143)）

## 关联概念

- [Agno](entities/Agno.md)

- [Agent Harness](concepts/Agent Harness.md)

- [Claude Agent SDK](entities/Claude Agent SDK.md)

- [LangGraph](entities/LangGraph.md)

- [DSPy](entities/DSPy.md)
