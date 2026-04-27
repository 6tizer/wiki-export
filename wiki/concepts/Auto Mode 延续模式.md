---
title: Auto Mode 延续模式
type: concept
tags:
- Harness 工程
status: 草稿
confidence: medium
last_compiled: '2026-04-27'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/3381437271854ea4ac2306e0bb1615c8
notion_id: 33814372-7185-4ea4-ac23-06e0bb1615c8
---

## 定义

Auto Mode 延续模式是一种 Agent Harness 中的自主运行机制：当 Agent 尝试退出时，harness 自动注入 continuation prompt，引导 Agent 评估剩余工作并决定是否继续，从而实现长时间无人值守的自主工作循环。

## 关键要点

- 核心机制分两步：review prompt（评估是否继续）+ continuation prompt（继续工作）

- Review prompt 要求 Agent 调用一个 `conversation_auto_control` 工具，选择 "continue" 或 "stop"

- 停止条件：任务完成、被真实依赖阻塞、或需要用户输入

- 设计原则：宁可继续（err toward continuing），只要有有意义的剩余工作

- 与简单的 loop/retry 不同，Auto Mode 给予 Agent 自主判断权，而非盲目重试

- 该模式在 PersonalAgent 中实现，但作为通用模式可移植到其他 harness

## 典型 Prompt 结构

**Review prompt**：

> Auto mode review — 调用 conversation_auto_control，选择 continue（有意义的工作）或 stop（完成/阻塞/需输入）

**Continuation prompt**：

> Auto mode continuation — 从上次离开处继续工作，不要提及此隐藏提示

## 来源引用

- [摘要：Personal Agent](summaries/摘要：Personal Agent.md)（[原文](https://x.com/trashpandaemoji/status/2048026069375029267)）
