---
title: pikiclaw
type: entity
tags:
- Agent 编排
- 开发工具
- CLI 工具
- MCP 协议
status: 草稿
confidence: high
last_compiled: '2026-04-23'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/dca226112c4844b191d27983a661b301
notion_id: dca22611-2c48-44b1-91d2-7983a661b301
---

## 定义

pikiclaw 是一个开源 Node.js 工具，通过 Telegram、飞书、微信等 IM 应用将本地 AI Coding Agent（Claude Code、Codex CLI、Gemini CLI）暴露为可远程控制的接口，让用户在离开电脑时仍能通过手机管理和监控本地运行的 Agent 任务。

官方仓库：[https://github.com/xiaotonng/pikiclaw](https://github.com/xiaotonng/pikiclaw)

## 核心特点

- **一行启动**：`npx pikiclaw@latest`，无需全局安装

- **官方 CLI 原生桥接**：直接调用 claude/codex/gemini 原生 CLI，而非自研包装器

- **多 IM 支持**：Telegram、飞书、微信同时运行

- **Web Dashboard**：[http://localhost:3939](http://localhost:3939/) 管理 IM 渠道、Agent 配置、会话状态

- **MCP 桥接**：每个 Agent 会话注入 `im_list_files`、`im_send_file` 等本地工具

- **Skills 系统**：项目级 `.pikiclaw/skills/*/SKILL.md`，兼容 `.claude/commands/*.md`

- **Codex Human Loop**：Codex 请求用户输入时，通过 IM 转发提示并继续任务

- **GUI 自动化**：可选 Playwright MCP（浏览器）+ Appium Mac2（macOS 桌面）

## 与 OpenClaw 的关系

均属于「IM 接入 Agent」思路，pikiclaw 面向本地 CLI Agent，强调本机环境不变。

## 来源引用

- 未匹配：X 推文回复（@sthnavy，2026-04-10）

- 未匹配：GitHub README
