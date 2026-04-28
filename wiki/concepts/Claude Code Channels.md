---
title: Claude Code Channels
type: concept
tags:
- Coding Agent
status: 审核中
confidence: medium
last_compiled: '2026-04-17'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/65205516e8fc4881ad8d205342224ec8
notion_id: 65205516-e8fc-4881-ad8d-205342224ec8
---

**定义**：Claude Code Channels 是 Anthropic 推出的基于 MCP 协议的插件系统，允许外部聊天工具（Telegram、Discord、微信等）与 Claude Code 会话双向推送消息。

**官方支持的平台**

- Telegram、Discord（官方内置插件）

- 微信 ClawBot（通过社区桌接实现）

**Telegram 安装流程**

1. BotFather 创建机器人 Token

1. `/plugin install telegram@claude-plugins-official`

1. `/telegram:configure <token>`

1. 启动命令 + 发配对码

1. `/telegram:access policy allowlist`

**Discord 安装流程**

1. 创建 Bot 获取 Token，开启 Message Content Intent

1. `/plugin install discord@claude-plugins-official`

1. `/discord:configure <token>` + 启动命令 + 配对

**开放架构**

插件架构开放，可以写自定义 Channel 插件接入任意平台。

**来源引用**

- [摘要：Claude Code 官方远程连接 Telegram 和 Discord 的操作流程。](summaries/摘要：Claude Code 官方远程连接 Telegram 和 Discord 的操作流程。.md)

- [摘要：微信官方接入龙虾，我顺手给接上了 Claude Code。已开源](summaries/摘要：微信官方接入龙虾，我顺手给接上了 Claude Code。已开源.md)

- [原文链接](https://x.com/claudeai/status/2044131493966909862)｜《Learn more in the official documentation》｜来源条目：[摘要：Learn more in the official documentation](summaries/摘要：Learn more in the official documentation.md)

## 关联概念

- [Claude Code](entities/Claude Code.md)

- [MCP 协议](concepts/MCP 协议.md)

- [Claude Code Hooks](concepts/Claude Code Hooks.md)
