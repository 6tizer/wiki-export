---
title: Foundry Agent Service
type: entity
tags:
- Agent 框架
- 安全/隐私
status: 草稿
confidence: high
last_compiled: '2026-04-23'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/487a6d68132f4f0499397cb2dbca10a9
notion_id: 487a6d68-132f-4f04-9939-7cb2dbca10a9
---

## 定义

Foundry Agent Service 是微软在 Microsoft Foundry 中推出的托管 Agent 计算服务，核心主张是为每个 Agent 提供专属的企业级运行环境：独立沙箱、持久状态、内置身份与治理能力，并兼容不同的 harness 与 framework。

## 关键要点

- **专属运行环境**：不再把多个 Agent 混跑在同一个共享执行环境里，而是按 Agent 分配独立沙箱

- **支持长时任务**：通过持久状态保留文件、上下文与中间产物，适合跨会话与长周期任务

- **企业级治理**：把身份、权限、审计与治理能力前置到 Agent 基础设施层，而不是事后补丁

- **兼容现有生态**：强调可承载不同 Agent 框架与编排方式，而不强迫开发者重写模式

## 适用场景

- 长时间运行的 Coding Agent

- 需要审计链路的企业流程 Agent

- 需要独立隔离与权限边界的多 Agent 系统

## 来源引用

- [摘要：Foundry Hosted Agents：每个 Agent 都需要自己的“电脑”](summaries/摘要：Foundry Hosted Agents：每个 Agent 都需要自己的“电脑”.md)（[原文](https://x.com/satyanadella/status/2047033636923568440)）

## 关联概念

- [AI 沙箱](concepts/AI 沙箱.md)

- [Agent 身份基础设施](concepts/Agent 身份基础设施.md)
