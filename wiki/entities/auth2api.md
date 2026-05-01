---
title: auth2api
type: entity
tags:
- CLI 工具
- AI 产品
status: 审核中
confidence: high
last_compiled: '2026-04-12'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/e67685c7a843420393b43926f396b93e
notion_id: e67685c7-a843-4203-93b4-3926f396b93e
---

## 定义

auth2api 是一个把 Claude OAuth 登录态转换为 OpenAI 兼容 API 的轻量代理项目，面向本地自用或自托管接入场景。

## 核心要点

- 复用 Claude 账号授权，暴露标准 `/v1/chat/completions` 等接口

- 重点能力是模拟 Claude Code CLI 请求特征，降低异常流量暴露度

- 适合 Cursor、Cline、Continue 等需要兼容 OpenAI 接口的工具链

## 来源引用

- [原文链接](https://x.com/0xAA_Science/status/2042151683283878146)｜《auth2api：用 Claude Max 订阅伪装成真实 CLI 用户，自建 OpenAI 兼容 API 代理》｜来源页：auth2api：用 Claude Max 订阅伪装成真实 CLI 用户，自建 OpenAI 兼容 API 代理
