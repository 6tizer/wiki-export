---
title: ClawBot
type: entity
tags:
- OpenClaw
status: 审核中
confidence: high
last_compiled: '2026-04-17'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/06d50915d1234f49bb86ee99b049fc60
notion_id: 06d50915-d123-4f49-bb86-ee99b049fc60
---

**定义**：ClawBot 是微信官方推出的 AI Agent 接入插件，内置在微信 App 里，通过 iLink 平台为 AI Agent 提供安全的官方消息通道。

**iLink 协议核心机制**

- **认证**：插件调用 `ilink/bot/get_bot_qrcode` 拿二维码，用户扫码后返回 `bot_token`

- **收消息**：通过 `ilink/bot/getupdates` 長轮询，每条消息带 `context_token`

- **发消息**：调用 `ilink/bot/sendmessage` 带上 `bot_token` 和 `context_token`

**设计实质**

- 这套接口和接的是什么 AI 没有关系，它只是一个消息通道

- 微信不关心你用谁的模型，只关心交互是否发生在微信里

- 标志着微信首次开放"通道里跑什么我不管"的官方接口

**安装方式**

```bash
npx -y @tencent-weixin/openclaw-weixin-cli@latest install
```

执行并扫码即可完成配对。

**来源引用**

- [摘要：微信官方接入龙虾，我顺手给接上了 Claude Code。已开源](summaries/摘要：微信官方接入龙虾，我顺手给接上了 Claude Code。已开源.md)

- [摘要：聊聊微信的Agent野心](summaries/摘要：聊聊微信的Agent野心.md)

- [摘要：微信不止能接 OpenClaw，我把 Claude Code、Codex、Opencode 等 AI IDE 也接进来了](summaries/摘要：微信不止能接 OpenClaw，我把 Claude Code、Codex、Opencode 等 AI IDE 也接进来了.md)
