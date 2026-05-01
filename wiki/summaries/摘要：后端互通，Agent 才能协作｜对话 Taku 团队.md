---
title: 摘要：后端互通，Agent 才能协作｜对话 Taku 团队
type: summary
tags:
- Harness 工程
- 多Agent协作
- Agent 协作模式
status: 已审核
confidence: medium
last_compiled: '2026-04-11'
source_tags: Agent, Multi-Agent, 行业观察
source_article_url: ''
notion_url: https://www.notion.so/Tizer/597cf860797e419f94e4f2c9d5f0feb8
notion_id: 597cf860-797e-419f-94e4-f2c9d5f0feb8
---

## 一句话摘要

Taku 是一个早期产品，通过三层 Harness 架构（Runtime、统一后端协议、跨应用记忆共享）让不同 Agent 和工具的后端互通，解决「生成容易，协作难」的核心问题。

## 关键洞察

- **三层 Harness 架构**：第一层 Runtime（生成即可运行）、第二层统一后端通讯协议（任意工具互调）、第三层跨应用 context 和记忆共享

- **开发者 vs 普通人的需求反转**：Claude Code 默认项目隔离（对开发者合理），但普通人想要的恰恰是默认打通

- **代码原子化分发**：技能可以被原子化提取、分发、按次付费，稀缺的是知识而非代码

- **跨应用记忆自动同步**：在 A 应用积累的数据和上下文，会自动更新相关联的 B 应用

- **创始人 Austin 背景**：连续创业者，前 Sapient Intelligence 联合创始人（$22M 种子轮），当前项目尚未融资

## 提取的概念

- Taku

- Agent Harness（已有相关概念）

- 跨应用记忆共享

## 原始文章信息

- **作者**: 赛博禅心

- **来源**: 微信公众号

- **发布时间**: 2026-03-22

## 个人评注

Taku 的三层架构思路与 Tizer 面临的 OpenClaw 跨项目记忆问题高度相关。跨应用 context 共享是当前痛点，值得跟踪 Taku 的进展。
