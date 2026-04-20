---
title: Agent OS
type: concept
tags:
- Agent 框架
- Agent 编排
status: 审核中
confidence: high
last_compiled: '2026-04-20'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/231115259903408ca77760fd94041e1d
notion_id: 23111525-9903-408c-a777-60fd94041e1d
---

## 定义

Agent OS（智能体操作系统）是一种将 AI Agent 作为操作系统级进程或统一执行层来管理的架构范式，提供调度、资源管理、隔离和安全机制，使 Agent 能够像系统服务一样自主可靠地运行。

## 关键要点

- 核心区别：普通 Agent 框架是应用层胶水代码，Agent OS 提供内核级或基础设施级能力

- Agent 作为进程：拥有独立的调度、资源计量、沙箱隔离，可随时终止

- 关键特性：调度器不依赖用户输入就能触发 Agent，对比传统对话式 Agent 更强调持续执行

- 代表项目：OpenFang（Rust 实现，13.7 万行代码）

- 与传统 Agent 框架（LangGraph、CrewAI、AutoGen）的本质区别，是从「应用层」提升到「系统层」思考

- 在 CREAO 的语境里，Agent OS 也被描述为连接 Gmail、Slack 等工具的统一执行层，强调从“对话”直接走向“执行”

## 来源引用

- [摘要：一个 Rust 写的 Agent OS——OpenFang](summaries/摘要：一个 Rust 写的 Agent OS——OpenFang.md)

- [摘要：OpenClaw正在成为新的交互入口，AI投资人：这4个生态位，短期内会爆发机会](summaries/摘要：OpenClaw正在成为新的交互入口，AI投资人：这4个生态位，短期内会爆发机会.md)

- [摘要：Agent 不是你该做的事：OS 与 Agent-native 应用的分野](summaries/摘要：Agent 不是你该做的事：OS 与 Agent-native 应用的分野.md)

- [摘要：CREAO Pioneer Program: Run It All.](summaries/摘要：CREAO Pioneer Program- Run It All.md)
