---
title: 规范驱动开发 SDD
type: concept
tags:
- Coding Agent
status: 已审核
confidence: high
last_compiled: '2026-04-30'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/60e9b74d73bd4041a72e43c4127abd94
notion_id: 60e9b74d-73bd-4041-a72e-43c4127abd94
---

## 定义

规范驱动开发（Spec-Driven Development, SDD）是一种 AI 编程范式，核心思想是在让 AI 写代码之前，先用结构化文档描述清楚要做什么、为什么做、怎么做，用规范约束 AI 在自由和纪律间找平衡。

## 关键要点

- 核心理念：AI 代码的质量上限，取决于输入的规范质量

- 演进路径：Copilot 补全 → Vibe Coding → 质量危机 → SDD 用规范约束 AI

- 三大代表工具：OpenSpec（~27K⭐，规范对齐层）、Superpowers（~61K⭐，方法论框架含强制 TDD）、GSD（~23K⭐，子代理隔离解决上下文腐烂）

- 行业背书：Martin Fowler 发文分析、GitHub 推出 Spec Kit、AWS 发布 Kiro IDE

- 趋势判断：SDD 将成为 AI 编程标配，从可选项变为必选项

## 来源引用

- [摘要：AI 编程三大 SDD 工具深度对比（OpenSpec vs Superpowers vs GSD）](summaries/摘要：AI 编程三大 SDD 工具深度对比（OpenSpec vs Superpowers vs GSD）.md)（机智流 AI Insight，2026-03-02）— 从 11 个维度深度对比 OpenSpec/Superpowers/GSD 三个工具，分析 SDD 赛道趋势

- [摘要：AI开发范式——Spec Kit、OpenSpec、BMAD 全解析](summaries/摘要：AI开发范式——Spec Kit、OpenSpec、BMAD 全解析.md)（娄晨，2026-03-03）— 深入对比 Spec Kit/OpenSpec/BMAD 三个框架，含腾讯工程师实践失败案例，提出 Context Engineering 和 Compound Engineering 是更底层的进化方向

- [摘要：OpenAI开源Symphony：给每一个任务配一个永不下班的 AI员工](summaries/摘要：OpenAI开源Symphony：给每一个任务配一个永不下班的 AI员工.md)（[原文](https://x.com/vista8/status/2049484504444834126)）— Symphony 用 [SPEC.md](http://spec.md/) 定义协议，让 Codex 用多语言实现，验证了规范驱动开发的可行性
