---
title: 摘要：code-review-graph：Claude Code 本地知识图谱，减少 6.8 倍代码审查 Token !
type: summary
tags:
- Coding Agent
- 开发工具
status: 已审核
confidence: high
last_compiled: '2026-04-17'
source_tags: ''
source_article_url: https://www.notion.so/345701074b68812f9ae9ecba44d080de
notion_url: https://www.notion.so/7a124525606f4d7d810f4a68c7eef583
notion_id: 7a124525-606f-4d7d-810f-4a68c7eef583
---

## 一句话摘要

code-review-graph 通过把本地代码库构造成可增量更新的知识图谱，并经由 MCP 提供给 Claude Code 等 Coding Agent 使用，让 AI 在代码审查和开发任务中只读取真正相关的上下文，从而显著降低 Token 消耗。

## 关键洞察

- **上下文裁剪是核心价值**：它不是让 Agent 读得更多，而是让 Agent 只读和当前任务真正相关的文件、函数、依赖与测试。

- **底层依赖结构化解析**：借助 [Tree-sitter](entities/Tree-sitter.md) 把代码转成 AST 和图谱节点，为后续查询、检索与影响分析提供基础。

- **增量维护决定可用性**：通过 [增量更新](concepts/增量更新.md) 和哈希校验，图谱可以在文件保存或 git 提交后快速刷新，而不必全量重建。

- **影响分析优先保证不漏**：爆炸半径分析 以 100% 召回率为目标，宁可多给上下文，也尽量不漏掉真正受影响的代码范围。

- **适合大型仓库与 Agent 工作流**：在大型单体仓库里，这类 [代码知识图谱](concepts/代码知识图谱.md) 能显著减少噪音上下文，是 Coding Agent 基础设施层的一种补强。

## 提取的概念

- [code-review-graph](entities/code-review-graph.md)

- [Tree-sitter](entities/Tree-sitter.md)

- 爆炸半径分析

- [增量更新](concepts/增量更新.md)

- [代码知识图谱](concepts/代码知识图谱.md)

- [Claude Code](entities/Claude Code.md)

- [MCP 协议](concepts/MCP 协议.md)

## 原始文章信息

- 作者：AI开源提效指南

- 来源：微信

- 发布时间：2026-04-09

- 原文链接：[https://mp.weixin.qq.com/s?__biz=MzY5NzIxODM2MQ==&mid=2247484353&idx=1&sn=f2ad30ea21fee327daac93a9143a76fb&chksm=f539ae6800aa8066504c6b4ed683e14b501d516a93882ddd92b4c501a2537281c3b85d7d3c8f#rd](https://mp.weixin.qq.com/s?__biz=MzY5NzIxODM2MQ%3D%3D&mid=2247484353&idx=1&sn=f2ad30ea21fee327daac93a9143a76fb&chksm=f539ae6800aa8066504c6b4ed683e14b501d516a93882ddd92b4c501a2537281c3b85d7d3c8f#rd)

- 源页面：code-review-graph：Claude Code 本地知识图谱，减少 6.8 倍代码审查 Token !

## 个人评注

这篇文章对 Tizer 当前的工作流有两个直接启发：一是可把 code-review-graph 看成 Coding Agent 的“仓库记忆层”，用于减少 Claude Code / OpenClaw 一类 Agent 在代码任务里的重复读库成本；二是“图谱 + 增量更新 + 影响分析”的组合，很适合接入 HITL 的代码审查与内容生产流水线，在保证上下文精度的同时压缩调用成本。
