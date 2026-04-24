---
title: Metric Library
type: concept
tags:
- LLM
- 开发工具
status: 草稿
confidence: medium
last_compiled: '2026-04-24'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/dbb6994d0fce42b3b980a3a931a9ccce
notion_id: dbb6994d-0fce-42b3-b980-a3a931a9ccce
---

## 定义

Metric Library 是 One-Eval 中将不同评测指标封装为可插拔组件的指标库设计，用于支持灵活替换、扩展和组合评测 metric。

## 关键要点

- 它把指标实现从具体 benchmark 流程里解耦出来。

- 有利于按任务需要替换 metric 或扩展新的评估方法。

- 对内部定制评测与领域扩展尤其重要。

## 关联概念

- [One-Eval](entities/One-Eval.md)

- [Benchmark Gallery](concepts/Benchmark Gallery.md)

## 来源引用

- [摘要：DeepSeek-V4 发布 10 小时，北大开源项目实现了自动化评测！](summaries/摘要：DeepSeek-V4 发布 10 小时，北大开源项目实现了自动化评测！.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzIyNjM2MzQyNg%3D%3D&mid=2247722249&idx=1&sn=7e9f29cb43e6948fe35c0a1435f013d8&chksm=e909fc8f9ecba3b58d11840fbdb88bf7db327e9a06421ac4903412691391c0edb1ef97cc7696#rd)）
