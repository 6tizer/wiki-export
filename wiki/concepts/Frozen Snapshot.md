---
title: Frozen Snapshot
type: concept
tags:
- 记忆系统
status: 草稿
confidence: medium
last_compiled: '2026-04-15'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/cf3d1ce3f3374179b3a3d816eae85816
notion_id: cf3d1ce3-f337-4179-b3a3-d816eae85816
---

## 定义

Frozen Snapshot 是 Hermes 在会话开始时注入上下文的一种冻结记忆快照机制。它会把 [MEMORY.md](http://memory.md/) 和 [USER.md](http://user.md/) 的当前版本作为稳定前缀载入，而不是在当前会话中实时刷新。

## 关键要点

- 冻结快照能让当前会话的上下文前缀保持稳定

- 这有助于提高缓存命中并降低推理成本

- 会话中途新写入的记忆，通常不会立刻反映到当前轮上下文里

- 这也是很多用户误以为 Agent “没记住”的原因之一

## 来源引用

- [原文链接](https://x.com/BTCqzy1/status/2044259795499450414)｜《Hermes Agent 从中级到高级进阶指南》｜源文章页面：Hermes Agent 进阶指南：记忆系统、技能自进化与多 Agent 协作全解析

## 关联概念

- [Hermes Agent](entities/Hermes Agent.md)

- [持久化跨会话记忆](concepts/持久化跨会话记忆.md)
