---
title: Credential Exfiltration
type: concept
tags:
- 安全/隐私
- Agent 技能
status: 草稿
confidence: high
last_compiled: '2026-04-23'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/111cf98d6b134871bf2779ac3974410d
notion_id: 111cf98d-6b13-4871-bf27-79ac3974410d
---

## 定义

Credential Exfiltration 指攻击者通过提示注入、恶意网页、受污染文档或其它操纵手段，诱导 Agent 把本可访问的凭证泄露给外部攻击者的安全问题。

## 关键要点

- 在 Agent 场景里，凭证外泄常常不是传统意义上的“代码漏洞”，而是由模型可操纵性带来的系统性风险。

- 一旦凭证被带出执行环境，后续往往会演变成数据外泄、越权访问或横向移动等连锁问题。

- 仅仅缩短凭证生命周期可以降低损失窗口，但不能阻止 Agent 本身把凭证说出去、发出去或带出去。

- 因此，很多 Agent 安全方案的重点不再是检测泄露，而是从架构上避免 Agent 直接接触密钥。

## 来源引用

- [摘要：Agent Vault: The Open Source Credential Proxy and Vault for Agents](summaries/摘要：Agent Vault- The Open Source Credential Proxy and Vault for Agents.md)（[原文](https://x.com/dangtony98/status/2046982854710857762)）
