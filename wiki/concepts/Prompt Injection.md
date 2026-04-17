---
title: Prompt Injection
type: concept
tags:
- 安全/隐私
status: 草稿
confidence: medium
last_compiled: '2026-04-15'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/148c73731bbc44059cd0e838ebde9d1b
notion_id: 148c7373-1bbc-4405-9cd0-e838ebde9d1b
---

## 定义

Prompt Injection 是指外部内容通过伪装成指令、规则或高优先级信息，诱导 Agent 偏离原始系统约束、执行错误操作或泄露信息的攻击方式。

## 关键要点

- 它的核心不是模型能力不足，而是指令优先级被错误理解。

- 在网页浏览、外部文档读取和自动执行链路中尤为常见。

- 防御重点是把外部内容视为不可信输入，并显式声明其不能覆盖系统规则。

## 来源引用

- [原文链接](https://x.com/BTCqzy1/status/2043210007358148893)｜《Hermes Agent 从入门到精通：25 个致命坑避坑实战指南》

## 关联概念

- [Hermes Agent](entities/Hermes Agent.md)

- [Context Bleed](concepts/Context Bleed.md)

- [Gateway](concepts/Gateway.md)
