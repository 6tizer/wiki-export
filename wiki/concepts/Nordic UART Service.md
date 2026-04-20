---
title: Nordic UART Service
type: concept
tags:
- Agent 技能
- 开发工具
status: 草稿
confidence: high
last_compiled: '2026-04-20'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/a75c91ef2fc24a508c662d5ef813ecdf
notion_id: a75c91ef-2fc2-4a50-8c66-2d5ef813ecdf
---

## 定义

Nordic UART Service（NUS）是一种常见的 BLE 串口抽象协议，用于把蓝牙连接模拟成类似串口的数据收发通道，方便设备与上位机交换文本或结构化消息。

## 关键要点

- 它降低了蓝牙设备开发门槛，让很多控制与状态同步场景可以沿用“收发消息”的思路实现。

- 在 Claude 外设场景里，NUS 适合作为设备与桌面端之间传递事件、审批指令与状态更新的基础通道。

- 对 Maker 项目来说，NUS 比自定义复杂协议更容易快速原型化与调试。

## 来源引用

- [摘要：Building your own device?](summaries/摘要：Building your own device.md)（[原文](https://x.com/fm100/status/2045127919882977441)）

## 关联概念

- [Claude Desktop Buddy](entities/Claude Desktop Buddy.md)

- [Claude Code Desktop](entities/Claude Code Desktop.md)

- [ESP32](entities/ESP32.md)
