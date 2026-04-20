---
title: A2UI 协议
type: concept
tags:
- Agent 编排
status: 审核中
confidence: high
last_compiled: '2026-04-20'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/639d7a9d1ccc48f696483ce6d3e34933
notion_id: 639d7a9d-1ccc-48f6-9648-3ce6d3e34933
---

## 定义

A2UI（Agent-to-UI）是 Google 于 2025 年底发布的开源协议，核心思想是 AI 只描述「要什么」，客户端决定「怎么画」，实现声明式的 Agent 驱动界面生成。

## 关键要点

- 声明式而非可执行代码：Agent 负责「展示什么」，客户端负责「怎么展示」

- 适合生成式交互型 UI（表单、问卷、投票），与 SDUI 形成互补

- 组件扁平简单，LLM 可自由生成

- 传输协议用 JSONL，3 条消息描述一个完整界面（createSurface → updateComponents → beginRendering）

- 支持流式体验和局部刷新

- 与 MCP、A2A、AG-UI 共同构成 2026 年 AI Agent 协议栈

## 来源引用

- [摘要：从千问点奶茶说起——Generative UI 协议架构实践](summaries/摘要：从千问点奶茶说起——Generative UI 协议架构实践.md)（老码小张，2026-02-28）
