---
title: Agent-curated memory
type: concept
tags:
- 记忆系统
status: 审核中
confidence: medium
last_compiled: '2026-04-15'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/ed9bdd7147f54f2ab36a0eebf67d4f71
notion_id: ed9bdd71-47f5-4f2a-b36a-0eebf67d4f71
---

## 定义

Agent-curated memory 是 Hermes 的长期记忆治理机制，强调由 Agent 在阶段性反思中筛选高价值信息，再写入记忆文件，而不是把每轮对话全量保存下来。

## 关键要点

- 它关注的是高密度、低噪声的长期记忆，而不是完整聊天记录

- 更适合沉淀用户偏好、环境事实、纠错经验和任务里程碑

- 通常会配合 `nudge_interval` 在若干轮对话后触发整理，而不是每轮实时写入

- 设计目标之一是减少记忆污染，并让后续决策更稳定

## 来源引用

- [原文链接](https://x.com/BTCqzy1/status/2044259795499450414)｜《Hermes Agent 从中级到高级进阶指南》｜源文章页面：Hermes Agent 进阶指南：记忆系统、技能自进化与多 Agent 协作全解析

## 关联概念

- [Hermes Agent](entities/Hermes Agent.md)

- [持久化跨会话记忆](concepts/持久化跨会话记忆.md)
