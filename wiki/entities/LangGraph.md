---
title: LangGraph
type: entity
tags:
- Agent 编排
status: 审核中
confidence: high
last_compiled: '2026-04-30'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/c6734e1129dd49d4b7912730d55bfbe4
notion_id: c6734e11-29dd-49d4-b791-2730d55bfbe4
---

## 定义

LangGraph 是 LangChain 团队推出的有状态 Agent 编排框架，用有向图（StateGraph）描述 Agent 工作流——每个节点是处理步骤，边是条件跳转或并行分支。支持循环、分支、Human-in-the-Loop 等复杂控制流，被 Klarna、Replit、Elastic 等公司用于生产环境。

**GitHub**：langchain-ai/langgraph | License: MIT | 持续活跃维护

## 核心特性

- **StateGraph**：基于状态图的工作流定义，支持复杂分支和循环

- **interrupt()**：实现 Human-in-the-Loop 人工介入节点

- **Store**：长期记忆持久化支持

- **Multi-Agent**：langgraph-supervisor 支持多 Agent 协作编排

- **流式输出**：支持 token 级和消息级双模式流

- **LangGraph Cloud**：官方托管服务

## 适用场景

- 金融分析 Agent（多步骤数据拉取→分析→报告）

- 学术文献综述（多 Agent 协同处理）

- 需要 Human-in-the-Loop 的审批工作流

- 任何有状态、可回溯的复杂 Agent 任务

## 来源引用

- [摘要：Agent Service Toolkit：用 LangGraph + FastAPI + Streamlit 快速搭建生产级 AI Agent 服务](summaries/摘要：Agent Service Toolkit：用 LangGraph + FastAPI + Streamlit 快速搭建生产级 AI Agent 服务.md)

- LangGraph AI 金融分析师 Agent 实践

- Nexus AI 多 Agent 学术研究系统

- Web3 AI Agent 真相分析

- [原文链接](https://x.com/sitinme/status/2033171859144048745)｜《SwarmClaw：从管理一个 AI 助手到指挥一支 AI 团队》｜来源条目：[摘要：SwarmClaw：从管理一个 AI 助手到指挥一支 AI 团队](summaries/摘要：SwarmClaw：从管理一个 AI 助手到指挥一支 AI 团队.md)

- [原文链接](https://x.com/sitinme/status/2036370938099335335)｜《Open-SWE：LangChain 开源的异步编程 Agent，让 AI 像队友一样提 PR》｜来源条目：[摘要：Open-SWE：LangChain 开源的异步编程 Agent，让 AI 像队友一样提 PR](summaries/摘要：Open-SWE：LangChain 开源的异步编程 Agent，让 AI 像队友一样提 PR.md)

- [原文链接](https://mp.weixin.qq.com/s?__biz=MzIzNjc1NzUzMw%3D%3D&mid=2247882749&idx=2&sn=2d4f10773aa251563dacfab3852c341d&chksm=e90834c479dc425ef1224f6ce2a17375a87c3e52109831d2865c2e45b32888aa931ce30fa9e0#rd)｜《有人把巴菲特芒格炼化成Agent，然后开源了…》｜来源条目：[摘要：有人把巴菲特芒格炼化成Agent，然后开源了…](summaries/摘要：有人把巴菲特芒格炼化成Agent，然后开源了….md)

- [摘要：AgentOS now supports Claude Code, LangGraph, and DSPy](summaries/摘要：AgentOS now supports Claude Code, LangGraph, and DSPy.md)（[原文](https://x.com/ashpreetbedi/status/2049511642946249143)）

- [摘要：Agno 2.0：agent 框架的生产 runtime](summaries/摘要：Agno 2.0：agent 框架的生产 runtime.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzYzNzg4ODc5NQ%3D%3D&mid=2247484325&idx=1&sn=bfcbaed95b8834a6c5a70b8eaae52df6&chksm=f1f8a3fe9687d8c180430e6658e5df0133606c5823bcce395bf7d09c3e763436b84445935a36#rd)）

## 关联概念

- [Open-SWE](entities/Open-SWE.md)

- [异步编程 Agent](concepts/异步编程 Agent.md)

- [原文链接](https://x.com/sitinme/status/2036370938099335335)｜《Open-SWE：LangChain 开源的异步编程 Agent，让 AI 像队友一样提 PR》｜来源条目：[摘要：Open-SWE：LangChain 开源的异步编程 Agent，让 AI 像队友一样提 PR](summaries/摘要：Open-SWE：LangChain 开源的异步编程 Agent，让 AI 像队友一样提 PR.md)

- [原文链接](https://x.com/AYi_AInotes/status/2043033290014147063)｜《LangChain创始人Harrison Chase这篇，直接点透了现在所有AI Agent的核心问题。》｜来源条目：Agent Harness 与记忆：LangChain 创始人点透了 AI Agent 的核心命题

- [AI Hedge Fund](entities/AI Hedge Fund.md)

- [React Flow](entities/React Flow.md)

- [AgentState](concepts/AgentState.md)

- [投资大师 Agent 化](concepts/投资大师 Agent 化.md)
