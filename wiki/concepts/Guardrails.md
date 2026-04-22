---
title: Guardrails
type: concept
tags:
- Coding Agent
- Agent 编排
status: 草稿
confidence: high
last_compiled: '2026-04-20'
source_tags: Agent, 自动化, Hooks, harness, LLM
source_article_url: ''
notion_url: https://www.notion.so/aa4c2036f7eb4e1095be7b1b5b9c492c
notion_id: aa4c2036-f7eb-4e10-95be-7b1b5b9c492c
---

## 定义

Guardrails 是嵌入在 Agent 工作流中的约束与校验机制，用来把团队对质量、安全、风格和边界的要求转化为可执行的硬约束，而不是只停留在提示词建议层。

## 关键要点

- 它的本质是把“什么叫好结果”形式化为检查点、规则和验证流程。

- 高质量 guardrails 往往由文档规范、review 规则、lints、tests 和审批节点共同组成。

- 真正有效的 guardrails 必须接入执行过程，在关键动作发生前后触发，而非完全依赖模型自觉。

- 在 Coding Agent 场景中，guardrails 是把人类 taste 转化为稳定工程输出的核心桥梁。

## 来源引用

- [摘要：什么才是真正的 Harness Engineering？](summaries/摘要：什么才是真正的 Harness Engineering？.md)（[原文](https://x.com/SaitoWu/status/2045458721929892345)）

## 关联概念

- [Harness Engineering](concepts/Harness Engineering.md)

- [PreToolUse](concepts/PreToolUse.md)

- [Agent Skills](concepts/Agent Skills.md)

- [渐进式披露](concepts/渐进式披露.md)
