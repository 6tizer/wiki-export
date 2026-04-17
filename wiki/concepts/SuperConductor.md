---
title: SuperConductor
type: concept
tags:
- Coding Agent
status: 草稿
confidence: medium
last_compiled: '2026-04-18'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/639ff05b20474511958ebc7b6b5c23b7
notion_id: 639ff05b-2047-4511-958e-bc7b6b5c23b7
---

## 定义

SuperConductor 是一款原生 macOS 的 AI Coding Agent 管理工具，采用 100% Rust 编写，基于 GPU 渲染（Metal），无 Electron 或 Tauri 依赖，专为并行运行多个 Coding Agent 而设计。

别名：Superconductor

## 核心特点

- **100% Rust + Metal 渲染**：原生性能，启动时间 <50ms，无 Web 运行时

- **Git Worktree 隔离**：每个 Agent 任务运行在独立的 git worktree 中

- **支持多种 CLI Agent**：Claude Code、OpenAI Codex、Gemini CLI 以及任意 CLI Agent

- **多布局工作区**：支持无限标签页与工作区，可 Picture-in-Picture 浮窗

- **专为 Agentic Engineering 设计**：并行调度、diff 审查、PR 状态跟踪一体化

- **Alpha 阶段**：官网 [https://super.engineering/](https://super.engineering/) 开放申请

## 定位

对标 Cursor / Warp 等工具，但聚焦于多 Agent 并行编程场景，而非单人 IDE 体验。

## 来源引用

- X 推文：[https://x.com/berryxia/status/2042603510102184346（@berryxia，2026-04-10）](https://x.com/berryxia/status/2042603510102184346（@berryxia，2026-04-10）)
