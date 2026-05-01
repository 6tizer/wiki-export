---
title: Hermes Messaging Gateway
type: concept
tags: []
status: 审核中
confidence: medium
last_compiled: '2026-04-20'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/e41d68a88bb2499ca6ca388dbec9b80b
notion_id: e41d68a8-8bb2-499c-a6ca-388dbec9b80b
---

## 定义

Hermes Messaging Gateway 是 Hermes Agent 的统一消息入口层，用同一套 Agent 会话与配置连接 Telegram、Discord、Slack、WhatsApp、Signal、Email 等多个外部沟通渠道。

## 关键要点

- 让同一个 Hermes Agent 可以在多个消息平台持续工作，而不是被单一终端绑定。

- 将消息接入、身份路由与平台状态管理抽象成统一网关，降低多平台部署复杂度。

- 与 CLI/TUI 形成互补：本地适合深度操作，消息网关适合远程触发与持续协作。

- 对内容分发、告警推送、异步任务回传这类工作流尤其关键。

## 来源引用

- [摘要：Hermes Agent Creative Hackathon 正式启动](summaries/摘要：Hermes Agent Creative Hackathon 正式启动.md)（[原文](https://x.com/NousResearch/status/2045225469088326039)）

- [摘要：Ollama 一键启动 Hermes Agent：免费、本地、会自我进化的 AI 私人助手](summaries/摘要：Ollama 一键启动 Hermes Agent：免费、本地、会自我进化的 AI 私人助手.md)（[原文](https://x.com/Saboo_Shubham_/status/2045692123887050816)）

## 关联概念

- [Hermes Agent](entities/Hermes Agent.md)

- [OpenClaw](entities/OpenClaw.md)

- [自我进化 Skills 系统](concepts/自我进化 Skills 系统.md)

- [OpenClaw 迁移](concepts/OpenClaw 迁移.md)
