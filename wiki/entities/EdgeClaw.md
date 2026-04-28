---
title: EdgeClaw
type: entity
tags:
- OpenClaw
- 记忆系统
status: 审核中
confidence: high
last_compiled: '2026-04-28'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/57a0c446447245729c98a2fa2c3ece4b
notion_id: 57a0c446-4472-4572-9c98-a2fa2c3ece4b
---

## 定义

EdgeClaw是将Claude Code长期记忆能力引入OpenClaw的开源扩展，支持多层结构化记忆、成本感知路由和三层隐私保护。

## 核心要点

- **三层记忆架构**：工作记忆（当前任务）+ 情节记忆（历史交互）+ 语义记忆（领域知识）

- **成本感知路由**：根据任务复杂度自动选择模型，显著降低API费用

- **三层隐私保护**：本地加密 + 访问控制 + 敏感信息过滤

- **适用场景**：大型代码库长期维护、敏感数据处理、复杂自动化任务

- **与Claude Code的关系**：将Claude Code的记忆模式移植到OpenClaw生态

## ClawXRouter 智能路由

EdgeClaw 内置 ClawXRouter 端云协同架构：

- **三级隐私路由**：S3 私密局端处理 / S2 敏感脱敏上云 / S1 安全直接上云

- **性价比感知路由**：LLM-as-Judge 小模型评估任务复杂度，自动选模型

- **双轨记忆**：云端只看脱敏版 [MEMORY.md](http://memory.md/)，端侧保留完整版

## 来源引用

- [摘要：EdgeClaw：把 Claude Code 体验带到 OpenClaw](summaries/摘要：EdgeClaw：把 Claude Code 体验带到 OpenClaw.md)（小华同学ai，微信，2026-04-07）

- [摘要：EdgeClaw 2.0：把 Claude Code 的顶级记忆系统注入开源 AI Agent 生态](summaries/摘要：EdgeClaw 2.0：把 Claude Code 的顶级记忆系统注入开源 AI Agent 生态.md)（X书签文章，[原文](https://x.com/berryxia/status/2039376439204774093)）

- [摘要：龙虾成本狂陆58%！ClawXRouter开源智能调度员](summaries/摘要：龙虾成本狂陆58%！ClawXRouter开源智能调度员.md)
