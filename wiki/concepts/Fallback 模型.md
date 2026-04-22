---
title: Fallback 模型
type: concept
tags:
- 工作流
status: 草稿
confidence: high
last_compiled: '2026-04-18'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/39c4cd6c7cdc41c59f90a98f98ad9947
notion_id: 39c4cd6c-7cdc-41c5-9f90-a98f98ad9947
---

## 定义

Fallback 模型是一种容错机制，当 Agent 的主模型 API 不可用时，自动切换到备用模型继续工作，保障服务不中断。

## 关键要点

- **配置方式**：通过 `model.fallbacks` 数组指定备用模型优先级，如 Sonnet → GPT-4o → Gemini Pro

- **注意事项**：不同模型输出格式有差异，切换后可能格式错乱；fallback 模型成本可能比主模型更高

- **适用场景**：生产环境中防止因模型厂商 API 故障导致整个工作流停滞

- **与 OpenClaw 的关系**：OpenClaw 原生支持 `model.primary` + `model.fallbacks` 配置

## 来源引用

- [摘要：OpenClaw 进阶手册 Vol.3：跑稳之后，才是真的开始](summaries/摘要：OpenClaw 进阶手册 Vol.3：跑稳之后，才是真的开始.md)（[请致天下.AI](http://xn--ghqv4yd56a5mi.ai/), 2026-02-28）— Tip 08 详细讲述 Fallback 模型配置
