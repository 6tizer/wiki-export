---
title: memify
type: concept
tags:
- 记忆系统
status: 草稿
confidence: medium
last_compiled: '2026-04-16'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/2c8dd593b5d34c3c9d83dc5585b30396
notion_id: 2c8dd593-b5d3-4c3c-9d83-dc5585b30396
---

## 定义

memify 是 Cognee 中基于真实检索流量对记忆图进行强化与衰减的优化步骤，用来让图谱根据使用情况持续重排召回优先级。

## 关键要点

- 跟踪检索过程实际使用过的路径、节点与边

- 强化带来有效回答的连接，逐步衰减长期未使用的部分

- 从重复出现的使用模式中推断新的关联关系

- 属于 RL 启发式的记忆优化过程，让记忆系统更贴近真实任务流量

## 来源引用

- [文章链接](https://x.com/akshay_pachaar/status/2044699731277078785)｜《All Platforms, One Memory》｜来源条目：Agent 记忆的另一面：学会遗忘，才能真正记住

## 关联概念

- [Cognee](entities/Cognee.md)

- [智能遗忘](concepts/智能遗忘.md)
