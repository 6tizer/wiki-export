---
title: Scout
type: entity
tags:
- 知识管理
- 上下文管理
- AI 产品
status: 草稿
confidence: high
last_compiled: '2026-04-29'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/15476002c6b1498c889e4bfe578eaa92
notion_id: 15476002-c6b1-498c-889e-4bfe578eaa92
---

## 定义

Scout 是由 Agno 开发的开源 Context Agent（上下文代理），定位为「公司大脑」。它通过 Navigation over Search 模式和 Context Providers 架构，实时导航 Slack、Google Drive、Linear 等信息源，按需组装上下文，而非将所有数据灌入向量数据库。Scout 还能自动构建知识 Wiki 和 CRM，形成闭环学习系统。

**别名**：open-source company brain

## 关键要点

- 采用 Context Providers 架构，每个信息源封装为 query/update 两个工具，主 Agent 不直接暴露底层工具细节

- 使用 Navigation over Search 模式，像编码 Agent 遍历文件系统一样遍历信息源，保持实时状态

- 内置 CRM（scout_contacts、scout_projects、scout_notes、scout_followups）和知识 Wiki，自动学习并结构化公司知识

- 支持 Schema on Demand：LLM 可按需创建新数据表（如 scout_coffee_orders）

- 基于 Agno AgentOS 运行，支持 Docker 部署、多用户会话、定时任务

- 可集成 Slack，每个 Slack thread 成为独立 session

## 档案信息

- **GitHub**: [https://github.com/agno-agi/scout](https://github.com/agno-agi/scout)

- **开发者**: Ashpreet Bedi (@ashpreetbedi)

- **运行平台**: Agno AgentOS ([os.agno.com](http://os.agno.com/))

- **部署方式**: Docker

- **开源协议**: 待确认

## 来源引用

- [摘要：Meet Scout. The open-source company brain](summaries/摘要：Meet Scout. The open-source company brain.md)（[原文](https://x.com/ashpreetbedi/status/2049180168200106150)）
