---
title: iLink 协议
type: concept
tags:
- OpenClaw
status: 审核中
confidence: high
last_compiled: '2026-04-27'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/83521dfc78f64ffa8626c4dc93d54061
notion_id: 83521dfc-78f6-4ffa-8626-c4dc93d54061
---

## 定义

iLink 协议是微信官方推出的 AI Agent 接入协议，通过云端中继服务实现微信与本地 AI Agent 的双向消息通道。它本质是一套 HTTP 长轮询 + Token 认证的消息通道，接口跑在 `ilinkai.weixin.qq.com`。

## 核心机制

- **认证**：调用 `ilink/bot/get_bot_qrcode` 获取二维码，扫码后通过 `ilink/bot/get_qrcode_status` 长轮询返回 `bot_token`

- **收消息**：`ilink/bot/getupdates` HTTP 长轮询，每条消息携带 `context_token` 关联会话上下文

- **发消息**：`ilink/bot/sendmessage`，带上 `bot_token` 认证和 `context_token` 即可回复

## 关键特性

- 通道与模型无关：OpenClaw、Claude Code、Codex 都可从同一管道接入

- 官方安全通道，无封号风险（区别于之前的野路子方案）

- 支持通过 ACP 协议的 Agent 直接桥接

## 生态项目

- `@tencent-weixin/openclaw-weixin`：官方 OpenClaw 插件

- `claude-code-wechat-channel`：Claude Code 桥接插件（开源）

- `weixin-agent-gateway`：多 Agent 统一入口

- `weclaw`、`vibe-remote`、`wechatbot`：社区增强项目

## 关联概念

- [HermesClaw](entities/HermesClaw.md)

- [OpenClaw](entities/OpenClaw.md)

## 来源引用

- [摘要：微信官方接入龙虾，我顺手给接上了 Claude Code。已开源](summaries/摘要：微信官方接入龙虾，我顺手给接上了 Claude Code。已开源.md)

- [摘要：来看看微信Clawbot催生出了多少离谱的项目吧](summaries/摘要：来看看微信Clawbot催生出了多少离谱的项目吧.md)

- [原文链接](https://mp.weixin.qq.com/s?__biz=MzIzNDE0Njk0Nw%3D%3D&mid=2247492713&idx=1&sn=697d58329dc78edaa065853085f14870&chksm=e9b942103b8b34109e2b7033053b11da342a126ea251fb119534dab8fadc86f8969f2a181ca7#rd)｜[摘要：科研智能自动化平台PaperClaw；大模型会话知识库llmwiki](summaries/摘要：科研智能自动化平台PaperClaw；大模型会话知识库llmwiki.md)｜源文章：科研智能自动化平台PaperClaw；大模型会话知识库llmwiki

- [原文链接](https://mp.weixin.qq.com/s?__biz=MzIwMzY3Njc2MA%3D%3D&mid=2247484484&idx=1&sn=b877810761905accec8c61a88f1d20f3&chksm=97732bf3c04982b7874037c0a69fa13851f4885059370a3951a7a9094c6b6aba2a24fd85addc#rd)｜《Hermes Agent 高级玩法：微信扫码即用 + LLM Wiki 知识库，打造你的数据飞轮》｜来源条目：[摘要：Hermes Agent 高级玩法：微信扫码即用 + LLM Wiki 知识库，打造你的数据飞轮](summaries/摘要：Hermes Agent 高级玩法：微信扫码即用 + LLM Wiki 知识库，打造你的数据飞轮.md)
