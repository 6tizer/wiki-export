---
title: 摘要：Creating a Second Brain with Claude Code
type: summary
tags:
- Coding Agent
- 记忆系统
status: 已审核
confidence: high
last_compiled: '2026-04-16'
source_tags: ''
source_article_url: https://www.notion.so/344701074b6881bc8579c44db19b3a6b
notion_url: https://www.notion.so/9df183f3f9af4f9bb211de7c4788fdad
notion_id: 9df183f3-f9af-4f9b-b211-de7c4788fdad
---

## 一句话摘要

这篇文章展示了一套以 Claude Code 为执行宿主、以 QMD 为本地检索层、以个人画像与学习闭环为持续更新机制的“第二大脑系统”，其目标是把分散的历史工作资料转化为可随任务实时调用的长期记忆与行动能力。

## 关键洞察

- 第二大脑的核心不是单纯存档资料，而是把**原始文档、个人目标、工具接口、自动触发机制**整合成一个可持续运行的知识操作系统

- **QMD** 负责本地知识库索引与检索，并通过关键词检索和语义检索互补，提升历史资料的召回质量

- 作者先用 `me.md` 和一组中间摘要文档对个人经验做蒸馏，再让 Claude Code 在执行任务时自动读取相关上下文，避免每次都从零提示

- **Claude Code Hooks**、**MCP 协议** 与各类 CLI/连接器共同构成了“上下文注入 + 工具执行”的动作层，使系统从“会记”进一步走向“会做”

- 真正让系统持续增值的，不是一次性建库，而是**每会话、每日/每周、每月**的学习闭环，让记忆随着工作推进不断修正和增厚

## 提取的概念

- [第二大脑系统](concepts/第二大脑系统.md)

- [QMD](entities/QMD.md)

- [Claude Code](entities/Claude Code.md)

- [Claude Code Hooks](concepts/Claude Code Hooks.md)

- [MCP 协议](concepts/MCP 协议.md)

- [Claude Code Memory](concepts/Claude Code Memory.md)

- [Agent Swarms](concepts/Agent Swarms.md)

## 原始文章信息

- 作者：@rywiggs

- 来源：X书签

- 发布时间：2026/04/15

- 原文链接：[https://x.com/rywiggs/status/2044448092477661638](https://x.com/rywiggs/status/2044448092477661638)

- 源页面：用 Claude Code 打造「第二大脑」：一个 VP 如何把 5 年工作记忆装进 AI

## 个人评注

这篇材料对 Tizer 当前的内容管线和 Wiki 编译体系有直接启发：它强调的不是“知识库存量”，而是**在任务发生时把合适上下文自动送到 Agent 面前**。如果把这一思路迁移到 OpenClaw、HITL 与内容生产链路中，重点就不是再堆更多资料，而是构建“触发器 → 检索 → 蒸馏 → 回写记忆”的闭环，让知识在工作流里持续被调用、验证和再生产。
