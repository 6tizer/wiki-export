---
title: Read-before-write
type: concept
tags:
- Agent 安全
- 上下文管理
status: 审核中
confidence: medium
last_compiled: '2026-04-28'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/fb5d1ada172f4531b7e7d82e4f032f18
notion_id: fb5d1ada-172f-4531-b7e7-d82e4f032f18
---

## 定义

Read-before-write 是 coding agent 在写入文件前先读取当前内容的一种安全编辑策略，用于减少误覆盖和上下文偏差。

## 关键要点

- 先理解现状，再生成修改动作

- 常与 diff patch、LSP 诊断和增量编辑一起出现

- 对多文件工程环境尤其重要，可降低破坏性写入风险

## 来源引用

- [摘要：I tested the same prompt on both Grok 4.3 and GPT 5.5](summaries/摘要：I tested the same prompt on both Grok 4.3 and GPT 5.5.md)（[原文](https://x.com/geekbb/status/2036777857494741066)，2026-04-10）
