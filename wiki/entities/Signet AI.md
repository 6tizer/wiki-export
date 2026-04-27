---
title: Signet AI
type: entity
tags:
- 长期记忆
- CLI 工具
status: 草稿
confidence: medium
last_compiled: '2026-04-27'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/a5e8a1eed0f348ab8d6873f33a77ab49
notion_id: a5e8a1ee-d0f3-48ab-8d68-73f33a77ab49
---

## 定义

Signet AI 是一个本地优先（local-first）的可移植上下文层，为 AI Agent 提供身份、记忆、来源追踪、密钥管理和工作知识的持久化存储。核心理念是让 Agent 的上下文不绑定于任何单一聊天应用、模型提供商或 Harness，实现跨 Harness 的记忆连续性。

## 关键要点

- **LongMemEval 评分 97.6%**：在 MemoryBench rules profile 下的答案准确率

- **本地优先**：数据存储在本机 SQLite 和 Markdown 中，可移植

- **跨 Harness 支持**：兼容 Claude Code、OpenCode、OpenClaw、Codex、Hermes Agent 等

- **三层记忆架构**：workspace/transcripts（真实记录层）→ semantic memory（语义导航层）→ query layer（检索镜头层）

- **混合检索**：FTS5 + 向量搜索 + 图遍历 + 融合排序

- **环境记忆（Ambient Memory）**：自动捕获会话上下文，无需手动记忆仪式

- **多 Agent 策略**：隔离/共享/分组记忆可见性

- 语言：TypeScript

- 许可证：Apache 2.0

- GitHub Stars：128（截至 2026-04-27）

- 仓库：[https://github.com/Signet-AI/signetai](https://github.com/Signet-AI/signetai)

## 来源引用

- [摘要：Graph is the final boss of memory](summaries/摘要：Graph is the final boss of memory.md)（[原文](https://x.com/rohit4verse/status/2048081996841435596)）
