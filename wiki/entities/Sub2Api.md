---
title: Sub2Api
type: entity
tags:
- 开发工具
status: 草稿
confidence: medium
last_compiled: '2026-04-11'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/d7f12402e4da4c7cb32185ea7a46883a
notion_id: d7f12402-e4da-4c7c-b321-85ea7a46883a
---

## 定义

Sub2Api 是一个开源的 AI API 中转站程序，支持将 ChatGPT Business 账号的网页版会话转换为标准 OpenAI 兼容 API，实现自建低成本 AI API 中转服务。

## 核心功能

- 将 GPT Business 账号池转为标准 OpenAI 化 API

- 支持多账号轮询，平衡负载

- 配合 Cloudflare WARP 代理防风控

- 配合 Cloudflare Tunnel 隐藏真实服务器 IP

- 数据存储依赖 Neon PostgreSQL，缓存依赖 Upstash Redis

## 部署要点

- Neon 连接串必须去掉 `-pooler` 后缀

- WARP SOCKS5 代理必须开启，否则被 OpenAI 风控

- Tunnel URL 配置为 `localhost:8080` 而非 443

## 来源引用

- [摘要：一篇教你从0搭建中转站！超高性价比 token 自由，爽用 GPT-5.4](summaries/摘要：一篇教你从0搭建中转站！超高性价比 token 自由，爽用 GPT-5.4.md)
