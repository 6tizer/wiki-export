---
title: Nezha
type: entity
tags:
- Coding Agent
- IDE 集成
- 代码生成
- Agent 编排
- 工作流
status: 审核中
confidence: high
last_compiled: '2026-04-29'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/8de74836e2804df0b5026e5310117f53
notion_id: 8de74836-e280-4df0-b502-6e5310117f53
---

## 定义

Nezha（哪吒）是一款基于 Tauri + React 的 Agent-First Vibe Coding 桌面应用，专为并行管理多项目、多 AI Coding Agent（Claude Code、Codex CLI）而设计，集成任务生命周期跟踪、原生终端、Session 回放、Git 工作流和内置代码编辑器。

官方仓库：[https://github.com/hanshuaikang/nezha](https://github.com/hanshuaikang/nezha)

## 核心特点

- **多项目并行**：左侧项目导航栏一键切换，终端在后台持续运行

- **Agent-First 哲学**：内置终端直接集成 Claude Code / Codex 原生 CLI，支持多实例并行

- **Session 自动发现与回放**：任务完成后自动关联 session 记录，支持随时恢复

- **HITL 提醒**：等待用户确认的任务以黄色指示器高亮

- **Native Git 集成**：AI 辅助 Git commit message 生成

- **极轻量**：安装包仅 7MB（Tauri 技术栈，无 Electron 臃肿）

- **Usage Analytics**：每周 Token 消耗和工具调用统计

## 与 Tizer 工作流的关系

Nezha 的 Agent-First 并行哲学与 OpenClaw 生态高度契合，其 HITL 提醒机制和 session 可视化对于 HITL 工作流有参考价值。

## 来源引用

- [摘要：用 Claude 替代彭博终端：10 个提示词让你在家搭建私人量化分析师](summaries/摘要：用 Claude 替代彭博终端：10 个提示词让你在家搭建私人量化分析师.md)（[原文](https://x.com/NextBullReady/status/2031248942915268815)，文章链接）

- 未匹配：GitHub README
