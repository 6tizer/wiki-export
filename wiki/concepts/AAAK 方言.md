---
title: AAAK 方言
type: concept
tags: []
status: 审核中
confidence: high
last_compiled: '2026-04-13'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/4e3e3b4abc12438284bc2cb897394aff
notion_id: 4e3e3b4a-bc12-4382-84bc-2cb897394aff
---

## 定义

AAAK 方言是 MemPalace 体系里用于压缩表达记忆内容的结构化表示方式，核心问题不在于“压得多短”，而在于是否拥有可验证的形式文法、编码器、解码器与往返一致性。

## 关键要点

- 原项目的重要缺口是缺少形式化文法，导致 AAAK 文本更像启发式压缩结果，而非严格可验证的语言。

- Rust 重写版本把 AAAK 视为一个需要独立规范实现的子系统，而不是临时提示词技巧。

- 当记忆系统要服务多个 Agent 时，AAAK 这类中间表示能否被稳定解析，决定了其可维护性。

## 来源引用

- [原文链接](https://x.com/blackanger/status/2043063705324392585)｜源文章：mempal：用 Rust 重铸 AI 记忆宫殿，Coding Agent 的项目记忆工具

- [原文链接](https://mp.weixin.qq.com/s/1rY6qMBqSELEm83MbhDzLA)｜源文章：96.6%召回率，0美元成本：这款开源AI记忆系统凭什么超越一切付费方案

## 关联概念

- [MemPalace](entities/MemPalace.md)

- [LongMemEval](concepts/LongMemEval.md)

- [MCP 协议](concepts/MCP 协议.md)
