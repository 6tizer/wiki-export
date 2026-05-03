---
title: 摘要：Orb 自建记忆与路由的 Claude Code 封装框架
type: summary
tags:
- Agent 协作模式
- 长期记忆
- CLI 工具
status: 已审核
confidence: high
last_compiled: '2026-05-03'
source_tags: ''
source_article_url: https://www.notion.so/355701074b688115b29efe7d68ee5414
notion_url: https://www.notion.so/Tizer/397b8c78b2524abc9a9959250c8dc450
notion_id: 397b8c78-b252-4abc-9a99-59250c8dc450
---

## 一句话摘要

Orb 是一个围绕 Claude Code CLI 的多 profile 消息壳层，自建记忆、进化、路由三大核心能力，不依赖任何第三方 Agent 框架，直接对接 Slack 原生 Agent 能力实现深度集成。

## 关键洞察

- **不替代 Agent runtime，只做封装**：Orb 不重写 Claude Code 的运行时逻辑，而是在其外围提供路由、profile 隔离、长期记忆、文档检索、cron 调度和审批处理，Claude Code 升级无需迁移 prompt stack

- **Holographic Memory 分层记忆架构**：本地 SQLite 事实库支持信任评分、衰减控制和矛盾处理，与 Claude Code 自带的 auto-memory 形成「Orb 跨线程召回 + CLI workspace 记忆」的分层互补

- **Multi-profile 完全隔离**：每个 Agent 角色拥有独立的 scripts/workspace/data 目录，记忆库、文档索引、定时任务彼此隔离，系统级 skills 可跨 profile 共享

- **MCP Permission Relay 人在回路审批**：通过 MCP tool server 将 Claude Code 的权限请求转发到 Slack 审批卡片，实现敏感操作的实时人工审批

- **Slack 原生能力深度集成**：直接使用 assistant thread、流式 task card、按钮回调路由等 Slack 两个月内新放出的 agent 原生能力，套壳框架无法触达这一层

## 提取的概念

- [Orb](entities/Orb.md)（entity，已有条目）

- [Holographic Memory](concepts/Holographic Memory.md)

- [Multi-profile Agent 隔离](concepts/Multi-profile Agent 隔离.md)

- [MCP Permission Relay](concepts/MCP Permission Relay.md)

- [Claude Code](entities/Claude Code.md)（已有条目）

- [FTS5 全文检索](concepts/FTS5 全文检索.md)（已有条目，Orb 的 DocStore 基于 FTS5）

## 原始文章信息

- **作者**：@karry_viber（Karry × Orb 🔮）

- **来源**：X 书签

- **发布时间**：2026-05-02

- **原文链接**：[X 推文](https://x.com/karry_viber/status/2050483217858482374)

- **GitHub**：[KarryViber/Orb](https://github.com/KarryViber/Orb)（58★，MIT，JavaScript）

## 个人评注

- Orb 的「不替代 runtime、只做封装」思路与 OpenClaw 的 harness 哲学高度一致——都是在 Agent 核心能力之外补齐记忆、路由、权限等系统层

- Holographic Memory 的信任评分 + 衰减机制是一种比简单 append-only 更成熟的记忆方案，值得 OpenClaw Dreaming 参考

- MCP Permission Relay 的 HITL 审批流是 Agent 安全的实用范式，Slack 卡片审批体验远优于命令行确认

- Multi-profile 隔离设计适合「一个基础设施服务多个 Agent 角色」的部署场景，对 OpenClaw 的多 Agent 部署有参考价值
