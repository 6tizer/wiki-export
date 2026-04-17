---
title: Memory Folder
type: concept
tags:
- 记忆系统
status: 审核中
confidence: medium
last_compiled: '2026-04-18'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/7803cb21a81041a3922b23382f577a6e
notion_id: 7803cb21-a810-41a3-922b-23382f577a6e
---

## 定义

Memory Folder 是 Anthropic Harness 工程指南中推荐的一种**记忆持久化模式**，让 Claude 将上下文信息写成文件保存，需要时再读回来，实现跨会话的知识保留。

## 核心机制

- Agent 在工作过程中将重要上下文主动写入外部文件

- 后续需要时按需读取对应文件，而非依赖 context window 中的历史消息

- 本质是将「短期记忆」（context window）溢出的部分转化为「外部长期记忆」（文件系统）

## 要点

- **实测效果显著**：Sonnet 4.5 使用 Memory Folder 后，BrowseComp-Plus 准确率从 60.4% 提升至 67.2%

- 与 Compaction 互补：Compaction 压缩 context 内的历史，Memory Folder 将信息外置到文件

- 设计理念与 Claude Code 的 Auto Memory 一脉相承，但 Memory Folder 更偏向通用化建议

## 来源引用

- 《Claude Code Auto Dream 记忆整理功能深度解析》— 数字生命卡兹克（微信）
