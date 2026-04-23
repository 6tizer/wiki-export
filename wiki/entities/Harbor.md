---
title: Harbor
type: entity
tags:
- Coding Agent
- 开发工具
status: 审核中
confidence: medium
last_compiled: '2026-04-16'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/895ea8c78f3c4a858638e8f9edd9741c
notion_id: 895ea8c7-8f3c-4a85-8638-e8f9edd9741c
---

## 定义

Harbor 是一个用于组织 Agent 任务、环境与验证脚本的 benchmark / task 框架，EvoForge 通过兼容 Harbor 的任务格式来运行和评估实验。

## 关键要点

- 用 `task.toml`、`instruction.md`、tests、environment 等结构描述任务

- 验证结果会写出分数，便于 meta-agent 持续 hill-climb

- 让同一套 harness 可以在不同任务集上复用与比较

## 关联概念

- [Terminal Bench 2](entities/Terminal Bench 2.md)

- [Harness Engineering](concepts/Harness Engineering.md)

## 来源引用

- [原文链接](https://x.com/leonardtang_/status/2044426476632629545)｜《EvoForge: Scaling Evolutionary Harness Optimization》｜X书签文章
