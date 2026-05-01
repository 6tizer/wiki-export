---
title: Supabase
type: entity
tags:
- 链上协议
- Agent 安全
- 商业/生态
status: 审核中
confidence: high
last_compiled: '2026-04-23'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/9ad1fec4e16c4dbaba096a81dfefde4f
notion_id: 9ad1fec4-e16c-4dba-ba09-6a81dfefde4f
---

## 定义

Supabase 是一个开源后端平台，提供 Postgres 数据库、认证、存储、边缘函数和实时能力，常被用作现代全栈应用的后端基础设施。

## 关键要点

- 它的产品形态接近“开源版 Firebase + Postgres”，强调快速搭建数据库、认证和 Serverless 能力。

- 在 Agent 场景下，Supabase 也通过 MCP Server 暴露部分操作接口，但其信息组织方式仍然更多面向人类开发者。

- 当文档检索、状态发现和错误诊断缺乏结构化上下文时，Agent 可能需要多轮探索与重试，带来显著 Token 开销。

## 关联概念

- [Claude Code](entities/Claude Code.md)

- [InsForge](entities/InsForge.md)

- [Context Engineering](concepts/Context Engineering.md)

## 来源引用

- [摘要：How to cut Claude Code costs by 3x (using Karpathy's context engineering principles)](summaries/摘要：How to cut Claude Code costs by 3x (using Karpathy's context engineering principles).md)（[原文](https://x.com/_avichawla/status/2046500537584218438)）
