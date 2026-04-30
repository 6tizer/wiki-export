---
title: Cube Sandbox
type: entity
tags:
- 开发工具
- 安全/隐私
status: 审核中
confidence: high
last_compiled: '2026-04-23'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/1cc1c116cef241029f22dbc08bc0257f
notion_id: 1cc1c116-cef2-4102-9f22-dbc08bc0257f
---

## 定义

Cube Sandbox 是腾讯开源的 AI Agent 沙箱运行时，基于 KVM 微虚拟机、RustVMM 与 eBPF 网络隔离，强调高安全、低冷启动和高并发密度，并兼容 E2B SDK。

## 关键要点

- 面向 AI Agent 的代码执行与工具运行场景，而不是通用容器托管。

- 通过快照克隆与资源池预热，把可用沙箱的冷启动压缩到毫秒级。

- 以独立 Guest Kernel 提供比共享内核容器更强的隔离边界。

- 兼容 E2B 接口，降低现有 Agent 基础设施从闭源沙箱迁移的成本。

## 来源引用

- [摘要：Blazing-fast cold start:](summaries/摘要：Blazing-fast cold start-.md)（[原文](https://x.com/nash_su/status/2046778396844454105)）

- [摘要：腾讯云开源了 AI Agent 沙盒 Cube Sandbox，Rust 编写，Apache 2.0 协议。](summaries/摘要：腾讯云开源了 AI Agent 沙盒 Cube Sandbox，Rust 编写，Apache 2.0 协议。.md)（[原文](https://x.com/0xLogicrw/status/2046515815940592100)）
