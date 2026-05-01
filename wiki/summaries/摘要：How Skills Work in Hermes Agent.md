---
title: 摘要：How Skills Work in Hermes Agent
type: summary
tags:
- 上下文管理
- 长期记忆
- Harness 工程
status: 已审核
confidence: high
last_compiled: '2026-04-16'
source_tags: ''
source_article_url: https://www.notion.so/344701074b6881b18752c94f1d0d87ef
notion_url: https://www.notion.so/Tizer/01039c1432c64201ba986e5eeaa6ed10
notion_id: 01039c14-32c6-4201-ba98-6e5eeaa6ed10
---

## 一句话摘要

这篇文章解释了 Hermes 如何把 Skills 作为“程序性记忆”来按需加载，让 Agent 在不膨胀上下文的前提下复用成熟工作流。

## 关键洞察

- Hermes 把 **事实**、**会话历史** 和 **方法** 明确拆开，其中 Skills 承担的是“怎么做”的那一层。

- Skills 不是普通提示词片段，而是可以封装流程、命令、陷阱和验证步骤的可复用知识文档。

- Hermes 采用分层读取机制，先看技能索引，再读完整 [SKILL.md](http://skill.md/)，必要时才继续读模板、脚本和参考文件。

- 这种按需加载方式兼顾了能力扩展与上下文成本控制，让 Agent 默认保持轻量，需要时再变得专业。

- 当 Agent 能把一次次成功流程沉淀为 Skill 时，系统获得的是可复用的程序性改进，而不是单纯堆积更多上下文。

## 提取的概念

- [Hermes Agent](entities/Hermes Agent.md)

- [Agent Skills](concepts/Agent Skills.md)

- [Agent-Managed Skills](concepts/Agent-Managed Skills.md)

- [程序性记忆](concepts/程序性记忆.md)

- [渐进式披露](concepts/渐进式披露.md)

- [SKILL.md](concepts/SKILL.md.md)

## 原始文章信息

- 作者：@NeoAIForecast

- 来源：X书签

- 发布时间：2026-04-15

- 原文链接：[https://x.com/NeoAIForecast/status/2044252861710905685](https://x.com/NeoAIForecast/status/2044252861710905685)

## 个人评注

这篇文章对 Tizer 当前的内容编译和 Agent 工作流很有参考价值。它把“知识沉淀”进一步拆成了**事实记忆**与**方法记忆**两类，适合用于思考 OpenClaw、HITL 和内容流水线里哪些经验应该写进 Wiki，哪些则应该沉淀成可复用 Skill。对于长期运行的 Agent，这种结构也能显著降低上下文负担。
