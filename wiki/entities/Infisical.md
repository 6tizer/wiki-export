---
title: Infisical
type: entity
tags:
- 安全/隐私
- 开发工具
status: 草稿
confidence: high
last_compiled: '2026-04-23'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/cf07cde15c3348b9857709c20bfcfd2b
notion_id: cf07cde1-5c33-48b9-8577-09c20bfcfd2b
---

## 定义

Infisical 是一个集中式密钥管理与安全基础设施产品，在本文语境中充当 Agent Vault 背后的上游秘密存储与轮换系统。

## 关键要点

- 提供动态密钥、自动轮换、审计轨迹等传统 secrets management 能力。

- 可以与 Agent Vault 组合，形成“集中密钥库 + 近端凭证代理”的双层架构。

- 在 Agent 安全体系中，Infisical 负责管理凭证生命周期，Agent Vault 负责靠近执行侧的代理注入。

## 来源引用

- [摘要：Agent Vault never reveals vault-stored credentials to agents](summaries/摘要：Agent Vault never reveals vault-stored credentials to agents.md)（[原文](https://x.com/dangtony98/status/2046983159502586323)）
