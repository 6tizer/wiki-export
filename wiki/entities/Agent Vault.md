---
title: Agent Vault
type: entity
tags:
- Agent 安全
- MCP 协议
status: 审核中
confidence: high
last_compiled: '2026-04-23'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/de7a944a3f3f457d8ce96586a4613c93
notion_id: de7a944a-3f3f-457d-8ce9-6586a4613c93
---

## 定义

Agent Vault 是 Infisical 推出的开源 HTTP 凭证代理与保险库，目标是在不把明文凭证交给 Agent 的前提下，让 Agent 安全访问外部服务。

## 关键要点

- 面向 Agent 的凭证使用场景设计，强调代理注入而非直接取回密钥。

- 支持 API、CLI、SDK、MCP 等多种交互方式，适配本地 Agent 与沙箱 Agent。

- 通过代理层记录请求日志，并为后续访问控制与审计提供基础。

- 可与集中式密钥管理系统配合，用于短期凭证与轮换场景。

## 来源引用

- [摘要：Agent Vault never reveals vault-stored credentials to agents](summaries/摘要：Agent Vault never reveals vault-stored credentials to agents.md)（[原文](https://x.com/dangtony98/status/2046983159502586323)）

- [摘要：Agent Vault: The Open Source Credential Proxy and Vault for Agents](summaries/摘要：Agent Vault- The Open Source Credential Proxy and Vault for Agents.md)（[原文](https://x.com/dangtony98/status/2046982854710857762)）

- [摘要：A dream come true for every human anxious about their agents leaking secrets.](summaries/摘要：A dream come true for every human anxious about their agents leaking secrets.md)（[原文](https://x.com/dangtony98/status/2047036513536622918)）
