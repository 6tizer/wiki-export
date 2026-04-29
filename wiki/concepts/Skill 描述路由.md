---
title: Skill 描述路由
type: concept
tags:
- 代码生成
- Harness 工程
status: 草稿
confidence: medium
last_compiled: '2026-04-29'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/57242d8bab4b4b2ca6bf5292c7954612
notion_id: 57242d8b-ab4b-4b2c-a6bf-5292c7954612
---

### 定义

Skill 描述路由是指在 Coding Agent（如 Claude Code）的 Skill 系统中，通过 description 字段的写法来决定 AI 主线程何时触发该 Skill 的机制。核心区别在于「功能介绍型」描述（如"用于 X workflow"）与「触发条件型」描述（如"Use when … / NOT when …"）对 Skill 调用率的影响。

### 关键要点

- **功能介绍型描述失效**：写成"用于 X / X workflow"的 description，AI 主线程无法判断在何种场景下调用该 Skill，导致大量 Skill 实际上从未被触发

- **触发条件型描述有效**：改为"Use when + NOT when"格式后，AI 可以明确知道在什么条件下应该调用、什么条件下不应该调用

- **实证数据**：一个拥有 52 个 Skill 的项目（codeburn），subagent 调用率仅 0.18%，80.8% 的 Skill 处于「装废」状态，主要原因就是 description 写法不当

- **修复方法**：将所有 Skill 的 description 改为明确的 Use when / NOT when 格式

### 来源引用

- [摘要：今天才发现自己 80.8% 的 Claude Code skill 是装废的。](summaries/摘要：今天才发现自己 80.8% 的 Claude Code skill 是装废的。.md)（[原文](https://x.com/runes_leo/status/2049513537966674317)）
