---
title: 摘要：Why Everyone Is Suddenly Building Their Own Agent Harness
type: summary
tags:
- Harness 工程
- 商业/生态
status: 已审核
confidence: high
last_compiled: '2026-05-03'
source_tags: ''
source_article_url: https://www.notion.so/355701074b68819894aaf30556f8a8d7
notion_url: https://www.notion.so/Tizer/3aa2d3ff257245d79f65c440aaa5dd9d
notion_id: 3aa2d3ff-2572-45d7-9f65-c440aaa5dd9d
---

## 一句话摘要

当前应用 AI 最重要的转变是：模型不再是产品，围绕模型构建的 Harness 才是——相同模型配合不同 Harness 可以产生 13 分以上的基准差距。

## 关键洞察

- **Harness 定义**：Agent Harness 是将 LLM 从 token 生成器变为可工作 Agent 的所有包裹层——工具调度、上下文管理、沙箱、规划循环、子 Agent 编排、评测、可观测性、验证逻辑

- **模型商品化 vs Harness 复合**：前沿模型在工具使用、长上下文、推理、结构化输出方面正在趋同且价格暴跌；而 Harness 的每次修复都是永久性改进，适用于所有未来运行和未来模型

- **实证案例**：LangChain deepagents-cli 仅改 Harness（模型不变）就从 Terminal-Bench 2.0 的 52.8% 跳到 66.5%；Factory Droid、Stanford IRIS Lab、OpenAI Frontier 团队均证明 Harness 是决定性差异

- **通用框架不够用**：Claude Code、Cursor、Devin、OpenClaw 等成功产品都有定制 Harness，因为上下文窗口需要逐模型调优、工具需为 LLM 而非人类设计、评测须绑定产品而非通用基准

- **何时自建**：原型阶段直接用现有工具；当自研 vs 通用在评测上持续差 15+ 分、每任务经济性重要、或需要现有产品不提供的权限/审计能力时，再自建 Harness

## 提取的概念

- [Agent Harness](concepts/Agent Harness.md)

- [Harness 复合效应](concepts/Harness 复合效应.md)

- [Terminal-Bench 2.0](entities/Terminal-Bench 2.0.md)

- [Deep Agents](entities/Deep Agents.md)

- [Agentic Engineering](concepts/Agentic Engineering.md)

- [Factory Droid](entities/Factory Droid.md)

## 原始文章信息

- **作者**：@code_kartik

- **来源**：X 书签

- **发布时间**：2026-05-02

- **原文链接**：[https://x.com/code_kartik/status/2050631735529095575](https://x.com/code_kartik/status/2050631735529095575)

## 个人评注

本文是对 2026 年 Harness 工程趋势的综述性梳理，把 LangChain / Factory / Stanford / OpenAI 的案例串在一起论证「Harness > Model」。对 Tizer 的 OpenClaw 工作流直接相关：OpenClaw 自身就是一个定制 Harness，文中提到的复合效应、评测驱动迭代、[AGENTS.md](http://agents.md/) 扩展点等思路可直接指导 OpenClaw 的 Harness 层优化策略。文中「何时自建 vs 使用现有」的判断框架（15+ 分评测差距门槛）也是 HITL 决策的实用参考。
