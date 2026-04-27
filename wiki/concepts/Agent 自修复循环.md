---
title: Agent 自修复循环
type: concept
tags:
- Harness 工程
- 浏览器自动化
status: 草稿
confidence: high
last_compiled: '2026-04-27'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/b0b99d9685b14b51b2ca7383d3a57cb9
notion_id: b0b99d96-85b1-4b51-b2ca-7383d3a57cb9
---

## 定义

Agent 自修复循环（Self-Heal Loop）是一种 Agent 执行模式：当 Agent 在运行过程中遇到缺失的工具函数或运行时错误时，能自主诊断问题、编写或修改代码、然后重新执行，无需人工介入。

## 关键要点

- 核心机制：Agent 遇到错误 → 读取错误信息 → 定位原因 → 修改/新增代码 → 重试

- 在 Browser Harness 场景中，Agent 发现 [helpers.py](http://helpers.py/) 缺少某个函数时，会自行 grep 代码、添加函数、继续执行

- 不需要预设的 watchdog 或容错处理器，模型本身就是容错层

- 前提条件：Agent 必须有读写自身执行环境代码的权限（如 Claude Code 的 Read/Edit/Write 能力）

- 真实案例：Agent 自行编写了 upload_file() 函数，还在遇到 CDP websocket 10MB 限制后自主切换到分块上传模式

## 来源引用

- [摘要：The Bitter Lesson of Agent Harnesses](summaries/摘要：The Bitter Lesson of Agent Harnesses.md)（[原文](https://x.com/gregpr07/status/2047358189327520166)）

- [摘要：SOMEONE OPEN-SOURCED VIDEO EDITING FOR AI AGENTS.](summaries/摘要：SOMEONE OPEN-SOURCED VIDEO EDITING FOR AI AGENTS.md)（[原文](https://x.com/socialwithaayan/status/2047568884304367722)）

## 关联概念

- [Browser Harness](entities/Browser Harness.md)

- [Agent 自我调试](concepts/Agent 自我调试.md)

- [Agent Harness](concepts/Agent Harness.md)

- [Chrome DevTools Protocol](concepts/Chrome DevTools Protocol.md)
