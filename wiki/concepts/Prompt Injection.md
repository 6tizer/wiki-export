---
title: Prompt Injection
type: concept
tags:
- 安全/隐私
- Agent 技能
status: 审核中
confidence: high
last_compiled: '2026-04-23'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/38d1f42c1f21444681c7946d57686037
notion_id: 38d1f42c-1f21-4446-81c7-946d57686037
---

## 定义

Prompt Injection 是指攻击者通过网页内容、文档、工具返回值或其它外部输入，把恶意指令嵌入 Agent 的上下文中，从而诱导模型偏离原始任务、泄露敏感信息或执行越权操作。

## 关键要点

- 它是 Agent 场景里最根本的攻击面之一，因为很多系统都会把外部世界的文本直接送进模型上下文。

- 与传统注入攻击不同，Prompt Injection 利用的是模型对自然语言指令的服从倾向，而不是程序语法解析缺陷。

- 只要 Agent 仍然能直接读取高价值密钥、Token 或会话信息，Prompt Injection 就可能把这些能力转化为实际损害。

- 因此，安全设计往往要把重点放在最小权限、能力隔离和敏感操作代理，而不是只依赖提示词防护。

## 来源引用

- [摘要：Agent Vault: The Open Source Credential Proxy and Vault for Agents](summaries/摘要：Agent Vault- The Open Source Credential Proxy and Vault for Agents.md)（[原文](https://x.com/dangtony98/status/2046982854710857762)）
