---
title: OpenClaw 九层 System Prompt 架构
type: concept
tags:
- OpenClaw
- 上下文管理
- 提示工程
status: 审核中
confidence: high
last_compiled: '2026-04-28'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/68d73fe2a3554c1682d1d8d60c18e9db
notion_id: 68d73fe2-a355-4c16-82d1-d8d60c18e9db
---

## 定义

OpenClaw 九层 System Prompt 架构是 OpenClaw 在每轮运行时动态组装系统提示的分层设计，把框架层、用户层和当前输入清晰拆分。

## 关键要点

- 底层负责身份、工具、技能、运行时状态等稳定上下文

- 用户主要通过工作区文件和启动钩子定制个性与流程

- 本质是把 Agent 的稳定性与个性化分层管理

## 来源引用

- [摘要：OpenClaw 的 9 层 System Prompt 架构：框架管稳定，你管个性化](summaries/摘要：OpenClaw 的 9 层 System Prompt 架构：框架管稳定，你管个性化.md)（@yanhua1010，2026-04-01）— 系统拆解了 L1-L9 的职责分层

## 关联概念

- [OpenClaw](entities/OpenClaw.md)

- [SOUL.md](concepts/SOUL.md.md)
