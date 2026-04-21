---
title: Browser Harness
type: entity
tags:
- Agent 编排
- Agent 技能
status: 草稿
confidence: high
last_compiled: '2026-04-21'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/bf92576a01f14d729e478633adc44b57
notion_id: bf92576a-01f1-4d72-9e47-8633adc44b57
---

## 定义

Browser Harness 是 Browser Use 团队开源的极简浏览器 Agent harness，让 LLM 直接通过 Chrome DevTools Protocol 控制真实浏览器，并在任务过程中按需改写 helpers 源码补齐缺失能力。

## 关键要点

- 采用 thin harness 思路，不再给模型额外套一层复杂抽象

- 通过单个 websocket 直连 Chrome，把底层浏览器能力直接暴露给 Agent

- 核心卖点是 self-healing：当缺失某个工具函数时，Agent 可以直接修改 harness 代码继续执行

- 适合与 Claude Code、Codex 等通用 coding agent 配合，把浏览器操作变成可演化的执行层

## 来源引用

- 摘要：self-healing（[原文](https://x.com/Gorden_Sun/status/2046228429662794153)）

## 关联概念

- Harness Engineering

- Chrome DevTools Protocol

- Browser Use
