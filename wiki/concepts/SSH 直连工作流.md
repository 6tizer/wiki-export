---
title: SSH 直连工作流
type: concept
tags:
- Agent 安全
- Harness 工程
status: 审核中
confidence: medium
last_compiled: '2026-04-12'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/a9550d2477e24fa9bd59073115f0c88d
notion_id: a9550d24-77e2-4fa9-bd59-073115f0c88d
---

## 定义

SSH 直连工作流是指桌面端或本地端不经过额外网关层，直接通过 SSH 进入远程主机并操作目标工作流的运行环境。

## 关键要点

- **减少中间层**：省去网关 API、额外代理层或浏览器壳

- **更贴近真实运行环境**：直接面向远程服务器上的工作流与终端

- **体验依赖网络质量**：一旦 SSH 稳定性或延迟波动，使用体验会明显受影响

- **适合开发与运维混合场景**：既需要查看工作流，又需要随时进入终端操作

## 来源引用

- [原文链接](https://x.com/billtheinvestor/status/2042946398124150891)｜X书签｜来源条目：Hermes Desktop：用原生 macOS 应用直连远程 AI 工作流，彻底告别浏览器壳
