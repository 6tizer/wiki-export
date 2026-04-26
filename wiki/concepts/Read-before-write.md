---
title: Read-before-write
type: concept
tags:
- Agent 安全
- 上下文管理
status: 草稿
confidence: medium
last_compiled: '2026-04-12'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/fb5d1ada172f4531b7e7d82e4f032f18
notion_id: fb5d1ada-172f-4531-b7e7-d82e4f032f18
---

## 定义

Read-before-write 是 coding agent 在写入文件前先读取当前内容的一种安全编辑策略，用于减少误覆盖和上下文偏差。

## 关键要点

- 先理解现状，再生成修改动作

- 常与 diff patch、LSP 诊断和增量编辑一起出现

- 对多文件工程环境尤其重要，可降低破坏性写入风险

## 来源引用

- 《OmniCoder-9B：把顶级 AI 的编程思路蒸馏进一张消费级显卡》｜X书签文章｜原文链接：[https://x.com/geekbb/status/2036777857494741066](https://x.com/geekbb/status/2036777857494741066)
