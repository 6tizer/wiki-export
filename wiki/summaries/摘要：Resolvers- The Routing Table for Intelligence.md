---
title: '摘要：Resolvers: The Routing Table for Intelligence'
type: summary
tags:
- Agent 协作模式
- 知识管理
- 上下文管理
- OpenClaw
status: 已审核
confidence: high
last_compiled: '2026-04-20'
source_tags: Agent, Claude, OpenClaw, 自动化, LLM
source_article_url: https://www.notion.so/348701074b6881ddbc03ce5305a7bda0
notion_url: https://www.notion.so/Tizer/5db45dcd6c074f0aa1bb74ec6553f021
notion_id: 5db45dcd-6c07-4f0a-a1bb-74ec6553f021
---

## 一句话摘要

这篇文章把 **Resolver** 定义为 Agent 系统的治理层：它不是把所有知识硬塞进上下文，而是用一张可测试、可演化的“路由表”在正确时刻加载正确上下文、技能和文件，从而避免系统在规模化后滑向误路由、暗能力和 Context Rot。

## 关键洞察

- **Resolver 的本质不是提示词优化，而是上下文路由。** 作者用 200 行决策树替代 20,000 行 `CLAUDE.md`，把“全量塞入上下文”改成“按任务类型按需加载”，显著改善响应速度、准确性和归档质量。

- **技能内部各自维护隐性规则，会让知识库慢慢退化成杂物抽屉。** 真正的修复方式不是逐个修 bug，而是强制所有写入型技能在落库前先读取统一的 `RESOLVER.md` 与 filing rules。

- **Agent 系统最大的隐患不是没有技能，而是“技能存在但不可达”。** 当 resolver 没有登记触发条件时，系统会制造“看似会、实际调不出来”的暗能力，因此需要 trigger evals 与 `check-resolvable` 这类治理机制。

- **Resolver 会像组织结构一样自然腐烂。** 新技能、真实用户措辞、任务优先级都会在 30-90 天内让路由表失真，因此 resolver 必须被持续评测，而不是一次性写完。

- **最值得关注的终局不是更长 prompt，而是自我修复的路由层。** 作者把 resolver 视作可从真实任务流量中学习的治理层，这为长期运行的 Agent 组织提供了演化方向。

## 提取的概念

- [Resolver](concepts/Resolver.md)

- [Thin Harness, Fat Skills](concepts/Thin Harness, Fat Skills.md)

- [Trigger Evals](concepts/Trigger Evals.md)

- [check-resolvable](concepts/check-resolvable.md)

- [Context Rot](concepts/Context Rot.md)

- [GBrain](entities/GBrain.md)

- [gstack](entities/gstack.md)

## 原始文章信息

- 作者：@garrytan

- 来源：X书签

- 发布时间：2026-04-15

- 原文链接：[https://x.com/garrytan/status/2044479509874020852](https://x.com/garrytan/status/2044479509874020852)

## 个人评注

这篇文章对 Tizer 当前的 Wiki / Compiler / Agent 工作流很有启发：我们已经在做“内容入库—知识编译—引用回填”的流水线，但如果没有显式的 resolver、去重规则、来源约束和可达性检查，系统规模一大也会出现误归档、重复概念和能力失联。它提醒我们，真正让 Agent 变稳的不是继续堆 prompt，而是把“谁处理什么、先读什么、写到哪里、如何验证路由正确”沉淀成可审计的治理文档。
