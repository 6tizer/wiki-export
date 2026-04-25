---
title: web fetch
type: concept
tags:
- Agent 技能
- LLM
status: 草稿
confidence: high
last_compiled: '2026-04-25'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/d8b1448e6f3f4de899e2ed461e684ee7
notion_id: d8b1448e-6f3f-4de8-99e2-ed461e684ee7
---

## 定义

web fetch 是 Agent 直接抓取网页正文并将结果注入当前上下文的能力，看似简单，但在真实使用中常常是 token 成本最高的操作之一。

## 关键要点

- 代价往往高于普通代码生成与短文本推理

- 大页面和 PDF 会显著抬高上下文成本

- 需要配合截断、抽取和缓存策略控制成本

## 来源引用

- 摘要：OpenClaw 烧 Token 的真相：最贵的不是写代码，而是 web fetch（X书签）
