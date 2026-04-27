---
title: 摘要：Hermes-a2a
type: summary
tags:
- 多Agent协作
- Agent 协作模式
status: 已审核
confidence: medium
last_compiled: '2026-04-27'
source_tags: ''
source_article_url: https://www.notion.so/34f701074b6881a5b7c4f2fe776f6456
notion_url: https://www.notion.so/Tizer/f99e547a5ed7488db30de382d28bcbea
notion_id: f99e547a-5ed7-488d-b30d-e382d28bcbea
---

## 一句话摘要

hermes-a2a 是为 Hermes Agent 框架开发的开源插件，基于 Google A2A 协议实现 Agent 间对等通信，让两个拥有独立记忆和判断力的 Agent 以平等身份在活跃 session 中直接交流。

## 关键洞察

- **对等而非主从**：区别于传统的 delegate_task（spawn 子 agent 干完活就消失），hermes-a2a 实现的是两个独立 Agent 之间的平等对话，各自保持完整上下文和记忆

- **纯 Plugin 架构**：已完全适配 Hermes Agent v0.11.0，从 patch 源码升级为纯 Plugin 形式，不碰 Hermes 源码

- **Session 内消息注入 + 持久化**：A2A 消息直接注入对方正在运行的 session，对话自动持久化到磁盘，不会被 Context Compaction 压掉

- **Webhook 即时唤醒**：消息到达通过 webhook 立刻触发 agent turn，无需轮询，配合隐私隔离保证私有记忆不外泄

- **真实落地案例**：已用于跨地域 Agent 协作获取 bug 上下文、Claude Code 与 Hermes 互相 code review、报告自动流转等场景

## 提取的概念

- [hermes-a2a](entities/hermes-a2a.md)

- [Agent 对等通信](concepts/Agent 对等通信.md)

- [A2A 协议](concepts/A2A 协议.md)

- [Hermes Agent](entities/Hermes Agent.md)

- [Context Compaction](concepts/Context Compaction.md)

## 原始文章信息

- **作者**：@0xViviennn

- **来源**：X书签

- **发布时间**：2026-04-24

- **链接**：[原文](https://x.com/0xViviennn/status/2047626457191780527)

- **GitHub**：[hermes-a2a](https://github.com/iamagenius00/hermes-a2a)

## 个人评注

hermes-a2a 把 Agent 间通信从主从模式推进到对等模式，这对 OpenClaw 生态和 Tizer 的多 Agent 工作流有直接启发：当不同 Agent 各自拥有独立 context 和记忆时，对等交流比单向委托能产生更丰富的协作价值。Session 注入 + 持久化的设计也解决了 context compaction 丢消息的已知痛点，值得在内容自动化流水线中借鉴。
