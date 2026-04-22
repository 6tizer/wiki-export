---
title: Nanobot
type: entity
tags:
- Agent 框架
status: 审核中
confidence: high
last_compiled: '2026-04-22'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/83231adbe69f4e6fb3dc222c6d2ee9cb
notion_id: 83231adb-e69f-4e6f-b3dc-222c6d2ee9cb
---

## 定义

Nanobot 是香港大学开源的纳米级 Agent 框架，仅用约 4000 行代码复刻了 OpenClaw 的核心能力，强调极简设计和易部署。

## 核心要点

- 4000 行代码的极简设计

- 复刻 OpenClaw 核心能力

- 支持 9 个通讯渠道：Telegram、Discord、Slack、WhatsApp、Email、飞书、钉钉、MoChat、QQ

- pip install + 配置文件即可部署

- 丰富的工具集：read_file、write_file、exec、web_search、spawn 等

- 作为 ClawWork 的基础架构

## 别名

NanoClaw（不同文章中的叫法差异，实为同一项目）

## 補充要点

- 安装只需 3 行命令：clone → cd → claude

- 无配置文件概念，所有定制通过 Skills 完成

- 通过 Claude Code 处理安装和配置，AI 直接读 Skill、安装依赖、修改源码

- Karpathy 公开推荐，获 300 万+ 浏览

- 创始人 Gavriel Cohen 提出三个颠覆性观点：DRY 原则过时、文件行数限制过时、代码无需经得起时间考验

## 来源引用

- [摘要：ClawWork AI 经济压力测试框架](summaries/摘要：ClawWork AI 经济压力测试框架.md)（开源星探，2026-02-18）

  - GitHub: [https://github.com/HKUDS/nanobot](https://github.com/HKUDS/nanobot)

- [摘要：300万人围观，Karpathy怒喷OpenClaw。然后推荐了一个500行的替代品。](summaries/摘要：300万人围观，Karpathy怒喷OpenClaw。然后推荐了一个500行的替代品。.md)（探索AGI，2026-02-27）

  - GitHub: [https://github.com/qwibitai/nanoclaw](https://github.com/qwibitai/nanoclaw)
