---
title: Auto Dream
type: concept
tags:
- 记忆系统
status: 审核中
confidence: high
last_compiled: '2026-04-18'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/fe736f3f702542d1b8ce367dbf4f3144
notion_id: fe736f3f-7025-42d1-b8ce-367dbf4f3144
---

## 定义

Auto Dream（也常写作 autoDream）是 Claude Code 新增的**后台记忆整理功能**，灵感来自人类睡眠时的记忆巩固机制。它在用户不使用 Claude Code 时自动运行，对积累的记忆文件进行清理和优化。

## 核心机制

Auto Dream 的工作流程分为四个步骤：

1. **扫描现有记忆**：读取所有记忆文件

1. **识别问题**：找出过时、矛盾、重复的内容

1. **优化整理**：合并重复条目、删除过时信息、解决矛盾

1. **写回文件**：更新 [MEMORY.md](http://memory.md/) 和相关记忆文件

## 要点

- 与 Auto Memory（自动记录）互补：Auto Memory 负责「写入」，Auto Dream 负责「整理」

- 解决的核心问题是**记忆技术债**——旧决策矛盾、相对日期过时、已完结项目残留

- 记忆文件有上限约束（200 行 / 25KB），Auto Dream 确保在限额内保留最有价值的信息

- 该循环模式（扫描→识别→优化→写回）可抽象为通用的知识维护范式

- 适合个人助理型 Agent 的跨会话记忆维护，可在空闲时主动整理长期记忆

## 来源引用

- [摘要：Claude Code Auto Dream 记忆整理功能深度解析](summaries/摘要：Claude Code Auto Dream 记忆整理功能深度解析.md)（数字生命卡兹克，微信）

- 《OpenClaw 提速指南：一个加密交易员写出的 AI Agent 优化手册》（QingQ77，X书签，2026-03-17）— 将 autoDream 作为记忆碎片定期整编机制，补充长期运行中的维护价值。

- 《OpenClaw 提速指南：一个加密交易员写出的 AI Agent 优化手册》— X书签，2026-03-17：将自动整理机制视为控制记忆技术债的关键手段

- 《Claudebot-vibe：一个越用越聪明的 Claude Telegram 私人助理》｜X书签文章｜来源页：[摘要：Claudebot-vibe：一个越用越聪明的 Claude Telegram 私人助理](summaries/摘要：Claudebot-vibe：一个越用越聪明的 Claude Telegram 私人助理.md)
