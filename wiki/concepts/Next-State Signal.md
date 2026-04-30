---
title: Next-State Signal
type: concept
tags:
- Agent 协作模式
- 训练/微调
- OpenClaw
status: 审核中
confidence: medium
last_compiled: '2026-05-01'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/89ca347d0c724e7689aa30ae2c4e340b
notion_id: 89ca347d-0c72-4e76-89aa-30ae2c4e340b
---

## 定义

Next-State Signal 是一种把 Agent 动作之后环境反馈视为天然训练信号的在线学习思想，用下一状态来反推当前动作的好坏。

## 关键要点

- 无需完全依赖人工显式打标签

- 适合在线强化学习和持续纠偏场景

- 常与自动奖励建模和轨迹收集一起使用

## 来源引用

- [摘要：OpenClaw-RL：让你的本地 Agent 边聊边进化](summaries/摘要：OpenClaw-RL：让你的本地 Agent 边聊边进化.md)（X书签）
