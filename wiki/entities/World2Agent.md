---
title: World2Agent
type: entity
tags:
- Agent 协作模式
- CLI 工具
status: 草稿
confidence: high
last_compiled: '2026-04-30'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/44a717a88fa1429d85c3c0af97c05393
notion_id: 44a717a8-8fa1-429d-85c3-c0af97c05393
---

## 定义

World2Agent（W2A）是一个开源协议，标准化 AI Agent 对真实世界的感知方式。核心架构为 **World → Sensor → Agent**：Sensor 监听数据源并按 W2A 协议发出结构化信号，Agent 接收信号后自主决策。

别名：W2A

## 关键要点

- **开放协议**：定义统一的 Signal 格式规范，Sensor 之间可自由互换，Agent 不绑定特定数据源

- **SensorHub**：官方 Sensor 目录（类似 npm marketplace），按感知类别分类（市场、新闻、天气、AI 实验室等）

- **多运行时支持**：原生插件覆盖 Claude Code、Hermes、OpenClaw 三大 Agent 运行时

- **低门槛扩展**：约 50 行代码即可构建自定义 Sensor，发布到 npm 后全社区可用

- **Apache 2.0 开源**：TypeScript 实现，GitHub 417★（截至 2026-04-29）

## 技术架构

```javascript
World → Sensor → Agent
```

- **Sensor**：npm 包形式分发，监听外部数据源，输出符合 W2A Signal 规范的结构化数据

- **Bridge**：每个 Agent 运行时有对应的 sensor-bridge，负责将 Signal 路由到 Agent 会话

- **Graph Layer**（Roadmap）：组合和增强多个 Sensor 信号后再送达 Agent

## 仓库信息

- GitHub：[https://github.com/machinepulse-ai/world2agent](https://github.com/machinepulse-ai/world2agent)

- 语言：TypeScript

- 许可证：Apache-2.0

- 组织：MachinePulse AI

## 关联概念

- [Agent 感知协议](concepts/Agent 感知协议.md)

- [Proactive Agents](concepts/Proactive Agents.md)

## 来源引用

- [摘要：World → Sensor → Agent](summaries/摘要：World → Sensor → Agent.md)（[原文](https://x.com/hasantoxr/status/2049472203620815334)）
