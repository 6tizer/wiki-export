---
title: Memory KPI
type: concept
tags:
- 记忆系统
- Agent 编排
status: 审核中
confidence: high
last_compiled: '2026-04-16'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/d0e20e281bc946b181b8e914fd32175d
notion_id: d0e20e28-1bc9-46b1-81b8-e914fd32175d
---

## 定义

Memory KPI 是针对每个 Agent profile 单独维护的一组记忆健康指标，用来衡量该角色的记忆是否仍然新鲜、可追溯、彼此一致，避免多 Agent 团队在长期运行后重新塌缩成“同一个模糊声音”。

## 关键要点

- 不看整个系统的总记忆，而是按 profile 分开观测

- 重点关注 `stale_notes`、来源支撑比例、矛盾笔记等信号

- 一旦某个 profile 的陈旧记忆占比过高，就应安排清理、resolve 或重建上下文

- 它让“隔离运行”从结构设计升级为可量化、可运维的长期机制

## 来源引用

- [原文链接](https://x.com/nyk_builderz/status/2044472463279710344)｜《The Ultimate Hermes Guide - from one agent to a 4-profile team that still feels coherent on day 30》｜源文章：Hermes 多 Agent 团队：如何让四个角色在第 30 天还保持分工清晰

## 关联概念

- [Hermes Agent](entities/Hermes Agent.md)

- [隔离式 Agent](concepts/隔离式 Agent.md)

- [Handoff 文档](concepts/Handoff 文档.md)
