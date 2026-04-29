---
title: holaOS
type: entity
tags:
- Harness 工程
- AI 产品
status: 草稿
confidence: high
last_compiled: '2026-04-30'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/9d804598f6e148359ee504f42b08b535
notion_id: 9d804598-f6e1-4835-9ee5-04f42b08b535
---

## 定义

holaOS 是一个开源的 Agent Computer（智能体计算机），由 Holaboss AI 开发，旨在为人类与 AI Agent 提供共享的持久工作环境。与传统 Agent Harness 不同，holaOS 将计算机本身重新定义为一个协作操作系统，让人类和 Agent 在同一浏览器、文件系统和应用中并肩工作。

**别名**：Agent Computer、holaOS Agent Computer

## 关键要点

- **共享环境**：人类与 Agent 在同一操作上下文中工作，Agent 不是外部调用者，而是环境内的协作者

- **持久性**：工作状态在 run 结束后不会丢失，支持长周期任务的连续性

- **可检查性**：所有执行状态、文件、内存对人类和 Agent 均可见

- **开源 MIT 协议**：GitHub 仓库 `holaboss-ai/holaOS`，3400+ Stars，TypeScript 实现

- **核心理念**：Environment Engineering > Harness Engineering——环境定义系统

## 技术档案

- **仓库**：[https://github.com/holaboss-ai/holaOS](https://github.com/holaboss-ai/holaOS)

- **语言**：TypeScript

- **桌面框架**：Electron

- **许可证**：MIT

- **Stars**：3,403（截至 2026-04-29）

- **创建时间**：2026-03-22

- **创始人**：Jeffrey Li (@JeliPenguin)

## 核心架构

- **Workspace 模型**：工作空间作为持久化单元，包含文件、内存、应用状态

- **Registry**：用于发布和拉取可复用工作空间

- **App SDK**：提供现成集成，支持开发者构建自己的应用

- **BYOK**：Bring Your Own Keys，用户自带模型密钥

## 关联概念

- Environment Engineering（环境工程）

- Agent Harness

- Agent OS

## 来源引用

- [摘要：holaOS — 开源 Agent Computer](summaries/摘要：holaOS — 开源 Agent Computer.md)（[原文](https://x.com/JeliPenguin/status/2049147344315388281)）
