---
title: SuperHQ
type: entity
tags:
- Coding Agent
status: 草稿
confidence: medium
last_compiled: '2026-04-22'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/1e9b20c36bf14e35aa496be61ac13bb3
notion_id: 1e9b20c3-6bf1-4e35-aa49-6be61ac13bb3
---

## 定义

SuperHQ 是一个使用 Rust + GPUI 框架构建的沙箱化 AI Agent 编排平台，允许在隔离 VM 环境中并行运行多个 AI Coding Agent（Claude Code、OpenAI Codex 等），并通过 Auth Gateway 保护真实 API Key 不暴露给沙箱。

官方仓库：[https://github.com/superhq-ai/superhq](https://github.com/superhq-ai/superhq)

## 核心特点

- **VM 沙箱隔离**：每个工作区运行在独立 VM，有独立文件系统、网络和资源限制

- **Auth Gateway**：反向代理拦截 Agent 的 API 请求，注入真实凭证，沙箱内只看到假 key

- **支持 ChatGPT OAuth**：Codex 可通过 OAuth 使用 ChatGPT Plus/Pro 订阅，无需单独 API key

- **GPUI 渲染**：基于 Zed 编辑器的 GPU 加速 UI 框架

- **端口管理**：沙箱端口与宿主机双向转发

- **Diff 审查面板**：查看 Agent 产生的文件变更 unified diff

- **状态**：非常早期 Alpha，主要支持 macOS 14+（Apple Silicon）

## 技术架构

- UI：GPUI（GPU-accelerated，源自 Zed 编辑器）

- VM 编排：shuru-sdk

- 配置存储：SQLite（AES-256-GCM 加密）

## 来源引用

- X 推文回复：[https://x.com/berryxia/status/2042603510102184346（@harshthedev，2026-04-10）](https://x.com/berryxia/status/2042603510102184346（@harshthedev，2026-04-10）)

- GitHub README：[https://github.com/superhq-ai/superhq](https://github.com/superhq-ai/superhq)
