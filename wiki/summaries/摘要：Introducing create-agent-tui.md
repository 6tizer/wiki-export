---
title: 摘要：Introducing "create-agent-tui"
type: summary
tags:
- Harness 工程
- CLI 工具
status: 已审核
confidence: medium
last_compiled: '2026-04-27'
source_tags: ''
source_article_url: https://www.notion.so/34f701074b6881f793f6e5876fb8af86
notion_url: https://www.notion.so/Tizer/eff548f7cac04406837dff2597372637
notion_id: eff548f7-cac0-4406-837d-ff2597372637
---

## 一句话摘要

OpenRouter 发布 create-agent-tui Skill，让开发者基于 OpenRouter Agent SDK 快速搭建自定义终端界面（TUI）的 Agent Harness，支持 4 种 UI 风格和数十种可选功能。

## 关键洞察

- create-agent-tui 是一个交互式脚手架工具，通过向导流程生成带有终端 UI 的 Agent Harness 项目

- 提供 4 种界面自定义维度：Banner 样式、输入框风格（Codex / Claude Code / Pi / 自定义）、加载动画、工具调用显示样式

- 底层依赖 OpenRouter Agent SDK（`@openrouter/agent`），开箱即得类型安全的 Tool Calling 和多轮推理循环

- 另有 headless 版本 create-headless-agent，适用于 CI/CD 等无终端环境

- 作为 OpenRouter Skills 生态的组成部分，代码托管在 GitHub OpenRouterTeam/skills 仓库

## 提取的概念

- [create-agent-tui](entities/create-agent-tui.md)

- [OpenRouter Agent SDK](entities/OpenRouter Agent SDK.md)

- [Agent Harness](concepts/Agent Harness.md)

- [OpenRouter](entities/OpenRouter.md)

## 原始文章信息

- **作者**：@OpenRouter

- **来源**：X 书签

- **发布时间**：2026-04-24

- **链接**：[原文推文](https://x.com/OpenRouter/status/2047701992798392484)

- **GitHub**：[OpenRouterTeam/skills/create-agent-tui](https://github.com/OpenRouterTeam/skills/tree/main/skills/create-agent-tui)

## 个人评注

OpenRouter 正在构建围绕 Agent SDK 的 Skills 生态，create-agent-tui 是其中面向终端开发者的入口工具。对 Tizer 的 OpenClaw 生态有参考价值——TUI 作为 Agent 交互界面的设计思路（自定义 Banner、输入框风格、工具显示）可借鉴到 OpenClaw 的 CLI 体验中。headless 模式尤其值得关注，CI 环境下运行 Agent 是生产级 Harness 的刚需。
