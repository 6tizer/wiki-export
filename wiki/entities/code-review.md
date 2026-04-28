---
title: code-review
type: entity
tags:
- Coding Agent
- Agent 技能
status: 审核中
confidence: medium
last_compiled: '2026-04-20'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/20c7ab65585e41c69d3f37dadf3764d1
notion_id: 20c7ab65-585e-41c6-9d3f-37dadf3764d1
---

## 定义

code-review 是 Anthropic 放在 Claude Code 仓库 plugins/ 目录中的官方插件，用来把拉取请求审查拆给多个 Agent 并行完成，并将结果整理成可直接落到 PR 流程里的审查反馈。

## 关键要点

- 可并行启动多个 Agent 审查同一个 PR，提高问题覆盖率

- 重点检查编码规范、潜在 bug 与低价值改动，减少人工初筛成本

- 支持将整理后的审查结果直接回写到 PR 评论区，适合接入日常代码审查流水线

## 关联概念

- [Claude Code](entities/Claude Code.md)

- [Claude Code Hooks](concepts/Claude Code Hooks.md)

## 来源引用

- [摘要：用了这么久 Claude Code，很多人都在研究 CLAUDE.md、Hooks、Sub-Agent，但其实它 GitHub 仓库里还藏着一批官方插件，很多人根本没注意到。](summaries/摘要：用了这么久 Claude Code，很多人都在研究 CLAUDE.md、Hooks、Sub-Agent，但其实它 GitHub 仓库里还藏着一批官方插件，很多人根本没注意到。.md)（[原文](https://x.com/sitinme/status/2045127135195439279)）
