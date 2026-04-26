---
title: 摘要：auth2api：用 Claude Max 订阅伪装成真实 CLI 用户，自建 OpenAI 兼容 API 代理
type: summary
tags:
- Coding Agent
- 安全/隐私
status: 已审核
confidence: high
last_compiled: '2026-04-26'
source_tags: LLM, Agent, 自动化
source_article_url: https://www.notion.so/33e701074b6881e498e1d9699ef0f9f1
notion_url: https://www.notion.so/02ad180c67534982804276a719195739
notion_id: 02ad180c-6753-4982-8042-76a719195739
---

## 一句话摘要

auth2api 把 Claude Max 订阅的 OAuth 登录态转成 OpenAI 兼容 API，核心卖点是通过复刻官方 CLI 请求特征，让自用代理更轻量也更隐蔽。

## 关键洞察

- 它解决的不是“造一个新模型”，而是“把已有订阅能力接到现有 AI 工具链里”。

- 项目最关键的护城河是对官方客户端请求特征的精细模拟，而不是普通的接口转发。

- 对 Cursor、Cline、Continue 这类依赖 OpenAI 兼容接口的工具来说，协议兼容性比功能堆叠更重要。

- 这类方案天然处在平台条款与风控灰区，稳定性取决于检测规则是否变化。

## 提取的概念

- [auth2api](entities/auth2api.md)

- [OpenAI 兼容 API 代理](concepts/OpenAI 兼容 API 代理.md)

- [用户指纹复刻](concepts/用户指纹复刻.md)

## 原始文章信息

- 作者：@0xAA_Science

- 来源：X书签

- 发布时间：2026-04-09

- 链接：[https://x.com/0xAA_Science/status/2042151683283878146](https://x.com/0xAA_Science/status/2042151683283878146)

## 个人评注

这类“订阅能力适配层”很适合 Tizer 观察 Coding Agent 基础设施的灰度创新，尤其和 OpenClaw、Claude Code 周边工具链的兼容策略有关。
