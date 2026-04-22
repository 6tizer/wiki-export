---
title: 摘要：OpenClaw 的 9 层 System Prompt 架构：框架管稳定，你管个性化
type: summary
tags:
- OpenClaw
- LLM
status: 已审核
confidence: high
last_compiled: '2026-04-11'
source_tags: OpenClaw, Agent, LLM
source_article_url: ''
notion_url: https://www.notion.so/6a1b82968dc14c37b8cb7e21d68e9a8b
notion_id: 6a1b8296-8dc1-4c37-b8cb-7e21d68e9a8b
---

### 一句话摘要

OpenClaw 的九层 system prompt 架构把框架层稳定能力与用户层个性化定制拆分开来，使 Agent 的运行更像可维护系统，而不是一段一次性大提示词。

### 关键洞察

- 底层自动生成身份、工具、技能和运行时状态等信息，用户无需直接干预。

- 真正可定制的高价值入口是工作区文件与启动钩子，而不是反复在聊天里重复同样指令。

- 分层设计的本质，是把系统稳定性、用户定制和当次任务触发分别治理。

### 提取的概念

- [OpenClaw 九层 System Prompt 架构](concepts/OpenClaw 九层 System Prompt 架构.md)

- [IDENTITY.md](concepts/IDENTITY.md.md)

- [OpenClaw](entities/OpenClaw.md)

### 原始文章信息

- 作者：@yanhua1010

- 来源：X书签

- 发布时间：未明确给出

- 链接：[原文](https://x.com/yanhua1010/status/2030192442428023231)

### 个人评注

- 这对 Tizer 的 Agent 体系有直接启发，长期个性化应尽量落在结构化配置里，而不是散落在每次对话中。
