---
title: 隔离式 Agent
type: concept
tags:
- Agent 编排
status: 审核中
confidence: medium
last_compiled: '2026-04-15'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/e9fd075812404250bdf0b7fc23f551bc
notion_id: e9fd0758-1240-4250-bdf0-b7fc23f551bc
---

## 定义

隔离式 Agent 指把批评、重写、综合、评审等不同角色拆给相互隔离的 agent，各角色之间不直接共享上下文，只通过明确的中间产物传递信息，以减少自我认同和回声室效应。

## 核心要点

- 角色隔离让批评不再只是同一个模型对自己“客气地润色”

- 作者 agent 只读取 critique，不读取原稿，可以逼出真正不同的候选版本

- 评审 agent 不看批评过程，有助于降低路径依赖

- 适合需要引入真实分歧的内容、策略和判断型任务

## 来源引用

- [原文链接](https://x.com/shannholmberg/status/2043983746094026984)｜《how to use autoreason for marketing》｜源文章：Autoreason：用多智能体对抗博弈，打磨你的营销文案

- [原文链接](https://x.com/nyk_builderz/status/2044472463279710344)｜《The Ultimate Hermes Guide - from one agent to a 4-profile team that still feels coherent on day 30》｜来源条目：[摘要：The Ultimate Hermes Guide - from one agent to a 4-profile team that still feels coherent on day 30](summaries/摘要：The Ultimate Hermes Guide - from one agent to a 4-profile team that still feels coherent on day 30.md)

- [摘要：Audit, fix, and optimize any website to be cited by ChatGPT, Perplexity, Claude, and Gemini.](summaries/摘要：Audit, fix, and optimize any website to be cited by ChatGPT, Perplexity, Claude, and Gemini.md)（[原文](https://x.com/shannholmberg/status/2046891905389334958)）

## 关联概念

- [Autoreason](concepts/Autoreason.md)

- [Borda count](concepts/Borda count.md)

- [autoresearch](entities/autoresearch.md)

- [组织级知识层](concepts/组织级知识层.md)

- [Hermes Agent](entities/Hermes Agent.md)

- [Memory KPI](concepts/Memory KPI.md)

- [Policy Gate](concepts/Policy Gate.md)
