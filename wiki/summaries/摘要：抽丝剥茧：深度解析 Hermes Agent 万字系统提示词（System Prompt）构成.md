---
title: 摘要：抽丝剥茧：深度解析 Hermes Agent 万字系统提示词（System Prompt）构成
type: summary
tags: []
status: 已审核
confidence: high
last_compiled: '2026-04-16'
source_tags: ''
source_article_url: https://www.notion.so/344701074b68816eb7fde1d0b5573b3a
notion_url: https://www.notion.so/Tizer/5de5dc6195724959be4e6636dbb83643
notion_id: 5de5dc61-9572-4959-be4e-6636dbb83643
---

## 一句话摘要

这篇文章用 ModelBox 导出了 Hermes Agent 的完整 system prompt，拆解出身份文件、记忆快照、技能索引、项目级规范文件与平台上下文等九层结构，并指出 [AGENTS.md](http://agents.md/) 是提示词膨胀和 token 成本的主要来源。

## 关键洞察

- Hermes 的 system prompt 不是单一提示词，而是由 [SOUL.md](http://soul.md/)、记忆使用指南、MEMORY 快照、USER PROFILE、Skills 索引、[AGENTS.md](http://agents.md/)、会话元数据、平台提示和会话上下文等多层内容拼接而成。

- 其中 [AGENTS.md](http://agents.md/) 体量最大，接近占到整体 system prompt 的一半，是提示词优化最值得优先处理的部分。

- Hermes 的 Skills 索引虽然支持按需加载完整技能内容，但仅索引本身也会带来不小的上下文开销，反映出 Skill 生态扩张后的 token 管理问题。

- MEMORY 与 USER PROFILE 采用冻结快照的方式注入系统提示，提升了长期个性化与稳定性，但也可能把不该保留的敏感或冗余信息带进上下文。

- 文章给出的实操优化思路是调整 agent 的工作目录与项目级配置文件加载范围，从而显著压缩每轮会话的固定提示词成本。

## 提取的概念

- [Hermes Agent](entities/Hermes Agent.md)

- [ModelBox](entities/ModelBox.md)

- [SOUL.md](concepts/SOUL.md.md)

- [MEMORY.md](concepts/MEMORY.md.md)

- [AGENTS.md](concepts/AGENTS.md.md)

- [Agent Skills](concepts/Agent Skills.md)

## 原始文章信息

- 作者：@LufzzLiz

- 来源：X书签

- 发布时间：2026-04-15

- 原文链接：[https://x.com/LufzzLiz/status/2044258384556556743](https://x.com/LufzzLiz/status/2044258384556556743)

## 个人评注

这篇拆解很适合 Tizer 当前的 Agent 与 Wiki 工作流。一方面，它提醒我们在做 OpenClaw、Hermes 或内容管线设计时，不能只关注能力堆叠，还要关注 system prompt 的固定成本与可维护性。另一方面，它也说明了为什么需要把 SOUL、MEMORY、Skills、项目规范等内容分层管理，并通过 Wiki 持续沉淀这些“提示词基础设施”概念。
