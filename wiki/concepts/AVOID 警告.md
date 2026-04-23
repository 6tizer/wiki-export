---
title: AVOID 警告
type: concept
tags:
- Agent 编排
- Coding Agent
status: 草稿
confidence: high
last_compiled: '2026-04-23'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/46c47732dfcd4c429ed2d1520c57dbd8
notion_id: 46c47732-dfcd-4c42-9ed2-d1520c57dbd8
---

## 定义

AVOID 警告是 Gene 中用于沉淀失败经验的压缩表达形式，把过去的错误模式提炼成可直接注入模型的禁止项或避坑约束。

## 关键要点

- 它不是完整错误日志，而是从失败中蒸馏出的最小可执行警示。

- 文中认为，失败经验若原样堆成 log、reflection 或 Skill，往往会稀释有效控制；压缩成 AVOID 反而更有用。

- AVOID 的价值在于把“不要做什么”明确前置，减少模型在关键步骤上重复踩坑。

- 这种写法也说明，Agent 记忆的最佳形态未必是长轨迹，而可能是短小但高约束的警告信号。

## 来源引用

- [摘要：你写的Skill，正在拖慢模型？策略式Gene才是正确答案](summaries/摘要：你写的Skill，正在拖慢模型？策略式Gene才是正确答案.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzA3MzI4MjgzMw%3D%3D&mid=2651029194&idx=1&sn=74444aa55fa4caff4666f024133d1896&chksm=8556a7658823460534cdb2c17157b616b7b4dc1061276c088fe77b3338d30db85b2e60109ba7#rd)）

## 关联概念

- [GEP 协议](concepts/GEP 协议.md)

- [Evolver](entities/Evolver.md)
