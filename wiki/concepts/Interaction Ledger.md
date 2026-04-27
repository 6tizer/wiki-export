---
title: Interaction Ledger
type: concept
tags:
- 长期记忆
- 多Agent协作
status: 草稿
confidence: medium
last_compiled: '2026-04-27'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/73fd4da635a0442d999670f05032f037
notion_id: 73fd4da6-35a0-442d-9996-70f05032f037
---

## 定义

**Interaction Ledger**（交互账本）是多 Agent 系统中用于跨会话状态共享的持久化记录机制。它记录 Agent 与外部世界（Slack、iMessage、Discord、语音等）的所有交互事件，作为 Agent 间共享状态的**编排原语**（orchestration primitive），替代传统的会话共享方式。

## 关键要点

- Interaction Ledger 充当多 Agent 系统的**共享记忆层**：Agent 之间不共享会话上下文，而是通过读写同一份交互账本来协调状态

- 在生产级 Agent 系统中，Interaction Ledger 可能积累数万条记录（如 65,000+ 条跨平台交互记录）

- 记忆维护是 Agent 系统的**核心成本项**——约 40% 的 Token 消耗用于记忆管理，这是保持长期准确性的代价

- Interaction Ledger 的设计思路将记忆从「附加功能」提升为「一等公民」（first-class concern），而非事后补救

## 关联概念

- [GBrain](entities/GBrain.md)

- [Minions](concepts/Minions.md)

## 来源引用

- [摘要：Big drop for GBrain v0.19.](summaries/摘要：Big drop for GBrain v0.19.md)（[原文](https://x.com/garrytan/status/2047504667127799974)）
