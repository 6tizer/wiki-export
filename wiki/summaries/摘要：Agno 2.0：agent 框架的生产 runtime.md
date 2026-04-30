---
title: 摘要：Agno 2.0：agent 框架的生产 runtime
type: summary
tags:
- Harness 工程
- AI 产品
status: 已审核
confidence: high
last_compiled: '2026-04-30'
source_tags: ''
source_article_url: https://www.notion.so/352701074b6881a3aa8ee0b143c332b4
notion_url: https://www.notion.so/Tizer/d18f34d93bf444f392a7209817525092
notion_id: d18f34d9-3bf4-44f3-92a7-209817525092
---

## 一句话摘要

Agno 2.0 将自身定位从 Agent 框架转型为 Agent Runtime，通过 stateless 架构和统一 API 层，把异构 Agent 框架（Claude Agent SDK、LangGraph、DSPy）包装成生产级服务，用一个 Postgres 替代一整套基础设施。

## 关键洞察

- **Runtime ≠ Framework**：Agno 不做更聪明的 Agent，而是让别人写的 Agent 能在生产环境活下来——类比 Gunicorn 之于 Flask 的关系

- **多框架统一封装**：Claude Agent SDK、LangGraph、DSPy 三种异构框架经 Agno 包装后代码形状高度对齐，团队可把「选框架」和「上生产」两个决策拆开

- **彻底 stateless 化是关键前提**：Agno 2.0 把所有状态压进数据库，自身完全无状态——这不是优化，而是为了能 wrap 各种 stateful 框架（LangGraph 的 checkpoint、Claude SDK 的 session）做的必要条件

- **一个 Postgres 收敛全部基础设施**：sessions、memory、knowledge embedding（pgvector）、traces、schedules 全部塞进同一个库，最小部署只需一个容器 + 一个 Postgres

- **50+ 生产级 endpoint 开箱即用**：run/stream、session 管理、memory、knowledge、approvals（人工审批）、cron scheduling、JWT 鉴权，按 user/session 自动隔离

## 提取的概念

- [Agno](entities/Agno.md)（主体产品，前身 Phidata，39.7k star）

- [Agent Runtime](concepts/Agent Runtime.md)（runtime vs framework 的定位区分）

- [LangGraph](entities/LangGraph.md)（被 wrap 的 stateful 框架之一）

- [DSPy](entities/DSPy.md)（被 wrap 的结构化抽取框架）

- [pgvector](concepts/pgvector.md)（Agno 用同一个 Postgres + pgvector 收敛向量检索能力）

## 原始文章信息

- **作者**：向量猫

- **来源**：微信公众号

- **发布时间**：2026-04-28

- **原文链接**：[Agno 2.0：agent 框架的生产 runtime](https://mp.weixin.qq.com/s?__biz=MzYzNzg4ODc5NQ%3D%3D&mid=2247484325&idx=1&sn=bfcbaed95b8834a6c5a70b8eaae52df6&chksm=f1f8a3fe9687d8c180430e6658e5df0133606c5823bcce395bf7d09c3e763436b84445935a36#rd)

## 个人评注

对 Tizer 的工作流有直接参考价值：OpenClaw 体系中如果需要把不同框架写的 Agent 统一上线，Agno 的 AgentOS 模式（stateless runtime + 状态外置到 Postgres）是一个现成的工程参考。特别是「人工审批流」（approvals endpoint）和 Tizer 一直关注的 HITL 模式高度契合。此外，Agno 用单一 Postgres（含 pgvector）替代多套基础设施的思路，也值得在 content pipeline 的 RAG 部分借鉴——降低运维复杂度的同时保留向量检索能力。
