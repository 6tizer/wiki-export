---
title: Agent 输出表面适配
type: concept
tags:
- Agent 协作模式
- 内容自动化
status: 草稿
confidence: medium
last_compiled: '2026-04-27'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/b79e5f9ce08c45a89570e7b5a5d3cdb4
notion_id: b79e5f9c-e08c-45a8-9570-e7b5a5d3cdb4
---

## 定义

Agent 输出表面适配（Agent Output Surface Adaptation）指 AI Agent 在不同输出表面（Slack、Notion、Email、终端等）渲染内容时，同一文本可能呈现截然不同的效果，因此 Agent 和内容创建者需要针对多个表面进行适配设计。

典型案例：Markdown 在 Slack 中渲染效果差（格式丢失、换行异常），但在 Notion 中渲染优秀。当一个 Agent 同时输出到多个表面时，相同的文本需要「存活」于 4 个以上的渲染环境。

## 关键要点

- 同一段 Agent 输出在 Slack、Notion、Email、Web 等表面渲染效果差异巨大

- 设计 Agent 输出时需要考虑「最差表面」的兼容性

- 内容格式选择（Markdown、HTML、纯文本）直接影响多表面适配效果

- 这一问题推动了「为 Agent 设计」而非「为单一界面设计」的思维转变

## 来源引用

- [摘要：I've read this piece three times.](summaries/摘要：I've read this piece three times.md)（[原文](https://x.com/sytaylor/status/2047660039809241543)）

## 关联概念

- [Canonical Design](concepts/Canonical Design.md)

- [3uild](entities/3uild.md)
