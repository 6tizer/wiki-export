---
title: 摘要：微信不止能接 OpenClaw，我把 Claude Code、Codex、Opencode 等 AI IDE 也接进来了
type: summary
tags:
- OpenClaw
- 开发工具
status: 已审核
confidence: high
last_compiled: '2026-04-11'
source_tags: 微信生态, OpenClaw, Claude Code
source_article_url: ''
notion_url: https://www.notion.so/c494f579449a42d9ba10bcbcadc1c766
notion_id: c494f579-449a-42d9-ba10-bcbcadc1c766
---

## 一句话摘要

作者在 ClawBot 之上增加路由层，通过 agentapi 项目将 Claude Code、Codex、Opencode、GitHub Copilot 等多个 AI IDE 全部接入微信，实现微信作为多 Agent 统一入口。

## 关键洞察

- **架构演进**：`微信 → ClawBot → OpenClaw` 升级为 `微信 → ClawBot/接入层 → Router/路由层 → 任意Agent`

- **agentapi 是关键**：将原本面向终端交互的 CLI 工具包装成可调用的 HTTP 服务接口，屏蔽不同工具的交互差异

- **已接入6个工具**：Claude Code、Codex、Opencode、GitHub Copilot、Auggie、Cursor CLI

- **子命令切换后端**：发送 `/claude`、`/codex`、`/opencode` 等命令即可切换当前会话的 Agent 后端

- **多 Agent 统一入口的可行性已验证**：虽然仍是中间态，但方向已成立

## 提取的概念

- iLink 协议

- agentapi

- Multi-Agent 路由

## 原始文章信息

- **作者**: 拓扑笔记

- **来源**: 微信公众号

- **发布时间**: 2026-03-22

- **开源**: [https://github.com/BytePioneer-AI/weixin-agent-gateway](https://github.com/BytePioneer-AI/weixin-agent-gateway)

## 个人评注

OpenClaw 多 Agent 场景的重要参考——agentapi 提供了一种标准化方式将任何 CLI Agent 接入统一入口，与 HITL 工作流结合有价值。
