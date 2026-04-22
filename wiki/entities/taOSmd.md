---
title: taOSmd
type: entity
tags:
- 记忆系统
status: 草稿
confidence: high
last_compiled: '2026-04-16'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/3ce1de5852c44c64be992307ad7f7e26
notion_id: 3ce1de58-52c4-4c64-be99-2307ad7f7e26
---

## 定义

taOSmd 是 TinyAgentOS 的长期记忆系统，通过时间知识图谱、混合检索和零损归档等机制，为 Agent 提供可持续更新的记忆能力。

## 核心要点

- 结合 temporal knowledge graph、语义+关键词检索与 append-only archive

- 支持事实抽取、矛盾检测、意图感知检索与多层上下文组装

- README 中给出了 LongMemEval-S 上的高召回结果，强调其在低成本硬件上的可用性

- 可通过 HTTP API 被不同 Agent 框架读写，定位为框架无关的记忆后端

## 来源引用

- [原文链接](https://x.com/Teknium/status/2044329280201732217)｜《⚠️ Pre-beta — GUI not yet wired to core functions.》｜源文章：TinyAgentOS：用树莓派和旧电脑搭建自己的分布式 AI Agent 操作系统

## 关联概念

- [TinyAgentOS](entities/TinyAgentOS.md)

- [Hermes Agent](entities/Hermes Agent.md)

- [Browser Connect](concepts/Browser Connect.md)

- [Tailscale](entities/Tailscale.md)
