---
title: Agentic Engineering
type: concept
tags:
- Agent 编排
status: 审核中
confidence: medium
last_compiled: '2026-04-11'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/36ddcd72d4f547489ecb48175ca091d3
notion_id: 36ddcd72-d4f5-4748-9ecb-48175ca091d3
---

## 定义

Agentic Engineering 是一种以 AI Coding Agent 为核心执行单元的软件开发范式，将传统「人写代码」模式转变为「人并行调度多个 Agent 执行任务，人负责审查与决策」的模式。

## 核心理念

- **并行化**：多个 Agent 同时在不同项目/任务上工作，突破单线程人工编码瓶颈

- **人作为调度者**：开发者从「执行者」转变为「任务分配 + 结果审查」角色

- **工具链适配**：传统 IDE（VS Code 等）以人为中心设计，不适合 Agentic 场景；需要专为 Agent 管理设计的新工具（SuperConductor、Nezha 等）

- **隔离性**：每个 Agent 任务在独立环境（git worktree、沙箱 VM）中运行，避免互相干扰

## 代表工具

- SuperConductor（原生 macOS Rust）

- Nezha（Tauri，多项目并行）

- SuperHQ（沙箱 VM 隔离）

- pikiclaw（IM 远程控制本地 Agent）

## 与 Vibe Coding 的关系

Vibe Coding 强调「自然语言描述意图，Agent 生成代码」；Agentic Engineering 在此基础上强调多 Agent 并行和工程化管理，是 Vibe Coding 的进阶形态。

## 关联概念

- [Thin Harness, Fat Skills](concepts/Thin Harness, Fat Skills.md)

- [Fat Code](concepts/Fat Code.md)

- [Context Engineering](concepts/Context Engineering.md)

- [Software 3.0](concepts/Software 3.0.md)

- [Vibe Coding](concepts/Vibe Coding.md)

## 来源引用

- [原文链接](https://x.com/chenchengpro/status/2043697811993350611)｜《Garry Tan 提炼了他在 agentic engineering 领域的核心心法：Fat Skills, Fat Code, Thin Harness。》｜源文章：Garry Tan 的 Agent 工程心法：Fat Skills、Fat Code、Thin Harness

- X 推文：[https://x.com/berryxia/status/2042603510102184346（SuperConductor](https://x.com/berryxia/status/2042603510102184346（SuperConductor) 宣传语，2026-04-10）

- [摘要：Karpathy AI Ascent 2026：从 Vibe Coding 到 Agentic Engineering](summaries/摘要：Karpathy AI Ascent 2026：从 Vibe Coding 到 Agentic Engineering.md)（[原文](https://x.com/Av1dlive/status/2049561210593685876)）
