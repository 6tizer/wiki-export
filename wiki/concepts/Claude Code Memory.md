---
title: Claude Code Memory
type: concept
tags:
- 长期记忆
- 上下文管理
- CLI 工具
status: 审核中
confidence: high
last_compiled: '2026-04-26'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/23703fcaad8f40f0b8b03a81cbfa4e88
notion_id: 23703fca-ad8f-40f0-b8b0-3a81cbfa4e88
---

## 定义

Claude Code Memory 是 Anthropic 为 Claude Code 推出的记忆管理功能，通过自动记忆和文档记忆双机制，结合层级化管理和按需读取，解决 AI 在长期开发协作中的记忆持久化问题。

## 核心要点

- 自动记忆：AI 自动捕获对话中的关键偏好和模式

- 文档记忆：用户以纯文本格式主动记录偏好和项目说明

- 按需读取：仅加载核心记忆，避免上下文窗口浪费

- 层级化管理：多层级规则和约定管理，灵活适配不同场景

- 纯文本存储：简化管理同时保持灵活性和可编辑性

## 来源引用

- [摘要：Claude Code Memory 记忆功能](summaries/摘要：Claude Code Memory 记忆功能.md)（字节笔记本，2026-02-27）

- [摘要：Claude Code自动记忆来了！配合老金三层记忆系统全开源](summaries/摘要：Claude Code自动记忆来了！配合老金三层记忆系统全开源.md)（老金带你玩AI, 2026-02-28）— v2.1.59 自动记忆功能实测，[CLAUDE.md](http://claude.md/)（用户指令）与 [MEMORY.md](http://memory.md/)（Claude 笔记）双机制对比，三层 DIY 记忆系统补全知识管理短板

- @gerrox 对 Claude Code 内部架构深度分析（2026-04-01）— 3 层记忆架构支持跨会话持久化，分层管理不同生命周期信息；来源：[https://x.com/gerrox/status/2039137055746543860](https://x.com/gerrox/status/2039137055746543860)

- 《Claude Code 的七层记忆架构：从毫秒级 Token 裁剪到「睡眠整理」系统》｜X书签文章｜原文链接：[https://x.com/troyhua/status/2039052328070734102](https://x.com/troyhua/status/2039052328070734102)｜来源条目：摘要：Claude Code 的七层记忆架构：从毫秒级 Token 裁剪到「睡眠整理」系统

- [摘要：Claude Code 的七层记忆体系：从亚毫秒级缓存到「梦境」式整合](summaries/摘要：Claude Code 的七层记忆体系：从亚毫秒级缓存到「梦境」式整合.md)

- [摘要：Creating a Second Brain with Claude Code](summaries/摘要：Creating a Second Brain with Claude Code.md)

## 关联概念

- [第二大脑系统](concepts/第二大脑系统.md)

- [Claude Code Hooks](concepts/Claude Code Hooks.md)
