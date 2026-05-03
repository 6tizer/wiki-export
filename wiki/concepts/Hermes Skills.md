---
title: Hermes Skills
type: concept
tags:
- Harness 工程
- AI 产品
status: 草稿
confidence: medium
last_compiled: '2026-05-03'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/1c53477c9312409081e71ef3a210dfdf
notion_id: 1c53477c-9312-4090-81e7-1ef3a210dfdf
---

## 定义

Hermes Skills 是 Hermes Agent 的模块化技能系统，将可复用的工作流封装为斜杠命令（slash commands）。用户输入 `/` 即可调用预置或自定义技能，实现从架构图生成、测试驱动开发到跨平台内容发布等多种任务的一键执行。

## 关键要点

- Hermes Agent 内置 100+ 预置技能，覆盖代码、设计、研究、消息平台等场景

- 每个技能都是一个斜杠命令，支持 Tab 自动补全

- 用户可编写自定义技能，永久绑定到所有会话和平台

- 典型技能示例：`/architecture-diagram`（SVG 架构图）、`/excalidraw`（手绘图）、`/manim-video`（3Blue1Brown 风格动画）、`/test-driven-development`（强制 RED-GREEN-REFACTOR）、`/systematic-debugging`（四阶段根因分析）

- 自定义技能可跨平台（CLI、Telegram、Discord 等）一致调用

## 与其他概念的关系

- 是 Hermes Agent 区别于普通聊天机器人的核心架构特征之一

- 与 MCP 协议的工具注册模式互补：MCP 侧重外部工具集成，Skills 侧重内置工作流封装

- 自定义 Skill 本质上是 prompt + 工具调用链的声明式配置

## 来源引用

- [摘要：15 Hermes Agent features you've never touched](summaries/摘要：15 Hermes Agent features you've never touched.md)（[原文](https://x.com/sharbel/status/2049158152709382177)）

- [摘要：Architecture-diagram is one of my favorite @NousResearch Hermes agent skills, NGL!](summaries/摘要：Architecture-diagram is one of my favorite @NousResearch Hermes agent skills, NGL!.md)（[原文](https://x.com/mr_r0b0t/status/2049821753195585740)）

- [摘要：Shopify 官方为 Hermes Agent 构建电商运营 Skill](summaries/摘要：Shopify 官方为 Hermes Agent 构建电商运营 Skill.md)（[原文](https://x.com/NousResearch/status/2050336291586187711)）

## 关联概念

- [Hermes Agent](entities/Hermes Agent.md)

- [Shopify AI Toolkit](entities/Shopify AI Toolkit.md)

- [Agentic Commerce](concepts/Agentic Commerce.md)
