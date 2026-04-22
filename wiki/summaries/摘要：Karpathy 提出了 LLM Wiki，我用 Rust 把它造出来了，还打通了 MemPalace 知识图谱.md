---
title: 摘要：Karpathy 提出了 LLM Wiki，我用 Rust 把它造出来了，还打通了 MemPalace 知识图谱
type: summary
tags:
- 知识管理
- 记忆系统
status: 已审核
confidence: high
last_compiled: '2026-04-16'
source_tags: ''
source_article_url: https://www.notion.so/344701074b6881ceabceeb0165ecc3d8
notion_url: https://www.notion.so/5573ea7c07814f81a6ae9c70ae145cd8
notion_id: 5573ea7c-0781-4f81-a6ae-9c70ae145cd8
---

## 一句话摘要

这篇文章把 Karpathy 的 LLM Wiki 从概念设想推进到工程实现，给出了一个基于 Rust、SQLite、Outbox、三路 RRF 检索与 MemPalace bridge 的可审计知识系统原型。

## 关键洞察

- 作者将 **LLM Wiki** 从概念文档落到了可运行工程，核心不只是“把资料写成 Markdown”，而是把知识当作可演化、可追溯的系统来维护。

- 文章提出了 **Claim 断言模型** 与 **记忆分层架构**，让知识具备层级、置信度、质量分、取代关系与过时标记，而不是简单堆叠文本。

- 查询侧不是单一路径检索，而是把 **BM25、向量召回、知识图谱游走** 通过 **RRF 融合检索** 合并，再叠加保留强度权重。

- 工程侧通过 **Outbox 事件流**、审计记录与 Lint 健康检查，让知识库具备可观测、可追责、可增量消费的能力。

- `llm-wiki` 进一步打通了 **MemPalace** 知识图谱桥接，说明这套体系已经从个人 Wiki 走向“记忆系统 + 知识图谱 + Agent 编排”的复合架构。

## 提取的概念

- [Karpathy LLM Wiki 方法论](concepts/Karpathy LLM Wiki 方法论.md)

- [llm-wiki](entities/llm-wiki.md)

- [MemPalace](entities/MemPalace.md)

- [记忆分层架构](concepts/记忆分层架构.md)

- [RRF 融合检索](concepts/RRF 融合检索.md)

- [Claim 断言模型](concepts/Claim 断言模型.md)

- [Outbox 模式](concepts/Outbox 模式.md)

## 原始文章信息

- 作者：老码小张

- 来源：微信

- 发布时间：2026-04-17 00:30

- 原文链接：[https://mp.weixin.qq.com/s?__biz=MzkxNzY0OTA4Mg==&mid=2247493206&idx=1&sn=7080809308368860641fd4df6601bef9&chksm=c0a8ea2ad24191e6e6e084a08eacab4b318f12dd484d75fe35bb554e96c6e9906e407e998911#rd](https://mp.weixin.qq.com/s?__biz=MzkxNzY0OTA4Mg%3D%3D&mid=2247493206&idx=1&sn=7080809308368860641fd4df6601bef9&chksm=c0a8ea2ad24191e6e6e084a08eacab4b318f12dd484d75fe35bb554e96c6e9906e407e998911#rd)

- 源条目：Karpathy 提出了 LLM Wiki，我用 Rust 把它造出来了，还打通了 MemPalace 知识图谱

## 个人评注

这篇文章和 Tizer 当前的 Wiki Compiler 工作流高度契合。它强调“先编译、后查询”的知识管线，也强调事件驱动、审计轨迹、知识图谱联动与长期记忆分层，这些都能直接映射到 OpenClaw、HITL 审核和内容编译流水线的设计思路。
