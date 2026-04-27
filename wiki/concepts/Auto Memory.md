---
title: Auto Memory
type: concept
tags:
- 记忆系统
status: 审核中
confidence: high
last_compiled: '2026-04-27'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/f6a14ecd58434e4699b9469eb343f4fd
notion_id: f6a14ecd-5843-4e46-99b9-469eb343f4fd
---

## 定义

Auto Memory 是 Claude Code 的**自动记忆功能**，在对话过程中自动识别并记录重要信息到 [MEMORY.md](http://memory.md/) 文件，无需用户手动触发。

## 核心机制

- 对话过程中自动检测值得记录的信息（用户偏好、项目决策、关键上下文等）

- 将信息写入 [MEMORY.md](http://memory.md/) 及对应子目录（user/、feedback/、project/、reference/）

- 每次新对话启动时自动读取 [MEMORY.md](http://memory.md/) 前 200 行作为上下文

- 记忆按项目隔离，每个项目独立一套记忆文件

## 要点

- 与 Auto Dream 构成「写入-整理」的完整记忆生命周期

- 降低了用户手动维护 [CLAUDE.md](http://claude.md/) 的负担

- 记忆分层：[MEMORY.md](http://memory.md/)（索引）→ user/（个人信息）→ feedback/（纠正与肯定）→ project/（进展与决策）→ reference/（外部资源）

## 来源引用

- [摘要：Claude Code Auto Dream 记忆整理功能深度解析](summaries/摘要：Claude Code Auto Dream 记忆整理功能深度解析.md)

- [摘要：Claude Code Memory 记忆功能](summaries/摘要：Claude Code Memory 记忆功能.md)— 字节笔记本（微信，2026-02-27）：进一步介绍了自动记忆与文档记忆的双机制设计，以及按需读取优化策略

- [摘要：Claude Code自动记忆来了！配合老金三层记忆系统全开源](summaries/摘要：Claude Code自动记忆来了！配合老金三层记忆系统全开源.md) — 已知问题：Token 消耗增加（18分钟消耗 8% 配额）、记忆是影子状态（~/.claude/projects/ 不可 Git 追踪）、[MEMORY.md](http://memory.md/) 重复加载 Bug

- [摘要：Claude Code Handoff：让 AI 编程助手跨 Session 无缝接力](summaries/摘要：Claude Code Handoff：让 AI 编程助手跨 Session 无缝接力.md)

## 关联概念

- [Claude Code Handoff](concepts/Claude Code Handoff.md)

- [Handoff 文档](concepts/Handoff 文档.md)
