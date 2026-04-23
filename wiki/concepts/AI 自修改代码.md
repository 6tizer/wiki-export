---
title: AI 自修改代码
type: concept
tags:
- Coding Agent
- Agent 技能
- 代码生成
status: 已审核
confidence: medium
last_compiled: '2026-04-23'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/8de4a11e53614523b5ffaf51a9400218
notion_id: 8de4a11e-5361-4523-b5ff-af51a9400218
---

## 定义

AI 自修改代码是指 AI Agent 能够读取、理解并修改自身或所在系统源代码的能力，实现自我进化和自动化配置。

## 关键要点

- NanoClaw 中的典型实现：输入 `/add-telegram` 命令后，AI 自动读 Skill 文件、安装依赖、修改源码、配置 bot token

- Karpathy 特别赞赏这一特性

- 与传统的配置文件驱动方式形成对比：代码即配置，AI 既是用户也是开发者

- 创始人观点：DRY 原则在 AI 时代过时——AI 修改共享函数时不会考虑下游连锁反应，适度代码重复反而成为有效的物理隔离

- 引发关于代码寿命的思考：六个月后更强的模型会直接重写系统

## 来源引用

- [摘要：300万人围观，Karpathy怒喷OpenClaw。然后推荐了一个500行的替代品。](summaries/摘要：300万人围观，Karpathy怒喷OpenClaw。然后推荐了一个500行的替代品。.md)
