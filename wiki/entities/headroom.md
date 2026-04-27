---
title: headroom
type: entity
tags:
- 上下文管理
- CLI 工具
status: 草稿
confidence: medium
last_compiled: '2026-04-27'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/cbd0b0f4df1e46b0b8b32d6856f0c715
notion_id: cbd0b0f4-df1e-46b0-b8b3-2d6856f0c715
---

## 定义

headroom 是一个开源 CLI 工具，用于在 Claude Code 的终端状态栏实时显示上下文窗口使用率，帮助开发者在达到上下文上限前主动管理会话。

## 档案

- **仓库**: [henchmarketing-rgb/headroom](https://github.com/henchmarketing-rgb/headroom)

- **语言**: Shell + Python 3

- **Stars**: 38（截至 2026-04-27）

- **协议**: MIT

- **创建时间**: 2026-04-23

## 关键要点

- 通过 `PostToolUse` Hook 在每次 Bash/Agent/Write 调用后读取 session JSONL，计算并显示上下文窗口使用百分比

- 状态栏渲染示例：`████████░░ 78.3%`

- 自动检测模型类型（从 JSONL 读取而非环境变量），支持 Sonnet 4.6 标准 200k 和 max effort 1M 窗口自动切换

- 每个目录独立追踪，多窗口不互相干扰

- 一行 curl 安装，重启 Claude Code 即可激活

## 来源引用

- [摘要：Claude Code Web/Mobile 刷新与 Teleport 功能发布](summaries/摘要：Claude Code Web-Mobile 刷新与 Teleport 功能发布.md)（[原文](https://x.com/ClaudeDevs/status/2047773528121049488)）
