---
title: Agent 与执行环境分离
type: concept
tags:
- Agent 编排
- Coding Agent
status: 草稿
confidence: high
last_compiled: '2026-04-15'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/b345b317c0df44309d20b3adf5d8cc53
notion_id: b345b317-c0df-4430-9d20-b3adf5d8cc53
---

## 定义

Agent 与执行环境分离，是指把负责推理、规划与调度的 Agent 与负责文件操作、命令执行、代码运行的 Sandbox 或容器环境拆开设计，让两者通过工具接口协作，而不是把 Agent 直接塞进执行容器里。

## 关键要点

- 核心价值是让 Agent 生命周期、执行环境生命周期与模型选择彼此解耦

- 这样更容易做容错恢复、快照切换、安全隔离和多模型接入

- 这种设计通常把 Agent 视为“大脑”，把 Sandbox 视为“手”

- 它已经成为企业级 Coding Agent 和托管式 Agent 基础设施里的收敛方向

## 关联概念

- [Open Agents](entities/Open Agents.md)

- [Harness Engineering](concepts/Harness Engineering.md)

- [Sandbox 抽象](concepts/Sandbox 抽象.md)

- [Claude Managed Agents](entities/Claude Managed Agents.md)

## 来源引用

- [原文链接](https://x.com/dotey/status/2043904844608532640)｜《Vercel 开源了 Open Agents，一个用来搭建企业自有编程 Agent 平台的参考实现。》｜来源条目：[摘要：Vercel 开源了 Open Agents，一个用来搭建企业自有编程 Agent 平台的参考实现。](summaries/摘要：Vercel 开源了 Open Agents，一个用来搭建企业自有编程 Agent 平台的参考实现。.md)
