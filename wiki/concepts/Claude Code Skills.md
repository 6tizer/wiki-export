---
title: Claude Code Skills
type: concept
tags:
- Coding Agent
- Agent 技能
status: 草稿
confidence: high
last_compiled: '2026-04-16'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/991bbc8488a74c6580c90dd1433be967
notion_id: 991bbc84-88a7-4c65-80c9-0dd1433be967
---

### 定义

Claude Code Skills 指 Claude Code 中可复用的技能扩展机制，通常以独立目录分发，并通过 `SKILL.md`、依赖文件和安装命令接入到本地工作流中。

### 关键要点

- 支持通过仓库直接安装技能，例如 `npx skills add <repo>`

- 适合把特定能力封装成可复用的工作流模块

- 让 Coding Agent 能以更低成本获得稳定、可迁移的能力扩展

### 在本文中的体现

- Logo Generator 以 Skill 形式分发

- 安装目录示例为 `~/.claude/skills/`

- 技能目录通常包含 `SKILL.md` 与 `README.md`

### 来源引用

- 文章标题：Logo Generator

- 文章链接：[https://x.com/Lonely__MH/status/2044652473395376229](https://x.com/Lonely__MH/status/2044652473395376229)

- 源页面：Logo Generator Skill：用 Gemini 一键生成 SVG Logo 和专业展示图

- GitHub：[https://github.com/op7418/logo-generator-skill](https://github.com/op7418/logo-generator-skill)

- [摘要：Claude Code Skills 会悄悄失效：一个被忽视的上下文截断问题](summaries/摘要：Claude Code Skills 会悄悄失效：一个被忽视的上下文截断问题.md)（[原文](https://x.com/garrytan/status/2046981289031667961)）
