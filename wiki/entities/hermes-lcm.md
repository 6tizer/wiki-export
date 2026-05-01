---
title: hermes-lcm
type: entity
tags:
- 上下文管理
- 长期记忆
- Agent 协作模式
status: 审核中
confidence: high
last_compiled: '2026-04-23'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/141b8b06c1774e3c99c26e80cb056d47
notion_id: 141b8b06-c177-4e3c-99c2-6e80cb056d47
---

## 定义

hermes-lcm 是 Hermes Agent 的无损上下文管理插件，通过层次化 DAG 和插件内检索工具，把被压缩的历史对话变成可回溯、可展开的长期上下文层。

## 关键要点

- 用独立的不可变存储保存消息，避免传统压缩后细节永久丢失。

- 通过 `lcm_grep`、`lcm_expand` 等工具，为 Agent 提供当前会话内的精细回忆路径。

- 核心价值不只是“存更多”，而是让压缩后的上下文仍具备稳定的检索与钻取能力。

- 相比宿主侧历史恢复路径，它把上下文找回能力前置到插件自身，增强了 Agent 自主性。

## 来源引用

- [摘要：Lossless Context Management plugin for Hermes Agent](summaries/摘要：Lossless Context Management plugin for Hermes Agent.md)（[原文](https://x.com/GitTrend0x/status/2046932331001512385)）

## 关联概念

- [Hermes Agent](entities/Hermes Agent.md)

- [lossless-claw](entities/lossless-claw.md)

- [Supermemory](entities/Supermemory.md)
