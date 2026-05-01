---
title: 摘要：A good AGENTS.md is a model upgrade. A bad one is worse than no docs at
  all.
type: summary
tags:
- 知识管理
status: 已审核
confidence: high
last_compiled: '2026-04-23'
source_tags: ''
source_article_url: https://www.notion.so/34b701074b688111a111df616a7befdf
notion_url: https://www.notion.so/Tizer/0755270d2733417b87dd14319b51b765
notion_id: 0755270d-2733-417b-87dd-14319b51b765
---

## 一句话摘要

这篇文章基于代码生成评测指出，优秀的 [AGENTS.md](http://agents.md/) 能显著提升 Coding Agent 的完成质量，而糟糕或过载的说明文档会把 Agent 拖入过度探索，效果甚至不如没有文档。

## 关键洞察

- [AGENTS.md](http://agents.md/) 的价值高度依赖写法：短小、可路由、可按需加载的文档结构，比面面俱到的大而全说明更有效。

- 把任务写成编号清晰的程序化工作流，能明显降低 Agent 漏步骤、漏接线、漏文件的问题。

- 当代码库里存在多种可行做法时，决策表能帮助 Agent 在写代码前先选对路径，从而提升规范一致性。

- 真实代码片段、可执行规则和“不要这样做 + 应该这样做”的成对指引，比单纯堆叠禁令更有用。

- 文档失败的核心模式是 Context Rot：Agent 被架构概览、警告清单和周边文档拖入过度探索，消耗上下文却降低完成度。

## 提取的概念

- [AGENTS.md](concepts/AGENTS.md.md)

- [渐进式披露](concepts/渐进式披露.md)

- [程序化工作流](concepts/程序化工作流.md)

- [决策表](concepts/决策表.md)

- [Context Rot](concepts/Context Rot.md)

## 原始文章信息

- 作者：@augmentcode

- 来源：X书签

- 发布时间：2026-04-23

- 原文链接：[https://x.com/augmentcode/status/2047164534310494709](https://x.com/augmentcode/status/2047164534310494709)

## 个人评注

这篇材料对 Tizer 当前的 Agent 文档体系很有参考价值：与其把所有规范一次性塞进主指令，不如把高频原则放在主文档，把分支规则拆进可路由的参考文件。对 OpenClaw、内容工厂和 Notion Agent 流程来说，这意味着要优先设计“主干流程 + 决策表 + 按需展开”的结构，避免因为说明过多而让 Agent 在执行前消耗掉大部分上下文。 
