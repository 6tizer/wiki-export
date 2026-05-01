---
title: Maestro
type: entity
tags:
- 多Agent协作
- Harness 工程
- 上下文管理
status: 审核中
confidence: high
last_compiled: '2026-04-21'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/5880544fc27147f29de2e28c8d6261c2
notion_id: 5880544f-c271-47f2-9de2-e28c8d6261c2
---

## 定义

Maestro 是一个面向多 Agent 软件工程协作的本地优先编排器，用统一的磁盘状态模型管理任务、记忆、交接和 plan-approve-execute 协作流程。

## 核心要点

- 把 mission、feature、assertion、handoff、checkpoint 等状态存到本地文件系统，而不是依赖服务端

- 适合在多个 Agent 会话之间维持共享上下文与可审计的进度

- 强调 plan-approve-execute 这种分阶段协作方式，适合长任务和多人/多 Agent 协调

- 主要服务于编码工作流，因此与 Claude Code、Codex、Gemini 等 CLI 生态结合紧密

## 来源引用

- [摘要：Hermes Agent 生态继续狂飙，又卷出一大批全新进化体！](summaries/摘要：Hermes Agent 生态继续狂飙，又卷出一大批全新进化体！.md)（[原文](https://x.com/GitTrend0x/status/2045837379827896407)）

- [摘要：Hermes Agent 生态要炸了，这波进化速度把我整不会了！](summaries/摘要：Hermes Agent 生态要炸了，这波进化速度把我整不会了！.md)（[原文](https://x.com/NFTCPS/status/2046076635200553224)）

## 关联概念

- [Hermes Agent](entities/Hermes Agent.md)

- [Claude Code](entities/Claude Code.md)
