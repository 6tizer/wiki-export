---
title: Context Bleed
type: concept
tags:
- 多Agent协作
- 上下文管理
- Agent 安全
status: 审核中
confidence: medium
last_compiled: '2026-04-15'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/4b691bf99fdf4e5f9983415bca109c2c
notion_id: 4b691bf9-9fdf-4e5f-9983-415bca109c2c
---

## 定义

Context Bleed 指多 Agent、跨会话或长链路执行过程中，原本应被隔离的上下文、记忆或规则彼此串扰，最终造成角色混乱、记忆污染和错误决策。

## 关键要点

- 它常见于多 Agent 协作、共享记忆与会话隔离不足的系统中。

- 表面症状往往是答非所问、规则冲突、工具输出串线。

- 解决思路通常包括角色分离、环境隔离和外部记忆租户隔离。

## 来源引用

- [原文链接](https://x.com/BTCqzy1/status/2043210007358148893)｜《Hermes Agent 从入门到精通：25 个致命坑避坑实战指南》

## 关联概念

- [Hermes Agent](entities/Hermes Agent.md)

- [持久化跨会话记忆](concepts/持久化跨会话记忆.md)
