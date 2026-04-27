---
title: Runtime Skill Injection
type: concept
tags:
- Harness 工程
status: 草稿
confidence: medium
last_compiled: '2026-04-27'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/4ea311ea342f44cfaca2d5a3c60bf7ff
notion_id: 4ea311ea-342f-44cf-aca2-d5a3c60bf7ff
---

## 定义

**Runtime Skill Injection**（运行时技能注入）是一种 Agent 架构模式，允许 Agent 在运行时通过自然语言指令动态加载、升级或替换自身能力模块，而无需重新构建或部署整个系统。

## 关键要点

- 典型用例：用户对 Agent 说「Upgrade GBrain」，Agent 即可自动拉取最新的 Skill 包并热更新

- 这种模式将 Agent 的能力从**编译时硬编码**转向**运行时动态组装**，使 Agent 具备自演化能力

- 与传统的版本化部署相比，Runtime Skill Injection 降低了升级摩擦，但也增加了版本管理、兼容性和依赖追踪的复杂度

- 这是 GBrain + Skillify 体系的核心交互模式之一

## 关联概念

- [Skillify](concepts/Skillify.md)

- [GBrain](entities/GBrain.md)

- [self-improving-agent](concepts/self-improving-agent.md)

## 来源引用

- [摘要：Big drop for GBrain v0.19.](summaries/摘要：Big drop for GBrain v0.19.md)（[原文](https://x.com/garrytan/status/2047504667127799974)）
