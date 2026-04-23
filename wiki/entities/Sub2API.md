---
title: Sub2API
type: entity
tags:
- 开发工具
- 商业/生态
status: 审核中
confidence: medium
last_compiled: '2026-04-24'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/d7f12402e4da4c7cb32185ea7a46883a
notion_id: d7f12402-e4da-4c7c-b321-85ea7a46883a
---

## 定义

Sub2API 是一个开源的 AI API 中转站程序，支持将 ChatGPT Business 账号的网页版会话转换为标准 OpenAI 兼容 API，实现自建低成本 AI API 中转服务。

## 核心功能

- 将 GPT Business 账号池转为标准 OpenAI 化 API

- 支持多账号轮询，平衡负载

- 配合 Cloudflare WARP 代理防风控

- 配合 Cloudflare Tunnel 隐藏真实服务器 IP

- 数据存储依赖 Neon PostgreSQL，缓存依赖 Upstash Redis

- 补充支持 Claude、OpenAI、Gemini、Antigravity、Codex 等多服务统一接入

- 强调 API Key 分发、Token 级精确计费、粘性会话、并发控制与支付集成等运营能力

## 部署要点

- Neon 连接串必须去掉 `-pooler` 后缀

- WARP SOCKS5 代理必须开启，否则被 OpenAI 风控

- Tunnel URL 配置为 `localhost:8080` 而非 443

## 来源引用

- [摘要：一篇教你从0搭建中转站！超高性价比 token 自由，爽用 GPT-5.4](summaries/摘要：一篇教你从0搭建中转站！超高性价比 token 自由，爽用 GPT-5.4.md)

- [摘要：用开源中转统一接入Claude/OpenAI/Gemini：Sub2API核心功能解析](summaries/摘要：用开源中转统一接入Claude-OpenAI-Gemini：Sub2API核心功能解析.md)（[原文](https://mp.weixin.qq.com/s?__biz=Mzk0MjcxOTM2Nw%3D%3D&mid=2247502925&idx=1&sn=c5f44b38c0c75259cd2c498915216ee2&chksm=c299a356e1d1244e5ffda156d54336f50b545a4015f3df40854f080b1caedf90457af895153b#rd)）
