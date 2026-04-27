---
title: 摘要：Vercel 开源了 Open Agents，一个用来搭建企业自有编程 Agent 平台的参考实现。
type: summary
tags:
- Coding Agent
- Agent 框架
status: 已审核
confidence: high
last_compiled: '2026-04-27'
source_tags: ''
source_article_url: https://www.notion.so/343701074b6881bca10fd8370a39821e
notion_url: https://www.notion.so/5d9828ec1ae549e69aca7a8f9f34d8d8
notion_id: 5d9828ec-1ae5-49e6-9aca-7a8f9f34d8d8
---

## 一句话摘要

Open Agents 是 Vercel 开源的企业自建编程 Agent 平台参考实现，它把 Agent、Sandbox 与模型选择解耦，给技术团队提供了一套可以直接 fork 的 Coding Agent 基础架构。

## 关键洞察

- 这不是一个面向所有人的通用编程助手，而是一套面向企业自建 AI 软件工厂的参考实现。

- 它把系统拆成前端、持久化 Agent 工作流、Sandbox 执行环境三层，核心原则是 **Agent 不住在 Sandbox 里**。

- 这种外部工具操控 Sandbox 的设计，让 Agent 生命周期、执行环境生命周期、模型选择可以分别演进。

- 相比 Anthropic 的托管式 Managed Agents，Open Agents 更强调源码控制权、模型开放性和自部署能力。

- 对正在搭建内部 Coding Agent 的团队来说，Open Agents 的价值不只是功能完整，更在于把一套可落地的架构范式直接公开出来。

## 提取的概念

- [Open Agents](entities/Open Agents.md)

- [Harness Engineering](concepts/Harness Engineering.md)

- [Sandbox 抽象](concepts/Sandbox 抽象.md)

- [Agent 与执行环境分离](concepts/Agent 与执行环境分离.md)

- [Claude Managed Agents](entities/Claude Managed Agents.md)

## 原始文章信息

- 作者：@dotey

- 来源：X书签

- 发布时间：2026-04-14

- 原文链接：[https://x.com/dotey/status/2043904844608532640](https://x.com/dotey/status/2043904844608532640)

- 源文章：Vercel Open Agents：企业自建编程 Agent 平台的开源参考实现

## 个人评注

这篇材料对 Tizer 的价值，不在于直接照搬 Vercel 的产品形态，而在于验证了一条很清晰的工程路线：把 Agent 调度、执行环境、模型接入拆开处理。对后续 OpenClaw、HITL 协作流和内容管线之外的 Coding Agent 基础设施设计，这是一份很值得反复参考的样板。
