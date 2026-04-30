---
title: KVM 微虚拟机
type: concept
tags:
- 开发工具
- 安全/隐私
status: 审核中
confidence: high
last_compiled: '2026-04-23'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/bf02861e691a4c4f9e0eb9ef3c38a29c
notion_id: bf02861e-691a-4c4f-9e0e-b9ef3c38a29c
---

## 定义

KVM 微虚拟机是一类基于硬件虚拟化能力构建的轻量虚拟机运行模式，兼顾比容器更强的隔离性与比传统虚拟机更低的启动和资源开销。

## 关键要点

- 核心价值是在安全隔离与性能之间取得平衡。

- 相比共享宿主内核的容器方案，它更适合运行 LLM 生成的高风险代码。

- 在 Agent 基础设施里，微虚拟机常被用于浏览器操作、代码执行和临时任务沙箱。

## 来源引用

- [摘要：Blazing-fast cold start:](summaries/摘要：Blazing-fast cold start-.md)（[原文](https://x.com/nash_su/status/2046778396844454105)）

- [摘要：腾讯云开源了 AI Agent 沙盒 Cube Sandbox，Rust 编写，Apache 2.0 协议。](summaries/摘要：腾讯云开源了 AI Agent 沙盒 Cube Sandbox，Rust 编写，Apache 2.0 协议。.md)（[原文](https://x.com/0xLogicrw/status/2046515815940592100)）
