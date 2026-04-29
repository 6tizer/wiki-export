---
title: 摘要：AgentOS now supports Claude Code, LangGraph, and DSPy
type: summary
tags:
- Harness 工程
- AI 产品
- 多Agent协作
status: 已审核
confidence: high
last_compiled: '2026-04-29'
source_tags: ''
source_article_url: https://www.notion.so/351701074b68811baef5d50c1007d054
notion_url: https://www.notion.so/Tizer/10145f6c481f4fcbabe2d647c81b3ed6
notion_id: 10145f6c-481f-4fcb-abe2-d647c81b3ed6
---

## 一句话摘要

AgentOS 发布对 Claude Code（via Claude Agent SDK）、LangGraph 和 DSPy 的集成支持，实现在同一生产服务中运行多种 Agent 框架，并阐明了 SDK 与 Harness 的本质区别以及 Agent 生产服务的三层分离架构。

## 关键洞察

- **SDK vs Harness 二分法**：SDK 提供构建 Agent 的原语和可组合循环（如 Agno）；Harness 是围绕模型设计的完整执行环境（如 Claude Code、Codex、Cursor Background Agent），两者互补而非互斥

- **AgentOS 统一多框架**：Agno、Claude Agent SDK、LangGraph、DSPy 四种 Agent 架构可在同一个 AgentOS 实例中共享数据库、API 和 UI，通过 FastAPI 后端水平扩展

- **Agent 生产服务三层分离**：借鉴 Anthropic「Scaling Managed Agents」经验，将 Agent 循环（harness）、沙箱（sandbox）、会话存储（session storage）解耦为独立可伸缩层

- **Harness ≠ Backend**：Agent 循环会频繁崩溃，这是 Agent 的天性；后端服务管理 harness，harness 崩溃时服务继续运行

- **HITL 审批流**：通过 /run 启动 Agent → Agent 运行至需要人工审批时暂停 → /continue 传入输入恢复执行，实现敏感工具调用的门控

## 提取的概念

- [AgentOS](entities/AgentOS.md)（新建 entity：Agno 的 Agent 生产服务平台）

- [Agno](entities/Agno.md)（已有 entity：Agent 开发 SDK）

- [Agent Harness](concepts/Agent Harness.md)（已有 concept：Agent 执行底座）

- [Claude Agent SDK](entities/Claude Agent SDK.md)（已有 entity：Anthropic 的 Agent SDK）

- [LangGraph](entities/LangGraph.md)（已有 entity：LangChain 有状态编排框架）

- [DSPy](entities/DSPy.md)（已有 entity：语言模型程序优化框架）

## 原始文章信息

- **作者**：@ashpreetbedi（Ashpreet Bedi，Agno 创始人）

- **来源**：X 推文

- **发布时间**：2026-04-29

- **链接**：[原文](https://x.com/ashpreetbedi/status/2049511642946249143)

## 个人评注

本文的核心启示在于 Agent 生产化的方向：将 harness/sandbox/session 三层解耦是规模化运行 Agent 的关键。对 OpenClaw 而言，AgentOS 的多框架统一思路值得参考——如果 OpenClaw 的 Skill 执行引擎需要接入不同模型/框架的 Agent，类似的统一 API 层 + HITL 审批门控模式可以直接复用。三层分离也呼应了 Thin Harness, Fat Skills 的理念：harness 层保持轻量、可替换，核心价值沉淀在 Skill 和 Memory 层。
