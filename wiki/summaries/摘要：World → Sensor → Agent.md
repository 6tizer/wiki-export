---
title: 摘要：World → Sensor → Agent
type: summary
tags:
- Agent 协作模式
- Harness 工程
status: 已审核
confidence: high
last_compiled: '2026-04-30'
source_tags: ''
source_article_url: https://www.notion.so/351701074b6881e491d1c5c423614c91
notion_url: https://www.notion.so/Tizer/418baa086e9849c2adfc23bcbedbb184
notion_id: 418baa08-6e98-49c2-adfc-23bcbedbb184
---

## 一句话摘要

World2Agent（W2A）提出开源的 Agent 感知协议，通过「World → Sensor → Agent」架构让 AI Agent 主动感知真实世界，而非被动等待指令。

## 关键洞察

- **感知是自主性的前提**：“Agents that wait to be told what’s happening aren’t autonomous, they’re just fast typists”——没有实时感知能力的 Agent 本质上仍是被动响应器

- **统一信号规范**：W2A 定义标准化的 Signal 格式，Sensor 可自由互换，Agent 不绑定特定数据源，类似 MCP 对工具层的标准化

- **多运行时原生支持**：提供 Claude Code、Hermes、OpenClaw 三大 Agent 运行时的插件，安装即用

- **SensorHub 生态**：类似 npm marketplace 的 Sensor 目录，社区可贡献自定义 Sensor，约 50 行代码即可构建

- **协议而非产品的定位**：创始团队明确强调 W2A 是开放协议和邀请，而非封闭产品，鼓励社区共建感知层

## 提取的概念

- [World2Agent](entities/World2Agent.md)

- [Agent 感知协议](concepts/Agent 感知协议.md)

- [Proactive Agents](concepts/Proactive Agents.md)

## 原始文章信息

- **作者**：@hasantoxr（转发），原推 @LeahW_2077

- **来源**：X 书签

- **发布日期**：2026-04-29

- **原文链接**：[X 推文](https://x.com/hasantoxr/status/2049472203620815334)

- **GitHub**：[machinepulse-ai/world2agent](https://github.com/machinepulse-ai/world2agent)（417★，TypeScript，Apache-2.0）

## 个人评注

W2A 的「World → Sensor → Agent」架构与 OpenClaw 的 Hooks 机制有相似之处，都是让 Agent 能对外部事件做出反应。不同之处在于 W2A 更专注于「感知」层的标准化，而 MCP 协议覆盖的是「行动」层。对于 Tizer 的内容管线而言，W2A Sensor 可以作为自动化监听新内容源的方案之一，值得关注其 SensorHub 生态发展。
