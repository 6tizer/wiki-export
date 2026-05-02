---
title: Kimi CLI
type: entity
tags:
- CLI 工具
- Harness 工程
- 代码生成
status: 审核中
confidence: high
last_compiled: '2026-04-28'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/45eb345abab647ab9c0257fc55e87465
notion_id: 45eb345a-bab6-47ab-9c02-57fc55e87465
---

## 定义

Kimi CLI 是 RC 在 Kimi 时主导实践的本地 Coding Agent 形态：它长在命令行里，但核心价值并不只是 CLI 外壳，而是底层可复用的 local agent harness。

## 关键要点

- 面向程序员场景，是一个运行在命令行中的本地 Coding Agent

- 为 Agent 设计 CLI 时，需要把输入和输出都做成更清晰、结构化、低歧义的形式

- 底层 harness 可以继续向 Web UI、VS Code 扩展等图形界面复用

- 可以从最小的 agent loop 和 bash tool 起步，再逐步补足内建工具与系统提示

- CLI 只是第一步，不是 Agent 的终局交互形态

## 关联概念

- [Harness Engineering](concepts/Harness Engineering.md)

- [Slock](entities/Slock.md)

## 来源引用

- [摘要：用 Agent 动力学，和 40 个 Agents 一起为「人 + AI」做产品｜42章经](summaries/摘要：用 Agent 动力学，和 40 个 Agents 一起为「人 + AI」做产品｜42章经.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzIyMDE5OTYyMw%3D%3D&mid=2651051564&idx=1&sn=babc1b1e75b77826a63d304d33c348e0&chksm=8dd911d417729de737132383124e9f75bf193b1c2ce831b08c3e001f0552438ebac7eae45e1d#rd)）

- [摘要：Hi, I'm RC. I previously built Kimi CLI at Moonshot AI.](summaries/摘要：Hi, I'm RC. I previously built Kimi CLI at Moonshot AI.md)（[原文](https://x.com/istdrc/status/2040862482622026076)）
