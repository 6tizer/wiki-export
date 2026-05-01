---
title: 摘要：Why memory isn't a plugin (it's the harness)
type: summary
tags: []
status: 已审核
confidence: high
last_compiled: '2026-04-14'
source_tags: ''
source_article_url: https://www.notion.so/342701074b6881838523edddb7a69874
notion_url: https://www.notion.so/Tizer/aeb3b1394a9840f2b80443c4fa55c573
notion_id: aeb3b139-4a98-40f2-b804-43c4fa55c573
---

## 一句话摘要

这篇文章的核心观点是：**Agent 的记忆不是外挂插件，而是 harness 对上下文、状态与持久层进行统一治理后自然涌现出来的系统能力**。

## 关键洞察

- 文章把“把记忆接入 Agent”类比为“把驾驶接入汽车”，强调记忆本质上属于执行底座的核心职责。

- 仅靠 RAG 检索不足以构成真正的记忆，因为检索只是长期状态管理中的一小部分。

- 真正决定 Agent 是否具备记忆能力的，是 harness 如何加载系统文件、暴露技能元数据、处理压缩、保存交互和呈现外部状态。

- Letta Code 进一步展示了 memory-first harness 的实现路径，即把记忆投影到 Git 支撑的文件系统，并让后台子 Agent 持续整理和重写上下文。

- Context Constitution 则把这套实践上升为原则层，强调身份、连续性、记忆与上下文治理之间的内在绑定关系。

## 提取的概念

- [Agent Harness](concepts/Agent Harness.md)

- [Agentic Context Management](concepts/Agentic Context Management.md)

- [Context Compaction](concepts/Context Compaction.md)

- [Git 作为 Agent 记忆](concepts/Git 作为 Agent 记忆.md)

- [Letta Code](entities/Letta Code.md)

- [Context Constitution](concepts/Context Constitution.md)

## 原始文章信息

- 作者：@sarahwooders

- 来源：X书签

- 发布时间：2026-04-03

- 原文链接：[https://x.com/sarahwooders/status/2040121230473457921](https://x.com/sarahwooders/status/2040121230473457921)

## 个人评注

这篇文章对 Tizer 当前的内容管线和 Agent 设计很有参考价值。它提醒我们，**不要把记忆理解成一个可插拔的小功能**，而应把提示重写、上下文压缩、长期状态持久化、技能暴露方式和后台整理机制一起视为 harness 设计的一部分。对 OpenClaw、HITL 和知识编译工作流来说，这意味着后续如果要提升长期任务连续性，重点不应只是接一个“记忆插件”，而是重构上下文治理和状态管理的底座。
