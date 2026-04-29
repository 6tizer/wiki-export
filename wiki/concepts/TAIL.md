---
title: TAIL
type: concept
tags:
- 多模态
status: 草稿
confidence: high
last_compiled: '2026-04-28'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/6771388dc3cc48848739e30ce688962d
notion_id: 6771388d-c3cc-4884-8739-e30ce688962d
---

## 定义

TAIL（Time-Aligned Interleaving）是 MiniCPM-o 4.5 中提出的流式语音生成方案，旨在解决全双工场景下语音输出延迟过高的问题。TAIL 让每个语音块的生成紧跟其对应的文本块，避免文本「抢跑」过多导致语音滞后，同时通过轻量级的「预读」（pre-look）机制保证跨词发音的连贯性。

全称：Time-Aligned Interleaving

## 关键要点

- 解决流式语音生成中「文本先跑、语音滞后」的延迟问题

- 每个语音块紧随对应文本块生成，最小化语音输出与交互发生的延迟

- 轻量级 pre-look 机制解决跨词发音连贯性

- 在保证音频流畅悦耳的同时将延迟降到最低

- 是实现全双工场景下即时打断的关键技术之一

## 来源引用

- [摘要：MiniCPM-o 4.5技术报告发布：全双工全模态API开放，RTX5070即可实时运行](summaries/摘要：MiniCPM-o 4.5技术报告发布：全双工全模态API开放，RTX5070即可实时运行.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzIwMTc4ODE0Mw%3D%3D&mid=2247719918&idx=1&sn=cbff45b94902b42d7fd45f6fb079edc9&chksm=97101f37ad8063e784cbc767f4e95f0508b405d9e1139ea77dab6c3182100c13acef9d1b40d5#rd)，PaperWeekly，微信，2026-04-28）

- [摘要：首发Omni-Flow流式全模态架构，消费级显卡就能跑](summaries/摘要：首发Omni-Flow流式全模态架构，消费级显卡就能跑.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzkzNjgwNzMwNQ%3D%3D&mid=2247488507&idx=1&sn=8a7a55596274e541a89d16c7f7b8f75a&chksm=c312c36bc0423679e9095a15081351a18b482a6059fbfc5e9516372def651857eb573c215ca7#rd)，CourseAI，微信，2026-04-28）
