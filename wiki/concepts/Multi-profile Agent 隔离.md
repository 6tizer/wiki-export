---
title: Multi-profile Agent 隔离
type: concept
tags:
- Agent 协作模式
- Harness 工程
status: 草稿
confidence: medium
last_compiled: '2026-05-03'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/ac4cbe24b5994f0e9309b39c99466ba5
notion_id: ac4cbe24-b599-4f0e-9309-b39c99466ba5
---

## 定义

Multi-profile Agent 隔离是一种 Agent 运行环境的设计模式，通过为每个 Agent 角色（profile）提供独立的 scripts、workspace 和 data 目录，实现工作环境、记忆、文档索引和定时任务的完全隔离。

## 关键要点

- 每个 profile 目录结构：`profiles/{name}/scripts/`、`profiles/{name}/workspace/`、`profiles/{name}/data/`

- workspace 内包含独立的 `CLAUDE.md`、`.claude/skills/` 和 `.claude/agents/`，Claude Code 自动发现

- data 目录包含独立的 `memory.db`（Holographic Memory）、`doc-index.db`（DocStore）、`sessions.json` 和 `cron-jobs.json`

- 同一 Orb 实例可同时服务多个 profile，通过路由层将消息分发到正确的 profile 环境

- 系统级 skills（`.claude/skills/`）通过 `--add-dir` 跨 profile 共享，但 profile 级数据不交叉

## 适用场景

- 同一组织内多个 Agent 角色（如 Alice 负责代码审查、Bob 负责客户支持）共享同一基础设施但需独立记忆和权限

- 长期运行的 Agent 需要在隔离环境中积累各自领域知识

## 来源引用

- [摘要：Orb 自建记忆与路由的 Claude Code 封装框架](summaries/摘要：Orb 自建记忆与路由的 Claude Code 封装框架.md)（[原文](https://x.com/karry_viber/status/2050483217858482374)）

## 关联概念

- [Orb](entities/Orb.md)

- [Holographic Memory](concepts/Holographic Memory.md)

- [MCP Permission Relay](concepts/MCP Permission Relay.md)
