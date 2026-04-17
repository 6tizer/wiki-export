---
title: Prompt Caching
type: concept
tags:
- Coding Agent
- LLM
status: 审核中
confidence: high
last_compiled: '2026-04-11'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/f929311550e4404c85b3714806d540cb
notion_id: f9293115-50e4-404c-85b3-714806d540cb
---

## 定义

Prompt Caching 是通过复用对话前缀缓存来降低重复上下文成本、提升 Agent 交互效率的运行机制。

## 关键要点

- 对长上下文编程 Agent 的成本结构影响很大

- 前缀顺序稳定与静态内容固定是高命中率关键

- 会影响模型切换、工具顺序和系统提示设计

## 来源引用

- 《深度使用半年，我总结了 Claude Code 的架构、治理与工程实践》｜X书签文章｜原文链接：[https://x.com/HiTw93/status/2032091246588518683](https://x.com/HiTw93/status/2032091246588518683)

- [原文链接](https://x.com/jxnlco/status/2044469127696556153)｜《Sandboxes are coming to the Agents SDK》｜源文章：OpenAI Agents SDK 沙盒：让 AI Agent 真正「留下工作成果」

## 关联概念

- [In Distribution](concepts/In Distribution.md)

- [Agent Harness](concepts/Agent Harness.md)

- [Sandbox Agents](concepts/Sandbox Agents.md)
