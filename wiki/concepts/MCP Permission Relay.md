---
title: MCP Permission Relay
type: concept
tags:
- MCP 协议
- Agent 安全
status: 草稿
confidence: medium
last_compiled: '2026-05-03'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/61394295f5434ae6bf13dce54b467a9c
notion_id: 61394295-f543-4ae6-bf13-dce54b467a9c
---

## 定义

MCP Permission Relay 是一种将 Claude Code 的权限审批请求通过 MCP tool server 转发到消息平台（如 Slack）的架构模式，使人类审批者能够在聊天界面中实时批准或拒绝 Agent 的敏感操作。

## 关键要点

- Worker 进程为 Claude Code 创建临时 MCP 配置，通过 `--permission-prompt-tool` 启动

- `mcp-permission-server.js` 通过 Unix socket 将审批请求转发给 scheduler

- Scheduler 可自动放行（auto-allow）或通过 adapter 发送审批卡片到消息平台

- Slack 是目前实现的交互式审批路径，其他平台可通过 PlatformAdapter 接口扩展

- Orb 还会按需为 profile 生成保守的默认允许列表（`settings.json`），覆盖常见只读和检查命令

## 设计优势

- 人在回路（HITL）：敏感操作必须经人类审批，平衡自主性和安全性

- 平台无关：审批逻辑与具体消息平台解耦，adapter 层隔离传输和格式化

## 来源引用

- [摘要：Orb 自建记忆与路由的 Claude Code 封装框架](summaries/摘要：Orb 自建记忆与路由的 Claude Code 封装框架.md)（[原文](https://x.com/karry_viber/status/2050483217858482374)）

## 关联概念

- [Orb](entities/Orb.md)

- [Claude Code](entities/Claude Code.md)

- [Multi-profile Agent 隔离](concepts/Multi-profile Agent 隔离.md)
