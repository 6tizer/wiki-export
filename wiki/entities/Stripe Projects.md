---
title: Stripe Projects
type: entity
tags:
- 商业/生态
- Agent 安全
status: 草稿
confidence: medium
last_compiled: '2026-04-30'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/ace5da50a27f4586bd68a248639c3dc0
notion_id: ace5da50-a27f-4586-bd68-a248639c3dc0
---

## 定义

Stripe Projects 是 Stripe 推出的新协议，允许 AI Agent 以编程方式完成注册、订阅付费、获取凭证等全流程，无需人工输入信用卡或手动操作仪表盘。它通过 token 化支付机制（不向 Agent 暴露原始卡号）和默认 $100/月的消费上限，实现安全可控的 Agent 自主消费。

别名：Stripe Agent Payment Protocol

## 关键要点

- 基于支付 token 而非原始信用卡信息，Agent 只获得作用域受限的凭证

- 默认 $100 USD/月消费限额，用户可自行上调或设置预算告警

- Stripe 作为身份提供者和编排器，负责 OAuth/OIDC 身份验证

- Cloudflare 是首个集成 Stripe Projects 的平台，Agent 可一键完成账户创建→订阅→域名注册→API Token 获取→代码部署

- 任何使用 Stripe 的平台均可接入此协议，不限于 Cloudflare

## 来源引用

- [摘要：Cloudflare 宣布 Agent 可自主注册账户、购买域名和部署代码](summaries/摘要：Cloudflare 宣布 Agent 可自主注册账户、购买域名和部署代码.md)（[原文](https://x.com/Cloudflare/status/2049545195914498139)）

- [摘要：Vibedeploy with Stripe Projects, now available to everyone](summaries/摘要：Vibedeploy with Stripe Projects, now available to everyone.md)（[原文](https://x.com/stripe/status/2049528193368137908)）
