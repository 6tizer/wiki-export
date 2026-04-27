---
title: openclaw-managed-agents
type: entity
tags:
- Harness 工程
- 多Agent协作
status: 草稿
confidence: medium
last_compiled: '2026-04-28'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/1b388057395e4b2a9a27ace1556aa531
notion_id: 1b388057-395e-4b2a-9a27-ace1556aa531
---

## 定义

openclaw-managed-agents 是由 @stainlu 开发的开源自托管 Agent 平台，定位为 OpenAI Workspace Agents 的开源替代方案。支持任意大模型后端（Claude、GPT、Gemini、Kimi、DeepSeek 等），提供会话级 Docker 沙箱隔离、终端用户凭证隔离和子 Agent 全链路可观测能力。

别名：openclaw managed agents、Stain Lu managed agents

## 关键要点

- **模型无关**：不锁定单一 LLM 供应商，可随时切换后端模型

- **自托管**：可部署在自有服务器上，最低成本 €4/月

- **会话级 Docker 沙箱**：每个会话运行在独立容器中，一个崩溃不影响其他

- **凭证隔离**：每个终端用户的认证信息互相隔离，适合多租户 SaaS 场景

- **子 Agent 可观测性**：子 Agent 调用全程可追踪，非黑盒执行，采用了 Pi Pattern

- **适配器内置**：自带 Telegram 适配器，可快速搭建 Telegram/Discord AI 机器人

- 仓库地址：[https://github.com/stainlu/openclaw-managed-agents](https://github.com/stainlu/openclaw-managed-agents)

## 典型使用场景

- 企业内部搭建模型可替换的 AI Agent 服务

- SaaS 产品集成 AI 助手（用户账号隔离）

- Telegram / Discord AI 机器人

- 企业受控 Agent（限制 API 访问范围，不能随意出公网）

## 来源引用

- [摘要：OpenAI 刚发的 Workspace Agent，开源版来了](summaries/摘要：OpenAI 刚发的 Workspace Agent，开源版来了.md)（[原文](https://x.com/xiaohu/status/2047521587122106376)）

## 关联概念

- [Workspace Agents](entities/Workspace Agents.md)

- [Agent 可观测性](concepts/Agent 可观测性.md)
