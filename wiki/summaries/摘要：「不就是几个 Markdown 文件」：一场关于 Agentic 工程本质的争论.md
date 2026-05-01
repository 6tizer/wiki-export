---
title: 摘要：「不就是几个 Markdown 文件」：一场关于 Agentic 工程本质的争论
type: summary
tags:
- Harness 工程
- Agent 协作模式
- 上下文管理
status: 已审核
confidence: medium
last_compiled: '2026-04-20'
source_tags: Agent, LLM, Prompt工程, harness, Hooks
source_article_url: https://www.notion.so/348701074b68813ca40ac586b3e02392
notion_url: https://www.notion.so/Tizer/7c0f075757c14c8498629f3d09e42c72
notion_id: 7c0f0757-57c1-4c84-9862-9f3d09e42c72
---

## 一句话摘要

这篇文章借 Garry Tan 关于“Markdown 文件并不等于 Agentic 软件”的争论，指出真正决定 Agent 系统上限的，不是提示词文件本身，而是 Skills、Harness、状态管理与 Evals 之间的整体工程设计。

## 关键洞察

- gstack 之所以引发争议，不是因为它用了 Markdown，而是因为它把多角色工作流、工程规则和任务分工显式写进了可读的技能文件中。

- “Thin Harness, Fat Skills” 代表一种清晰分工：把判断逻辑放在可读的技能层，把循环、执行、安全和调度留给更薄的运行框架。

- 生产环境里的真正难点不是文件格式，而是状态漂移、上下文溢出、失败循环，以及测试环境与生产环境之间的不一致。

- 仅靠 Markdown 不能保证 Agent 稳定工作，系统还需要 Fat Code、Evals 和显式状态管理来把不确定性约束住。

- 这场争论本质上在重新定义 Agentic Engineering：它不是“写几个提示词”，而是构建一个能长期运行、可调试、可验证的自主软件系统。

## 提取的概念

- [gstack](entities/gstack.md)

- [Harness Engineering](concepts/Harness Engineering.md)

- [Thin Harness, Fat Skills](concepts/Thin Harness, Fat Skills.md)

- [Fat Code](concepts/Fat Code.md)

- [Evals](concepts/Evals.md)

- [状态漂移](concepts/状态漂移.md)

- [AGENTS.md](concepts/AGENTS.md.md)

## 原始文章信息

- 作者：@garrytan

- 来源：X书签

- 发布时间：2026-04-18

- 链接：[原文](https://x.com/garrytan/status/2045371983312097409)

## 个人评注

这篇材料对 Tizer 的启发在于：内容管线里沉淀下来的规则、模板和 Wiki 词条，确实可以像 Skills 一样成为 Agent 的“可读大脑”；但如果没有稳定的编排层、去重机制、状态回写和质量校验，这些知识文件很快就会在长流程里失效。换句话说，知识资产和执行框架必须一起设计，才能把内容编译流程真正做成可持续的 Agent 系统。
