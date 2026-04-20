---
title: notebooklm-client
type: entity
tags:
- Agent 技能
- 知识管理
status: 草稿
confidence: high
last_compiled: '2026-04-20'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/22dc6754067d4dd289651ca96bb623c9
notion_id: 22dc6754-067d-4dd2-8965-1ca96bb623c9
---

## 定义

notebooklm-client 是一个非官方的 NotebookLM 第三方客户端与命令行工具，通过逆向 NotebookLM 的内部协议，让用户可以在终端里访问 notebook、发起对话，并把 NotebookLM 能力接入 Agent 工作流。

## 关键要点

- 它同时提供 CLI 与 library 形态，可用于列出 notebook、查看详情、发起 chat，以及生成报告、音频、幻灯片等产物。

- 通过 `npx notebooklm skill install`，它可以把 NotebookLM 能力接入 Claude Code、Codex 等 Agent 环境。

- 首次使用通常需要导出 Google 登录 session，因此 session 文件本身需要妥善保管。

- 由于它依赖非官方协议，存在后端变更后失效或需要重新适配的风险。

## 来源引用

- [摘要：用好NotebookLM立省80%Token](summaries/摘要：用好NotebookLM立省80%Token.md)（[原文](https://x.com/MinLiBuilds/status/2046002143937941988)）

## 关联概念

- [NotebookLM](entities/NotebookLM.md)

- [Claude Code](entities/Claude Code.md)
