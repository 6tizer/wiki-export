---
title: 摘要：什么才是真正的 Harness Engineering？
type: summary
tags:
- Coding Agent
- Agent 编排
status: 已审核
confidence: high
last_compiled: '2026-04-20'
source_tags: Agent, 自动化, Hooks, harness, LLM
source_article_url: https://www.notion.so/348701074b688181840de99d10d8ebd7
notion_url: https://www.notion.so/eabf1a6595aa492d9ec5d87552f2b560
notion_id: eabf1a65-95aa-492d-9ec5-d87552f2b560
---

## 一句话摘要

Harness Engineering 的核心不是让模型多写代码，而是把人类对好代码的判断、执行约束与审查流程系统化写进 Agent 的运行环境，让工程师从实现者转为编排者。

## 关键洞察

- 当代码生成本身越来越便宜，真正稀缺的变成了上下文、评审标准、可靠性要求与执行边界。

- 高质量 Agent 不是靠一句 prompt 自觉工作，而是要把 taste、规范、ADR、日志、测试、lint 等沉淀成可调用的工程资产。

- Guardrails 必须进入执行检查点，变成硬约束，而不只是停留在提示词层面的软提醒。

- Skills 配合渐进式披露，可以在控制上下文成本的同时，让 Agent 按需调用团队积累的高价值经验。

- Review agents、CI lints 与 tests 组成了新的验证闭环，使人类从同步 review 中抽离，只在关键节点抽检和设定标准。

## 提取的概念

- [Harness Engineering](concepts/Harness Engineering.md)

- [PreToolUse](concepts/PreToolUse.md)

- [Agent Skills](concepts/Agent Skills.md)

- [渐进式披露](concepts/渐进式披露.md)

- [Guardrails](concepts/Guardrails.md)

- [Review Agents](concepts/Review Agents.md)

## 原始文章信息

- 作者：@SaitoWu

- 来源：X书签

- 发布时间：2026-04-18

- 原文链接：[https://x.com/SaitoWu/status/2045458721929892345](https://x.com/SaitoWu/status/2045458721929892345)

## 个人评注

这篇内容对 Tizer 当前的 AI 编译与内容流水线很有启发：重点不是继续堆 prompt，而是把选题标准、结构要求、去重规则、质检清单和审批节点前移为可复用的 guardrails。这样无论是 Wiki 编译、内容生产还是 Coding Agent 协作，都能把“人类经验”沉淀成长期可复用的编排资产。
