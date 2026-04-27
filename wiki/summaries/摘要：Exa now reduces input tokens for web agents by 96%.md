---
title: 摘要：Exa now reduces input tokens for web agents by 96%
type: summary
tags:
- RAG/检索
- 上下文管理
status: 已审核
confidence: high
last_compiled: '2026-04-27'
source_tags: Agent, LLM
source_article_url: https://www.notion.so/34f701074b6881b38884cb5bbc644fea
notion_url: https://www.notion.so/Tizer/2fe6f5c7a1f14226a672a6a4eb73e702
notion_id: 2fe6f5c7-a1f1-4226-a672-a6a4eb73e702
---

## 一句话摘要

Exa 推出 Highlights 功能，通过查询感知的文本提取将 Web Agent 的输入 token 减少 96%，500 token 即可匹配万级 token 全文的 RAG 准确率。

## 关键洞察

- Exa 训练了专门的文本提取模型 Highlights，针对给定查询动态筛选网页中最相关的 token 片段

- 在 SimpleQA 基准上，500 字符 highlights 匹配 8000 字符全文准确率，token 用量仅 1/16

- 4k 字符 highlights 表现优于 32k 字符全文，说明信息密度远比信息量重要

- 该技术对 frontier 模型（如 GPT 5.5）的长链路 Agent 任务尤为关键，可有效防止 Context Bloat

- Highlights 每次请求实时计算（非缓存），延迟低于 100ms

## 提取的概念

- [Exa Highlights](concepts/Exa Highlights.md)

- [SimpleQA](concepts/SimpleQA.md)

- [Exa](entities/Exa.md)

- [Context Bloat](concepts/Context Bloat.md)

## 原始文章信息

- **作者**：@ExaAILabs

- **来源**：X书签

- **发布时间**：2026-04-23

- **链接**：[原文推文](https://x.com/ExaAILabs/status/2047402544260116517) ｜ [Exa 博客](https://exa.ai/blog/highlights-for-agents)

## 个人评注

对 Tizer 的 Agent 工作流有直接启示：OpenClaw 和内容管道中的 web 搜索步骤如果接入 Exa Highlights，可以大幅降低每次搜索的 token 消耗和成本，使多轮搜索的 agentic loop 在经济上更可行。这与 HITL 流程中"按需加载最相关上下文"的设计理念高度一致——信息密度优先于信息完整性。
