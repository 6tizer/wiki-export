---
title: Dreaming 记忆整合
type: concept
tags:
- 记忆系统
- 长期记忆
- 上下文管理
status: 审核中
confidence: high
last_compiled: '2026-04-23'
source_tags: Agent, LLM, 自动化
source_article_url: ''
notion_url: https://www.notion.so/9960607f4ef6432688c1dbae6569f07b
notion_id: 9960607f-4ef6-4326-88c1-dbae6569f07b
---

## 定义

Dreaming 记忆整合是 Claude Code 在后台跨会话整理、合并和剪枝记忆的机制，作用类似人类睡眠阶段对信息的巩固。

## 关键要点

- 不在主对话线程里执行，而是在后台异步完成

- 重点是把碎片化会话笔记整合为更稳定的长期记忆

- 通过锁文件、只读工具限制和分阶段整理降低副作用

## 来源引用

- [摘要：Claude Code 的七层记忆架构：从毫秒级 Token 裁剪到「睡眠整理」系统](summaries/摘要：Claude Code 的七层记忆架构：从毫秒级 Token 裁剪到「睡眠整理」系统.md)（[https://x.com/troyhua/status/2039052328070734102](https://x.com/troyhua/status/2039052328070734102)）
