---
title: Agent-as-Customer 模式
type: concept
tags:
- 商业/生态
- Agent 安全
status: 草稿
confidence: medium
last_compiled: '2026-04-30'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/74260aaca03249a5b0a87b82fba874d9
notion_id: 74260aac-a032-49a5-b0a8-7b82fba874d9
---

## 定义

Agent-as-Customer 模式是指 AI Agent 不再仅作为用户的代理工具调用 API，而是直接作为云平台的「客户」，自主完成账户注册、付费订阅、资源购买和凭证获取的全流程。这标志着从「人类使用工具」到「Agent 成为基础设施消费者」的范式转变。

## 关键要点

- Agent 拥有独立的身份（非共享人类凭证）、预算、权限范围和审计链路

- 人类可在关键节点保留审批权（HITL），但全流程无需手动仪表盘操作

- Cloudflare 是首个实践此模式的大型平台，Agent 可完成：创建账户→付费订阅→注册域名→获取 API Token→部署代码

- 与 Stripe Projects 协议配合，解决了 Agent 自主消费的支付安全问题

- 被评论者称为 "Agent-first economy" 和 "Agent Led Growth" 的起点

## 与 Tizer 工作流的关联

该模式直接影响 OpenClaw 的架构设想——如果 Agent 能自主成为云服务客户，OpenClaw 的 Agent 可自动部署和扩展基础设施，减少人工运维环节。

## 来源引用

- [摘要：Cloudflare 宣布 Agent 可自主注册账户、购买域名和部署代码](summaries/摘要：Cloudflare 宣布 Agent 可自主注册账户、购买域名和部署代码.md)（[原文](https://x.com/Cloudflare/status/2049545195914498139)）
