---
title: Cursor SDK
type: entity
tags:
- Harness 工程
- 代码生成
- IDE 集成
status: 草稿
confidence: high
last_compiled: '2026-04-29'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/66f33ebbd5e94bc1bb22c7bf01a32d14
notion_id: 66f33ebb-d5e9-4bc1-bb22-c7bf01a32d14
---

## 定义

Cursor SDK 是 Cursor 官方推出的 TypeScript SDK（npm 包名 `@cursor/sdk`），允许开发者使用与 Cursor 桌面应用、CLI、Web 应用相同的 Agent Runtime、Harness 和前沿模型，以编程方式构建和部署 AI 编码 Agent。

别名：`@cursor/sdk`

## 关键要点

- **同源 Runtime**：SDK 暴露的 Agent 与 Cursor IDE 内置的 Agent 使用完全相同的运行时和 Harness，保证行为一致性

- **多种部署模式**：支持本地执行（`local.cwd`）和 Cursor 云端专用 VM 执行

- **CI/CD 集成**：可直接从 CI/CD 流水线调用 Agent，实现自动化 PR 审查、代码修复等

- **产品嵌入**：允许将 Agent 嵌入到第三方产品中，作为基础设施而非仅 IDE 功能

- **模型支持**：默认使用 `composer-2` 模型，支持多种前沿模型

- **Public Beta 阶段**：通过 `npm install @cursor/sdk` 即可安装，使用 API Key 按 token 计费

- **非开源**：SDK 为专有软件，不开源

## 技术架构

```javascript
import { Agent } from "@cursor/sdk";

const agent = await Agent.create({
  apiKey: process.env.CURSOR_API_KEY,
  model: { id: "composer-2" },
  local: { cwd: process.cwd() },
});

const run = await agent.send("Summarize what this repository does");
for await (const event of run.stream()) {
  console.log(event);
}
```

## 与 Cursor 生态的关系

Cursor SDK 将 Cursor 从一个 IDE 工具转变为 Agent 平台——编辑器是入口，SDK 是基础设施层。开发者可以在不依赖 Cursor 桌面环境的情况下，利用 Cursor 积累的 Harness 工程经验（安全沙箱、状态管理、环境配置、上下文管理）来构建生产级 Agent。

## 来源引用

- [摘要：Cursor SDK — 用编程方式构建与 Cursor 同源的 AI 编码 Agent](summaries/摘要：Cursor SDK — 用编程方式构建与 Cursor 同源的 AI 编码 Agent.md)（[原文](https://x.com/cursor_ai/status/2049499866217185492)）
