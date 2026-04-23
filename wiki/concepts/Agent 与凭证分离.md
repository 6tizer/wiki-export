---
title: Agent 与凭证分离
type: concept
tags:
- 安全/隐私
- Agent 编排
status: 草稿
confidence: high
last_compiled: '2026-04-23'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/567b5803dbe94e53a6c81f6190a82175
notion_id: 567b5803-dbe9-4e53-a6c8-1f6190a82175
---

## 定义

Agent 与凭证分离是指把 Agent 的推理与执行能力，与密钥存储、签发、注入等凭证能力拆分到不同安全边界中的架构原则。

## 关键要点

- Agent 不再直接拥有 secrets，而是只获得受限的调用能力。

- 这种拆分有助于形成更清晰的信任边界与审计链路。

- 它不能完全消除数据外泄风险，但能显著减少凭证外泄后的爆炸半径。

- 该模式正在成为 Agent 基础设施的通用方向之一。

## 来源引用

- [摘要：Agent Vault never reveals vault-stored credentials to agents](summaries/摘要：Agent Vault never reveals vault-stored credentials to agents.md)（[原文](https://x.com/dangtony98/status/2046983159502586323)）
