---
title: Agent 封装粒度
type: concept
tags: []
status: 审核中
confidence: high
last_compiled: '2026-04-20'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/4442a56852724860935544f9f094a188
notion_id: 4442a568-5272-4860-9355-44f9f094a188
---

## 定义

为 Agent 能力选择合适的封装层级：用长期指令表达全局约束，用 Skill 表达可复用工具，用 Custom Agent 表达独立角色与权限边界。

## 关键要点

- 不同封装粒度对应不同的调用成本、覆盖范围和隔离强度。

- 长期指令适合低摩擦的行为约束，Skill 适合重复任务模板，Custom Agent 适合独立交付角色。

- 选择错误的封装粒度，会导致过度工程化或复用不足。

- 这类判断本质上是 Agent 系统设计中的架构决策。

## 来源引用

- [摘要：Notion AI × Sub Agent：把检索隔离写进长期指令的实战](summaries/摘要：Notion AI × Sub Agent：把检索隔离写进长期指令的实战.md)（[原始对话](https://www.notion.so/)）
