---
title: Phantom Transfer
type: concept
tags:
- AI 对齐
- 训练/微调
- Agent 安全
status: 审核中
confidence: medium
last_compiled: '2026-04-16'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/7ad5b8e63fec4f35a9c606ab43327a37
notion_id: 7ad5b8e6-3fec-4f35-a9c6-06ab43327a37
---

### 定义

Phantom Transfer 指一种数据投毒或隐式迁移现象，即某些特征可以借由训练数据在不同模型家族之间迁移，即使这些特征并未以直白方式写入数据。

### 关键要点

- 线程中将其作为与 Subliminal Learning 相关的后续研究方向。

- 它强调风险不只存在于单一模型或同初始化模型内部，也可能跨模型家族传播。

- 这类现象会把问题从输出安全扩展到训练数据来源与蒸馏链路治理。

### 来源引用

- [Our paper on Subliminal Learning was just published in Nature!](https://x.com/OwainEvans_UK/status/2044488099707949545)｜源页面：潜意识学习：LLM 能通过语义无关数据悄悄传递「对齐信号」
