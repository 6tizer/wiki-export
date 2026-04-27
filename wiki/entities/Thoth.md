---
title: Thoth
type: entity
tags:
- AI 产品
- 长期记忆
- 知识管理
status: 草稿
confidence: medium
last_compiled: '2026-04-27'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/1c1b691f21ae4a668be1ad864405b56c
notion_id: 1c1b691f-21ae-4a66-8be1-ad864405b56c
---

## 定义

Thoth 是一个本地优先（local-first）的个人 AI 助手，以「Personal AI Sovereignty」（个人 AI 主权）为核心理念。命名取自古埃及智慧与书写之神 𓁟。基于 LangGraph ReAct Agent 架构，集成 28 个核心工具模块，支持 5 个消息通道（Telegram、WhatsApp、Discord、Slack、SMS），可通过 Ollama 本地运行或接入云端模型。

- GitHub: [https://github.com/siddsachar/Thoth](https://github.com/siddsachar/Thoth)

- 开源协议: Apache-2.0

- Stars: 318（截至 2026-04-27）

- 语言: Python

- 平台: Windows / macOS（一键安装）

## 关键要点

- **本地优先架构**：所有对话、记忆、知识图谱、文档存储在本地 `~/.thoth/`，无需注册账号、无服务端

- **个人知识图谱**：构建实体-关系知识图谱，支持 67 种有向关系、FAISS 语义检索 + NetworkX 1-hop 扩展、艾宾浩斯衰减机制

- **28 个工具模块**：包括 Web 搜索、Gmail、Google Calendar、文件系统、Shell、浏览器自动化、Vision、Designer Studio 等

- **多模型支持**：本地模型通过 Ollama（推荐 qwen3:14b），云端支持 OpenAI、Anthropic、Google AI、xAI、OpenRouter

- **插件市场**：内置插件系统与市场

- **Designer Studio**：五种模式——幻灯片、文档、着陆页、应用原型、动画故事板

- **健康追踪**：用药记录、习惯追踪、趋势分析

## 关联概念

- [Subagents 并行](concepts/Subagents 并行.md)

- [Git Worktree](concepts/Git Worktree.md)

## 来源引用

- [摘要：Cursor 3 /multitask 异步子代理并行执行](summaries/摘要：Cursor 3 -multitask 异步子代理并行执行.md)（[原文](https://x.com/cursor_ai/status/2047764651363180839)）
