---
title: Craft Agents
type: entity
tags:
- AI 产品
- MCP 协议
status: 草稿
confidence: medium
last_compiled: '2026-04-29'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/26a81841268f46949fb880a79f754d13
notion_id: 26a81841-268f-4694-9fb8-80a79f754d13
---

## 定义

Craft Agents 是一款开源桌面端 AI Agent 界面应用，支持连接任意 API 或 MCP 服务器，专注于非编程场景的 Agent 交互体验。由 Craft 团队开发，官网为 [agents.craft.do](http://agents.craft.do/)。

别名：Craft Agent

## 关键要点

- **开源桌面应用**：提供本地化的 Agent 交互界面，UI 设计精良、体验流畅

- **MCP 支持**：可连接任意 MCP 服务器，扩展 Agent 能力

- **Skill 管理**：内置 Skill 管理功能，支持直接查看和调用 Skill 的 markdown 定义文件

- **任务管理**：所有任务可视化、支持状态跟踪和归档

- **定时任务**：支持定时执行，适合自动化工作流

- **Workspace 隔离**：支持多 Workspace，相当于不同项目空间

- **Telegram 集成**：支持连接 Telegram 进行消息交互

- **适用场景**：主要面向非编程场景（如写文案），编程场景推荐搭配 opencode 使用

## 已知问题

- LiteLLM 接入存在 bug（从 v0.2.6 起），模型查找和权限验证报错，GitHub 已有多个 issue

- DeepSeek 模型兼容性不佳，不支持 Response API，工具调用报错

## 来源引用

- [摘要：再次推荐，这是我目前体验最好的桌面端 agent 产品](summaries/摘要：再次推荐，这是我目前体验最好的桌面端 agent 产品.md)（[原文](https://x.com/indie_maker_fox/status/2049298653588947330)）

## 关联概念

- [OpenCode](entities/OpenCode.md)
