---
title: 摘要：模型只是引擎，System Prompt 才是底盘：用 Claude 优化自身的迁移实验
type: summary
tags:
- Coding Agent
- LLM
status: 已审核
confidence: high
last_compiled: '2026-04-12'
source_tags: Agent, LLM, OpenClaw, 自动化, Claude
source_article_url: https://www.notion.so/33d701074b6881bb8398eda3ef438bdb
notion_url: https://www.notion.so/e8a5f8e037254c16957f9d51250dd630
notion_id: e8a5f8e0-3725-4c16-957f-9d51250dd630
---

**一句话摘要**

这篇文章证明，迁移模型时真正决定上限的往往不是模型名字，而是能否把优秀工作方式沉淀成稳定的系统级提示框架。

## 关键洞察

- Claude 与 GPT 的差距，可以通过显式的 Cognitive Framework 大幅缩小。

- System prompt 的价值在于规定思考顺序、输出结构与问题求解方式，而不是只补充背景信息。

- 子 Agent 的上下文注入和角色定义，是复杂任务稳定执行的关键。

- OAuth 受限后，SDK 与 CLI 仍是 Claude Agent 能力的重要接入路径。

**提取的概念**

- [Cognitive Framework](concepts/Cognitive Framework.md)

- [System Prompt 工程](concepts/System Prompt 工程.md)

- [Claude Agent SDK](entities/Claude Agent SDK.md)

- [MCP 协议](concepts/MCP 协议.md)

**原始文章信息**

- 作者：@outsource_

- 来源：X书签

- 发布时间：2026-04-04

- 链接：[原文](https://x.com/outsource_/status/2040345259335422463)

**个人评注**

对 Tizer 的工作流来说，这类框架最适合沉淀成编译代理的长期规则页，而不是散落在一次次聊天里的临时提示。
