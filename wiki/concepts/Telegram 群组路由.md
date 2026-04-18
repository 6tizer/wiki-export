---
title: Telegram 群组路由
type: concept
tags:
- OpenClaw
- Agent 编排
status: 审核中
confidence: medium
last_compiled: '2026-04-11'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/dc81a894a89148008103b29a4acf4f21
notion_id: dc81a894-a891-4800-8103-b29a4acf4f21
---

## 定义

Telegram 群组路由是指在单个 Gateway 或 Bot 之上，依据群组 ID、Topic 或提及规则把消息分发给不同 Agent 的编排方式。

## 关键要点

- 让多个角色 Agent 共享同一个消息入口，但保持工作区和记忆隔离

- 适合产品经理、工程师、QA 等多角色协作场景

- 本质上是一种轻量的消息分发与上下文隔离机制

## 来源引用

- 《OpenClaw 多角色 Telegram 群聊：一个 Gateway 跑产品经理、工程师、QA 的实战指南》（[Berryxia.ai](http://berryxia.ai/)，2026-04-01）— 系统说明了单 Bot 多群组和多 Bot 多 Agent 的路由方式

## 关联概念

- [OpenClaw](entities/OpenClaw.md)

- [子 Agent 派生](concepts/子 Agent 派生.md)
