---
title: Thin Harness, Fat Skills
type: concept
tags:
- Coding Agent
- Agent 编排
status: 草稿
confidence: high
last_compiled: '2026-04-15'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/16953cb5369a45628e01882f5fb62c25
notion_id: 16953cb5-369a-4562-8e01-882f5fb62c25
---

## 定义

Thin Harness, Fat Skills 是一种 Agent 架构原则：把通用运行时尽量做薄，把领域判断、流程知识和可复用经验沉淀到 Skills 中。

## 关键要点

- Harness 负责循环、上下文、文件读写、安全和工具调度，不承载过多业务逻辑

- Skills 用 markdown 或结构化文档封装流程、判断标准与可复用方法

- 把智能上推到 Skills，把执行下压到确定性工具，可以同时获得灵活性与可靠性

- 新模型发布后，Skills 往往能直接受益，而底层确定性能力无需重写

## 关联概念

- [Agent Harness](concepts/Agent Harness.md)

- [Resolver](concepts/Resolver.md)

- [Agent Skills](concepts/Agent Skills.md)

- [Context Engineering](concepts/Context Engineering.md)

- [Fat Code](concepts/Fat Code.md)

- [Skill 分类学](concepts/Skill 分类学.md)

- [Skill 颗粒度设计](concepts/Skill 颗粒度设计.md)

- [GBrain](entities/GBrain.md)

- [gstack](entities/gstack.md)

## 来源引用

- [摘要：「不就是几个 Markdown 文件」：一场关于 Agentic 工程本质的争论](summaries/摘要：「不就是几个 Markdown 文件」：一场关于 Agentic 工程本质的争论.md)（[原文](https://x.com/garrytan/status/2045371983312097409)）

- [摘要：Resolvers: The Routing Table for Intelligence](summaries/摘要：Resolvers- The Routing Table for Intelligence.md)（[原文](https://x.com/garrytan/status/2044479509874020852)）

- [原文链接](https://x.com/chenchengpro/status/2043697811993350611)｜《Garry Tan 提炼了他在 agentic engineering 领域的核心心法：Fat Skills, Fat Code, Thin Harness。》｜源文章：Garry Tan 的 Agent 工程心法：Fat Skills、Fat Code、Thin Harness

- [原文链接](https://x.com/garrytan/status/2042925773300908103)｜《Thin Harness, Fat Skills》｜源文章：Thin Harness, Fat Skills：Garry Tan 的 AI Agent 生产力架构

- [原文链接](https://mp.weixin.qq.com/s?__biz=MzIyMzA5NjEyMA%3D%3D&mid=2647681530&idx=1&sn=d5c714699089e31276c667cda1edefdb&chksm=f153676ae06e0dadad8df80becf797662c0126d74a5c1a314ecac659ebf41da34625aac44a6b#rd)｜《Skill其实就是分类学。》｜源文章：Skill其实就是分类学。

- [原文链接](https://x.com/AlphaSignalAI/status/2044461541232148986)｜《How GBrain Works, and How to Actually Wire It Into Your Agents》｜来源条目：[摘要：How GBrain Works, and How to Actually Wire It Into Your Agents](summaries/摘要：How GBrain Works, and How to Actually Wire It Into Your Agents.md)
