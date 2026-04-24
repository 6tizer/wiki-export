---
title: Open Agents
type: entity
tags:
- Coding Agent
- Agent 框架
status: 审核中
confidence: high
last_compiled: '2026-04-15'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/a7f40e28fff948bcb38f5fb19f1b0296
notion_id: a7f40e28-fff9-48bc-b38f-5fb19f1b0296
---

## 定义

Open Agents 是 Vercel 开源的企业自建编程 Agent 平台参考实现，提供对话式编码、沙箱执行、仓库操作与 PR 流程等基础能力，目标是让团队可以在自有代码仓库、知识体系与内部流程中运行 Coding Agent。

## 关键要点

- 面向企业自建，而不是开箱即用的通用 SaaS Agent

- 架构上将前端、持久化 Agent 工作流、Sandbox 执行环境拆分为相对独立的层

- Agent 通过工具从外部操作 Sandbox，而不是直接运行在 Sandbox 内部

- 支持仓库克隆、分支操作、自动提交、发 PR、快照恢复、会话分享与语音输入

- 模型层保持开放，可以接入不同 LLM

## 关联概念

- [Harness Engineering](concepts/Harness Engineering.md)

- [Sandbox 抽象](concepts/Sandbox 抽象.md)

- [Agent 与执行环境分离](concepts/Agent 与执行环境分离.md)

- [Claude Managed Agents](entities/Claude Managed Agents.md)

- [模型中立](concepts/模型中立.md)

## 来源引用

- [原文链接](https://x.com/dotey/status/2043904844608532640)｜《Vercel 开源了 Open Agents，一个用来搭建企业自有编程 Agent 平台的参考实现。》｜源文章：Vercel Open Agents：企业自建编程 Agent 平台的开源参考实现
