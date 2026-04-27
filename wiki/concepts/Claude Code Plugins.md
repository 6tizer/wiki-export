---
title: Claude Code Plugins
type: concept
tags:
- CLI 工具
- 商业/生态
status: 草稿
confidence: medium
last_compiled: '2026-04-27'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/50499df8a01f4be69b69baf563937951
notion_id: 50499df8-a01f-4be6-9b69-baf563937951
---

## 定义

Claude Code Plugins 是 Anthropic 为 Claude Code CLI 提供的插件生态系统，允许第三方开发者通过官方 Marketplace 分发工具插件，扩展 Claude Code 的能力边界。用户可通过终端命令一键安装插件，无需手动配置 MCP Server。

## 关键要点

- 插件通过 `claude plugin marketplace update` 和 `claude plugin i` 命令安装，采用终端优先的工作流

- 插件基于 MCP 协议实现，但封装为更易分发和使用的形式

- 官方 Marketplace（claude-plugins-official）提供经过审核的插件源

- 插件可以教会 Claude 特定的搜索模式和工作流，通过 subagent 并行执行任务

- 这一模式将 Claude Code 从单一 coding agent 扩展为可组合的通用 agent 平台

## 来源引用

- [摘要：Introducing Exa for Claude:](summaries/摘要：Introducing Exa for Claude-.md)（[原文](https://x.com/ExaAILabs/status/2047735503794094485)）

## 关联概念

- [Claude Code](entities/Claude Code.md)
