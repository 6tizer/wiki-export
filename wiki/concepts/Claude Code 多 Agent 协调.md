---
title: Claude Code 多 Agent 协调
type: concept
tags:
- 多Agent协作
- 链上协议
- Agent 协作模式
status: 审核中
confidence: high
last_compiled: '2026-04-27'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/e94517d5d8664abdb92f23d74c77b99c
notion_id: e94517d5-d866-4abd-b92f-23d74c77b99c
---

## 定义

Claude Code 多 Agent 协调是 Claude Code 支持多个 Agent 实例协同工作的架构机制，采用 leader-worker 模型实现复杂任务的并行分解与执行。

## 关键要点

- **Leader-Worker 模型**：一个主 Agent 负责任务规划与分配，多个 Worker Agent 并行执行子任务

- **4 种 backend**：支持 4 种不同的 Agent 执行后端，适应不同的运行环境与资源约束

- **权限同步**：多 Agent 场景下需要跨实例同步权限状态，防止 Worker Agent 执行未授权操作

- **与插件系统集成**：多 Agent 协调可通过插件系统（marketplace、MCPB）进行扩展

## 来源引用

- 来源：[@gerrox 对 Claude Code 内部架构的深度分析](https://github.com/roger2ai/claude-code-internals)（2026-04-01）

- 原始推文：[https://x.com/gerrox/status/2039137055746543860](https://x.com/gerrox/status/2039137055746543860)

- [摘要：深度使用半年，我总结了 Claude Code 的架构、治理与工程实践](summaries/摘要：深度使用半年，我总结了 Claude Code 的架构、治理与工程实践.md)｜X书签文章｜原文链接：[https://x.com/HiTw93/status/2032091246588518683](https://x.com/HiTw93/status/2032091246588518683)

- [原文链接](https://x.com/IndieDevHailey/status/2032273129582850230)｜《Agency Agents：用 147 个 AI 专家角色，把 Claude Code 变成一整家公司》｜来源条目：[摘要：Agency Agents：用 147 个 AI 专家角色，把 Claude Code 变成一整家公司](summaries/摘要：Agency Agents：用 147 个 AI 专家角色，把 Claude Code 变成一整家公司.md)

- [原文链接](https://x.com/sitinme/status/2033418986898207072)｜《everything-claude-code：把 Claude Code 调教成 AI 工程团队的完整配置系统》｜来源条目：[摘要：everything-claude-code：把 Claude Code 调教成 AI 工程团队的完整配置系统](summaries/摘要：everything-claude-code：把 Claude Code 调教成 AI 工程团队的完整配置系统.md)

- [原文链接](https://x.com/akshay_pachaar/status/2033456347354996815)｜《Claude Subagents vs Agent Teams：别过早引入多智能体，复杂度需要被赚到》｜来源条目：[摘要：Claude Subagents vs Agent Teams：别过早引入多智能体，复杂度需要被赚到](summaries/摘要：Claude Subagents vs Agent Teams：别过早引入多智能体，复杂度需要被赚到.md)

- 《Claude Code 源码泄露深度解析：一个开发者如何让它重新编译运行》｜X书签文章｜来源条目：[摘要：Claude Code 源码泄露深度解析：一个开发者如何让它重新编译运行](summaries/摘要：Claude Code 源码泄露深度解析：一个开发者如何让它重新编译运行.md)

- 《Claude Code 源码泄露始末：一个开发者如何让它真正跑起来，并拆解其内部架构》｜X书签文章｜来源条目：摘要：Claude Code 源码泄露始末：一个开发者如何让它真正跑起来，并拆解其内部架构

- [原文链接](https://x.com/gerrox/status/2039137055746543860)｜《Claude Code 源码泄露深度解析：一个开发者如何让它重新编译运行》｜源文章：[摘要：Claude Code 源码泄露深度解析：一个开发者如何让它重新编译运行](summaries/摘要：Claude Code 源码泄露深度解析：一个开发者如何让它重新编译运行.md)

- [原文链接](https://x.com/gerrox/status/2039137055746543860)｜《Claude Code 源码泄露始末：一个开发者如何让它真正跑起来，并拆解其内部架构》｜源文章：摘要：Claude Code 源码泄露始末：一个开发者如何让它真正跑起来，并拆解其内部架构

## 关联概念

- [agency-agents](entities/agency-agents.md)
