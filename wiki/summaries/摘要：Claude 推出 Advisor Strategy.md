---
title: 摘要：Claude 推出 Advisor Strategy
type: summary
tags:
- Agent 编排
- LLM
status: 已审核
confidence: high
last_compiled: '2026-04-15'
source_tags: ''
source_article_url: https://www.notion.so/343701074b6881349b0ec68cd75b01ed
notion_url: https://www.notion.so/4f1002a196304fc0a193b6473c68bb8a
notion_id: 4f1002a1-9630-4fc0-a193-b6473c68bb8a
---

## 一句话摘要

Claude 把 Advisor Strategy 带到 Claude Platform，让 Sonnet 或 Haiku 作为执行器、Opus 作为按需顾问，以更低成本获得接近 Opus 级别的 Agent 表现。

## 关键洞察

- 核心模式是“便宜模型持续执行，强模型只在难点介入”，把顾问-执行者协作做成平台原生能力。

- 这种做法的重点不是单次回答更强，而是让 Agent 在长任务里把高成本推理集中到关键决策点。

- 回复线程里的实战讨论表明，这一模式已经在 Claude Code、Hermes Agent、harness 类工程实践中出现，只是现在被 Anthropic 正式产品化。

- 相关社区项目开始围绕可视化评测、对比实验和工作流范式做延伸，例如 Advisor Tool Playground 与 Ratchet-Driven Development。

## 提取的概念

- [Advisor Strategy](concepts/Advisor Strategy.md)

- [Advisor Tool](concepts/Advisor Tool.md)

- [Harness Engineering](concepts/Harness Engineering.md)

- [Hermes Agent](entities/Hermes Agent.md)

- [Ratchet-Driven Development](concepts/Ratchet-Driven Development.md)

## 原始文章信息

- 作者：@claudeai

- 来源：X书签

- 发布时间：2026-04-09

- 原文链接：[https://x.com/claudeai/status/2042308622181339453](https://x.com/claudeai/status/2042308622181339453)

## 个人评注

对 Tizer 的工作流来说，这种模式很适合放进 HITL 与内容编译流水线：抓取、清洗、结构化填表可以交给低成本执行模型，而概念抽取、去重判断、最终审稿等高价值节点再调用更强模型，以控制成本并提升稳定性。
