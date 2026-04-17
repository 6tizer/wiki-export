---
title: Ratchet-Driven Development
type: concept
tags:
- Coding Agent
- 工作流
status: 草稿
confidence: medium
last_compiled: '2026-04-15'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/f6db11e31c2d4dd5967e10de0555ce7a
notion_id: f6db11e3-1c2d-4dd5-967e-10de0555ce7a
---

## 定义

Ratchet-Driven Development（RDD）是一种面向 AI 编程与 Agent 开发的工作方法：把项目状态压缩为少量外部上下文文件，并用完整测试套件作为“棘轮”持续约束回归。

## 关键要点

- 每个迭代尽量在新的对话上下文中推进，避免长上下文反复膨胀

- 通过 `project.md`、`tests.md` 等轻量文件把项目状态外置化

- 每轮都重新运行测试，把验证结果当作不可逆的质量护栏

- 核心价值是在降低 token 成本的同时保持稳定迭代与低回归风险

## 来源引用

- [原文链接](https://x.com/claudeai/status/2042308622181339453)｜《Claude 推出 Advisor Strategy》｜源文章：Claude Advisor Strategy：用 Sonnet 的钱，买 Opus 的脑子

## 关联概念

- [Advisor Strategy](concepts/Advisor Strategy.md)

- [Advisor Tool](concepts/Advisor Tool.md)

- [Harness Engineering](concepts/Harness Engineering.md)

- [Hermes Agent](entities/Hermes Agent.md)
