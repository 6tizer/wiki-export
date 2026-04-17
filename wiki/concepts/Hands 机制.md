---
title: Hands 机制
type: concept
tags:
- Agent 编排
status: 审核中
confidence: high
last_compiled: '2026-04-18'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/571af514a19e4f3dbaeebe3760f76a7c
notion_id: 571af514-a19e-4f3d-baee-be3760f76a7c
---

## 定义

Hands 是 OpenFang Agent OS 中的核心概念，代表可自主运行的工作单元，Agent 按预设计划主动执行任务并持续生成结果。

## 关键要点

- 传统 Agent 是被动模式（等输入 → 执行 → 返回 → 等待），Hands 是主动模式（设参数 → 按计划跑 → 持续生成结果 → 汇报）

- 每个 Hand 打包内容：HAND.toml（元配置）、系统 Prompt（多阶段操作手册）、[SKILL.md](http://skill.md/)（领域知识）、可配置参数、仪表盘指标追踪

- 所有内容在编译时打进二进制文件，不依赖外部文件

- 预装 7 个 Hands，如 Research Hand 可每天自动搜索某领域最新动态并整理报告

- 设计哲学：Agent 的安全性必须在设计层面构建，因为自主运行时没有人工 last check

## 来源引用

- 《一个 Rust 写的 Agent OS》（老码小张，2026-02-28）
