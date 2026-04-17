---
title: 摘要：Thin Harness, Fat Skills
type: summary
tags:
- Coding Agent
- Agent 编排
status: 已审核
confidence: high
last_compiled: '2026-04-15'
source_tags: ''
source_article_url: https://www.notion.so/343701074b68816bbdf5c98528c32af8
notion_url: https://www.notion.so/ef81287197084aa6a0fc4429adba3b37
notion_id: ef812871-9708-4aa6-a0fc-4429adba3b37
---

## 一句话摘要

这篇文章提出一个高杠杆 Agent 架构原则：不要一味追求更强模型，而应把可复用判断沉淀为 Skills，把执行交给确定性工具，并让 Harness 只承担最薄的一层运行时职责。

## 关键洞察

- 决定 AI coding agent 上下限的，往往不是模型本身，而是包裹模型的 harness 设计

- Skill 文件更像可传参的方法调用，用来封装流程、判断和领域知识，而不是一次性提示词

- Resolver 负责按任务自动装载正确上下文，避免把海量知识硬塞进主提示中

- 需要判断与综合的步骤应交给模型，需要稳定与可验证的步骤应交给确定性系统

- Diarization 代表了一类高价值知识工作：跨文档阅读后生成结构化画像和判断摘要

## 提取的概念

- [Thin Harness, Fat Skills](concepts/Thin Harness, Fat Skills.md)

- [Agent Harness](concepts/Agent Harness.md)

- [Agent Skills](concepts/Agent Skills.md)

- [Resolver](concepts/Resolver.md)

- [Latent vs. Deterministic](concepts/Latent vs. Deterministic.md)

- [Diarization](concepts/Diarization.md)

## 原始文章信息

- 作者：@garrytan

- 来源：X书签

- 发布时间：2026-04-11

- 链接：[https://x.com/garrytan/status/2042925773300908103](https://x.com/garrytan/status/2042925773300908103)

## 个人评注

这套思路和 Tizer 当前的知识编译与 Agent 工作流高度契合：把稳定动作沉到数据库、脚本和结构化流程里，把判断性工作上提到可复用的技能与知识条目中，才能让 OpenClaw / 内容管线持续复利。
