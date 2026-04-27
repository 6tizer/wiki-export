---
title: hermes-a2a
type: entity
tags:
- 多Agent协作
- Agent 协作模式
status: 草稿
confidence: medium
last_compiled: '2026-04-28'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/f3d1c08cc3e34acba1e6ccb076fce29d
notion_id: f3d1c08c-c3e3-4acb-a1e6-ccb076fce29d
---

## 定义

hermes-a2a 是一个开源插件，为 Hermes Agent 框架添加基于 Google A2A 协议的跨框架 Agent 间对等通信能力。与传统的 delegate_task（主从式任务委托）不同，hermes-a2a 让两个拥有独立记忆和判断力的 Agent 在对等关系中直接交流。

**别名**：Hermes A2A Plugin

**GitHub**：[https://github.com/iamagenius00/hermes-a2a](https://github.com/iamagenius00/hermes-a2a)

## 关键要点

- **纯 Plugin 架构**：完全适配 Hermes Agent v0.11.0，不修改 Hermes 源码

- **Session 内消息注入**：A2A 消息直接进入对方正在运行的 session，回复的是同一个 session 的 Agent 本体

- **对话持久化**：自动将对话保存到磁盘，不会被 context compaction 压掉，Agent 重启后仍在

- **Webhook 即时唤醒**：消息到达通过 webhook 立刻触发 agent turn，无需轮询

- **隐私隔离**：私有记忆/日记不会泄露到 A2A 消息中

## 实际应用案例

- 通过 A2A 联系远程同事的 Agent 获取 bug 修复上下文

- Claude Code 与 Hermes Agent 相互 review 代码，基于不同 context 给出多角度见解

- Agent 产出报告直接通过 A2A 发送给同事的 Agent，携带完整上下文

## 来源引用

- [摘要：Hermes-a2a](summaries/摘要：Hermes-a2a.md)（[原文](https://x.com/0xViviennn/status/2047626457191780527)）

## 关联概念

- [Agent 对等通信](concepts/Agent 对等通信.md)

- [A2A 协议](concepts/A2A 协议.md)

- [Hermes Agent](entities/Hermes Agent.md)

- [Context Compaction](concepts/Context Compaction.md)
