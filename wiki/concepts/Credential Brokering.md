---
title: Credential Brokering
type: concept
tags:
- 安全/隐私
- Agent 技能
status: 审核中
confidence: high
last_compiled: '2026-04-23'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/e0420f624ba64f3b9640591aed1f73a0
notion_id: e0420f62-4ba6-4f3b-9640-591aed1f73a0
---

## 定义

Credential Brokering 是一种把凭证保留在独立控制层、由代理或中间层在请求发出时动态注入认证信息的安全模式，核心目标是让 Agent 获得访问能力而不是直接拿到密钥本身。

## 关键要点

- 它把“给 Agent 发凭证”改写成“替 Agent 代理凭证”，本质上是在能力授权和密钥持有之间加一道隔离层。

- 这种模式特别适合不可信、非确定性、容易被提示注入操纵的 Agent 执行环境。

- 统一的 brokering 层可以顺带承载审计、限流、策略控制和凭证撤销，而不必在每个工具或 SDK 中重复实现。

- 与短期凭证、自动轮换等方案相比，它解决的是“凭证是否暴露给 Agent”而不只是“凭证暴露后能用多久”。

## 来源引用

- [摘要：Agent Vault: The Open Source Credential Proxy and Vault for Agents](summaries/摘要：Agent Vault- The Open Source Credential Proxy and Vault for Agents.md)（[原文](https://x.com/dangtony98/status/2046982854710857762)）
