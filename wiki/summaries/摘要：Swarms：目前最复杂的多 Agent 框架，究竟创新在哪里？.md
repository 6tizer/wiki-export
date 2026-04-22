---
title: 摘要：Swarms：目前最复杂的多 Agent 框架，究竟创新在哪里？
type: summary
tags:
- Agent 框架
status: 已审核
confidence: high
last_compiled: '2026-04-11'
source_tags: Agent, LLM
source_article_url: ''
notion_url: https://www.notion.so/3dd8704684ab44788cb4ebc096025ca4
notion_id: 3dd87046-84ab-4478-8cb4-ebc096025ca4
---

**一句话摘要**：Swarms 是由 Kye Gomez 开发的企业级多 Agent 编排框架，核心创新在于内置多种协作架构模式（顺序/并发/专家混合/自动分解），是设计野心最大但开发者生态最薄弱的 Agent 框架。

## 关键洞察

- 核心创新：内置多种 Agent 协作模式（SequentialWorkflow/ConcurrentWorkflow/MixtureOfAgents/AutoSwarm），"架构菜单"设计

- GitHub 5,600+ Stars，Apache-2.0 开源，v8.5.0（2025年10月），主要由创始人一人维护

- 与 Eliza 本质区别：Eliza 专注 Agent 人格化，Swarms 专注 Agent 间协作编排

- 致命弱点：链上生态几乎为零，Web3 场景需大量自行实现，开发者生态远弱于 LangChain/CrewAI

- 复杂度是价值（丰富协作模式）也是负担（上手门槛高、文档覆盖不足）

## 提取的概念

- **Swarms 框架** — kyegomez 企业级多 Agent 编排框架，核心架构模式详解

- **Multi-Agent 群聊** — Agent 间协作编排的不同设计模式

- **ElizaOS** — 对比：Swarms（协作导向）vs Eliza（人格化导向）

## 原始文章信息

- **作者**：@hhhx402（0xhhh，Web3 Agent 开发者）

- **来源**：X书签

- **发布时间**：2024-12-30

- **链接**：[https://x.com/hhhx402/status/1873702809755107669](https://x.com/hhhx402/status/1873702809755107669)

## 个人评注

Swarms 的"架构菜单"设计思路对 OpenClaw 工作流编排有参考价值，尤其是 ConcurrentWorkflow（并发处理）和 MixtureOfAgents（专家路由）模式。建议作为设计参考而非直接依赖。
