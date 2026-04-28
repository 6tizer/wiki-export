---
title: Context Mode
type: concept
tags:
- Coding Agent
- Agent 编排
status: 审核中
confidence: medium
last_compiled: '2026-04-21'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/403f71ffa3e6482099a1348a059d9904
notion_id: 403f71ff-a3e6-4820-99a1-348a059d9904
---

## 定义

Context Mode 是一种把原始工具输出隔离到上下文沙箱中、再以结构化结果提供给 AI 的工作模式，用来降低噪音输入并提升长任务中的上下文可控性。

## 关键要点

- 它强调“原始输出”和“提供给模型的摘要结果”分层存在，而不是把所有内容直接塞进模型上下文。

- 与 rtk 的命令输出压缩相比，Context Mode 更偏向上下文隔离与结构化交付。

- 它适合需要兼顾可追溯性、成本控制与信息完整性的 AI 编程流程。

- 在本文中，Context Mode 被作为 rtk 之外的相邻思路，用来对比不同的上下文治理路径。

## 来源引用

- [摘要：rtk：给 AI 编码工具装上「信息压缩阀」，Token 消耗最高降 90%](summaries/摘要：rtk：给 AI 编码工具装上「信息压缩阀」，Token 消耗最高降 90%.md)（[原文](https://x.com/laogui/status/2045677115341934867)）

- [摘要：The fastest and most efficient code intelligence engine for AI coding agents.](summaries/摘要：The fastest and most efficient code intelligence engine for AI coding agents.md)（[原文](https://x.com/DataChaz/status/2045784379155226971)）

## 关联概念

- [RTK](entities/RTK.md)

- [上下文压缩](concepts/上下文压缩.md)

- [Context DAG](concepts/Context DAG.md)
