---
title: Global State 数据总线架构
type: concept
tags:
- Agent 编排
- 工作流
status: 草稿
confidence: medium
last_compiled: '2026-04-24'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/6bb90e4960394699bf6a472a18fed446
notion_id: 6bb90e49-6039-4699-bf6a-472a18fed446
---

## 定义

Global State 数据总线架构是指把评测流程的完整生命周期统一托管到一个动态状态对象中，让各个核心算子围绕同一全局状态读写与协同的执行设计。

## 关键要点

- 它替代了传统无状态线性流水线，使执行过程更可追踪。

- 各模块会在全局状态上留下结构化轨迹，便于回放与排错。

- 这种架构特别适合长流程、可中断、需复盘的评测系统。

## 关联概念

- [One-Eval](entities/One-Eval.md)

- [DataFlow](entities/DataFlow.md)

- [Human-In-The-Loop](concepts/Human-In-The-Loop.md)

## 来源引用

- [摘要：DeepSeek-V4 发布 10 小时，北大开源项目实现了自动化评测！](summaries/摘要：DeepSeek-V4 发布 10 小时，北大开源项目实现了自动化评测！.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzIyNjM2MzQyNg%3D%3D&mid=2247722249&idx=1&sn=7e9f29cb43e6948fe35c0a1435f013d8&chksm=e909fc8f9ecba3b58d11840fbdb88bf7db327e9a06421ac4903412691391c0edb1ef97cc7696#rd)）
