---
title: Agno
type: entity
tags:
- AI 产品
- 多Agent协作
status: 草稿
confidence: medium
last_compiled: '2026-04-30'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/bcd9cd835edc419fa1d2086684456fe3
notion_id: bcd9cd83-5edc-419f-a1d2-086684456fe3
---

## 定义

Agno（原 Phidata，2025 年改名）是一个 Agent Runtime 平台，定位为 **runtime for agentic software**——不做更聪明的 Agent 框架，而是把已有框架（Claude Agent SDK、LangGraph、DSPy）统一包装成生产级 API。提供 AgentOS 运行环境，包含 UI、多用户会话管理、定时任务调度和 FastAPI 应用部署。GitHub 39.7k star、5.3k fork。Scout 是基于 Agno 构建的开源 Context Agent。

## 关键要点

- 提供 AgentOS：包含 UI、多用户 session、scheduled tasks、FastAPI 部署

- AgentOS 控制台：[os.agno.com](http://os.agno.com/)

- GitHub 组织：[https://github.com/agno-agi](https://github.com/agno-agi)

- 支持 Docker 部署

- Scout 是其旗舰开源项目

- **Agno 2.0 架构转型**：彻底 stateless 化，所有状态压进 Postgres，横向扩展只需加 pod + LB

- 多框架统一封装：Claude Agent SDK / LangGraph / DSPy 包装后代码形状高度对齐

- 50+ endpoint 开箱即用：run/stream、session、memory、knowledge、approvals、schedules、JWT 鉴权

- 单一 Postgres（含 pgvector）替代 sessions + 向量库 + tracing + scheduler + auth 多套基础设施

## 来源引用

- [摘要：Meet Scout. The open-source company brain](summaries/摘要：Meet Scout. The open-source company brain.md)（[原文](https://x.com/ashpreetbedi/status/2049180168200106150)）

- [摘要：AgentOS now supports Claude Code, LangGraph, and DSPy](summaries/摘要：AgentOS now supports Claude Code, LangGraph, and DSPy.md)（[原文](https://x.com/ashpreetbedi/status/2049511642946249143)）

- [摘要：Agno 2.0：agent 框架的生产 runtime](summaries/摘要：Agno 2.0：agent 框架的生产 runtime.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzYzNzg4ODc5NQ%3D%3D&mid=2247484325&idx=1&sn=bfcbaed95b8834a6c5a70b8eaae52df6&chksm=f1f8a3fe9687d8c180430e6658e5df0133606c5823bcce395bf7d09c3e763436b84445935a36#rd)）

## 关联概念

- [Agent Runtime](concepts/Agent Runtime.md)

- [LangGraph](entities/LangGraph.md)

- [DSPy](entities/DSPy.md)

- [pgvector](concepts/pgvector.md)
