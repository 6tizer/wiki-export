---
title: Webhook 幂等性
type: concept
tags:
- 开发工具
status: 审核中
confidence: high
last_compiled: '2026-04-18'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/6946847b681d41eea7186314d54e3ebb
notion_id: 6946847b-681d-41ee-a718-6314d54e3ebb
---

## 定义

Webhook 幂等性是指在 Webhook 重复触发时，确保同一事件只被处理一次的能力。由于外部服务在未收到 200 响应时会自动重试，同一事件可能触发 2-3 次。

## 关键要点

- **问题根源**：GitHub 等服务在 Webhook 未收到 200 响应时自动重试，导致同一事件重复处理

- **简易去重方案**：让 Agent 维护已处理事件 ID 文件（如 `processed-events.md`），每次处理前先检查

- **维护要点**：定期清理记录文件，只保留最近 7 天，防止文件无限增长

- **适用场景**：GitHub PR Review Bot、Webhook 驱动的自动化工作流

## 来源引用

- [摘要：OpenClaw 进阶手册 Vol.3：跑稳之后，才是真的开始](summaries/摘要：OpenClaw 进阶手册 Vol.3：跑稳之后，才是真的开始.md)（[请致天下.AI](http://xn--ghqv4yd56a5mi.ai/), 2026-02-28）— Tip 09 讲述 Webhook 去重方案
