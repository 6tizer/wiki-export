---
title: Skill 蒸馏
type: concept
tags:
- Agent 技能
- 工作流
status: 审核中
confidence: high
last_compiled: '2026-04-11'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/836620467a4947e091430656311f2e53
notion_id: 83662046-7a49-47e0-9143-0656311f2e53
---

## 定义

Skill 蒸馏（也常写作 Agent Skill蒸馏，Skill Distillation）是一种将已有工具或系统的设计原则和最佳实践提炼为可安装 Agent Skill 的工程方法。通过分析源码或运行行为，提取核心设计模式，打包为标准化 Skill。

## 典型流程

1. **源码/行为分析**：阅读目标工具的源码或观察其运行模式

1. **多 Agent 协作蒸馏**：一个 Agent 负责审查/分析，另一个负责执行和提炼

1. **注入个人偏好**：确保提取的实践符合实际使用需求（非纯自动化）

1. **打包为 Skill**：将提炼出的原则封装为可安装的 OpenClaw Skill

## 实践案例

- **Claude Code 源码 → Agent Skill**（DevAI）：从51万行源码提炼六大设计原则

- **歸藏的 Skills 系列**：对特定任务（视频处理、文档配图等）的最佳实践蒸馏

## 关键价值

- 将专家知识编码为可复用的自动化单元

- 跨越"看懂"和"用上"之间的鸿沟

- 适合沉淀个人或团队可复用的 AI 工具库

- 与 Harness Engineering 配套：蒸馏出 Skill，用 Harness 编排执行

## 来源引用

- 来源条目：摘要：把 Claude Code 源码蒸馏成 Agent Skill — Harness Engineering 实践

- 来源条目：[摘要：万物皆可蒸馏：一场从同事到自己的 Claude Skill 狂潮](summaries/摘要：万物皆可蒸馏：一场从同事到自己的 Claude Skill 狂潮.md)

- 来源条目：[摘要：女娲.skill：让乔布斯、芒格、费曼在 Claude Code 里给你打工](summaries/摘要：女娲.skill：让乔布斯、芒格、费曼在 Claude Code 里给你打工.md)
