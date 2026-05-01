---
title: Orb
type: entity
tags:
- CLI 工具
- AI 产品
- 长期记忆
- 上下文管理
- 身份准入
- Agent 协作模式
status: 审核中
confidence: high
last_compiled: '2026-04-16'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/518d99f001ff4375a8abefadd63ac6b1
notion_id: 518d99f0-01ff-4375-a8ab-efadd63ac6b1
---

## 定义

Orb 是一个围绕 Claude Code CLI 构建的自进化 AI Agent 框架，重点补齐持久化记忆、身份一致性、多用户服务与消息平台接入。

## 关键要点

- 不重写 Agent runtime，而是直接封装 Claude Code CLI，跟随上游能力升级

- 采用本地 SQLite + 轻量守护进程设计，部署门槛低

- 通过事实提取、纠错沉淀与记忆同步，让 Agent 随交互持续改进

- 支持 Slack 等消息入口与多 profile 隔离，适合长期运行助手

## 来源引用

- [原文链接](https://x.com/karry_viber/status/2044671868272308570)｜《Why Claude Code?》｜源文章：Orb：给 Claude Code 装上持久记忆和灵魂的开源框架

## 关联概念

- [Claude Code](entities/Claude Code.md)

- [持久化跨会话记忆](concepts/持久化跨会话记忆.md)
