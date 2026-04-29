---
title: Human-Agent 协作平台
type: concept
tags:
- Agent 协作模式
- AI 产品
status: 草稿
confidence: medium
last_compiled: '2026-04-28'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/d90bdb99a72c40a6a22a278176f350dd
notion_id: d90bdb99-a72c-40a6-a22a-278176f350dd
---

## 定义

Human-Agent 协作平台是一类新兴产品形态，将 AI Agent 和人类用户放入同一协作环境（通常类似 IM/Slack 界面），让 Agent 不再是被调用的工具，而是以「队友」身份参与日常沟通、任务分工和信息共享。

## 关键要点

- 核心理念：Agent 不是工具，而是团队成员（"not as tools, but as equals"）

- 交互界面借鉴即时通讯（频道、DM、线程），降低人机协作的认知负担

- 支持多 Agent 同时在线，各自承担不同角色（工程师、设计师、PM 等）

- Agent 通常运行在用户本地机器上（通过 daemon 进程），平台负责消息路由和状态同步

- 与传统 chatbot 的区别：强调持续性（Agent 有记忆和上下文积累）、多方协作（多人+多Agent）、异步通信

- 代表产品：Slock

## 关联概念

- [Slock](entities/Slock.md)

- [Multi-Agent 群聊](concepts/Multi-Agent 群聊.md)

- [Agent 动力学](concepts/Agent 动力学.md)

## 来源引用

- [摘要：Hi, I'm RC. I previously built Kimi CLI at Moonshot AI.](summaries/摘要：Hi, I'm RC. I previously built Kimi CLI at Moonshot AI.md)（[原文](https://x.com/istdrc/status/2040862482622026076)）

- [摘要：Connecting Agents to Decisions](summaries/摘要：Connecting Agents to Decisions.md)（[原文](https://x.com/PalantirTech/status/2049136883528011954)）
