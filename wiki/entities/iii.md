---
title: iii
type: entity
tags:
- 多Agent协作
- AI 产品
status: 草稿
confidence: medium
last_compiled: '2026-04-28'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/ccbe991f9eca455bae41f3fc7466aa41
notion_id: ccbe991f-9eca-455b-ae41-f3fc7466aa41
---

## 定义

iii（读作 "three eye"）是一个开源的后端统一与编排系统，由 iii-hq 开发。其核心理念是将传统后端中分散的 API 框架、任务队列、定时调度、事件总线、状态存储、WebSocket 服务器和可观测性管道统一为单一应用级接口。

别名：iii / three eye / Motia（Discord 社区名）

## 关键要点

- **三原语模型**：iii 围绕三个核心原语构建——Worker（任何连接的进程）、Function（Worker 注册的命名工作单元）、Trigger（触发 Function 执行的条件，如 HTTP、Cron、队列、状态变化）

- **Worker 即一切**：Rust daemon、TypeScript 服务、Python 脚本、浏览器标签页、microVM 甚至 LLM 本身都可以作为 Worker 连接到引擎

- **编排模式即触发器**：Supervisor、Swarm、Hierarchical 等多 Agent 编排模式不再是独立架构，而是同一组原语的不同触发器组合

- **沙箱即 Worker**：sandbox::create、sandbox::exec、sandbox::destroy 三个 Function 实现隔离执行，底层可以是 Firecracker、Docker 或 Wasm

- **n+1 扩展**：新能力加入只需连接一个 Worker，无需更新消费者服务、网关配置或注册表

## 技术档案

- GitHub：[https://github.com/iii-hq/iii](https://github.com/iii-hq/iii)

- 文档：[https://iii.dev/docs](https://iii.dev/docs)

- Discord：[https://discord.gg/motia](https://discord.gg/motia)

- 开源协议：待确认

- 语言支持：Rust、TypeScript、Python

## 来源引用

- [摘要：Agents 201: The Unit Shrank](summaries/摘要：Agents 201- The Unit Shrank.md)（[原文](https://x.com/ghumare64/status/2047401813364683007)）
