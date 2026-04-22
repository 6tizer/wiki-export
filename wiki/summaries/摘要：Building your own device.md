---
title: 摘要：Building your own device?
type: summary
tags:
- Coding Agent
- Agent 技能
status: 已审核
confidence: high
last_compiled: '2026-04-20'
source_tags: ''
source_article_url: https://www.notion.so/348701074b68818a955bebc1d6b7c130
notion_url: https://www.notion.so/1f91229e1bc041389900c92c5ac35c86
notion_id: 1f91229e-1bc0-4138-9900-c92c5ac35c86
---

## 一句话摘要

Anthropic 为 Claude Code / Claude Cowork 桌面端开放了面向 Maker 的蓝牙接口，让外部硬件可以实时接收会话、审批与状态事件，把编程 Agent 的内部运行状态映射到物理设备上。

## 关键洞察

- 官方仓库 `claude-desktop-buddy` 不只是玩具示例，而是给出了 BLE 通信协议、JSON schema 与 folder push transport 的参考实现。

- 示例硬件基于 ESP32 与 M5Stack 生态，说明这条路线偏向低门槛原型验证，适合快速做出可交互的桌面设备。

- 设备可以显示 recent messages、权限审批与会话活跃度，并允许直接在硬件端 approve / deny，体现出更强的 HITL 交互形态。

- 该能力只在开发者模式下开放，定位更接近开发者实验接口，而非默认面向大众的正式功能。

- 这提示 Tizer 的 OpenClaw / HITL 工作流后续也可以把等待审批、任务繁忙、异常提醒等状态外化到桌面终端或环境设备。

## 提取的概念

- [Claude Desktop Buddy](entities/Claude Desktop Buddy.md)

- [Nordic UART Service](concepts/Nordic UART Service.md)

- [M5Stack](entities/M5Stack.md)

- [ESP32](entities/ESP32.md)

- [Claude Code Desktop](entities/Claude Code Desktop.md)

- [Claude Code](entities/Claude Code.md)

## 原始文章信息

- **作者**：@fm100

- **来源**：X书签

- **发布时间**：2026-04-17

- **原文链接**：[https://x.com/fm100/status/2045127919882977441](https://x.com/fm100/status/2045127919882977441)

- **源页面**：Claude Desktop 开放蓝牙 API：让 ESP32 小玩具成为你的 AI 物理助手

## 个人评注

这类“Agent → BLE → 外设”的链路，本质上是在把原本只存在于 CLI / GUI 里的状态机，扩展成可被环境感知的事件总线。对于需要 HITL 审批和长期运行监控的系统，这种设计很适合延伸到桌面机器人、告警终端或轻量硬件面板。
