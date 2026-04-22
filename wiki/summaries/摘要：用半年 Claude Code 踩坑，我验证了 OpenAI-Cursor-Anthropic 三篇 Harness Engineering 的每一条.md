---
title: 摘要：用半年 Claude Code 踩坑，我验证了 OpenAI/Cursor/Anthropic 三篇 Harness Engineering 的每一条
type: summary
tags:
- Coding Agent
- Agent 编排
status: 已审核
confidence: high
last_compiled: '2026-04-12'
source_tags: Agent, LLM, Cursor, 自动化
source_article_url: https://www.notion.so/33e701074b688191b796ffbe91ac8eb5
notion_url: https://www.notion.so/76f65ce3369942d0a95bad662687276e
notion_id: 76f65ce3-3699-42d0-a95b-ad662687276e
---

## 一句话摘要

Harness Engineering 的本质不是调 prompt，而是为 Agent 建立可持续工作的上下文、隔离与状态管理体系。

## 关键洞察

- 三家大厂讨论的是同一个问题的不同维度：环境可见性、并行隔离与长时可靠性。

- Git Worktree 这类隔离机制对多 Agent 并行开发非常关键，否则改动互相覆盖几乎不可避免。

- 长 Session 的最大风险不是显式报错，而是悄悄忘约束、悄悄跑偏。

- 把 SSOT 路由表、[CLAUDE.md](http://claude.md/)、行为规则文件外置出来，本质上是在替 Agent 建“外脑”。

## 提取的概念

- [Harness Engineering](concepts/Harness Engineering.md)

- [Git Worktree](concepts/Git Worktree.md)

- [上下文焦虑](concepts/上下文焦虑.md)

- [SSOT 路由表](concepts/SSOT 路由表.md)

- [CLAUDE.md](concepts/CLAUDE.md.md)

## 原始文章信息

- 作者：@runes_leo

- 来源：X书签

- 发布时间：2026-04-09

- 链接：[https://x.com/runes_leo/status/2042243228678693244](https://x.com/runes_leo/status/2042243228678693244)

## 个人评注

这类“把环境当产品做”的思路，和 Tizer 的 OpenClaw 养虾、内容流水线、长期任务稳定性治理直接相关，值得持续沉淀。
