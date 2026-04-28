---
title: security-guidance
type: entity
tags:
- Coding Agent
- 安全/隐私
status: 审核中
confidence: medium
last_compiled: '2026-04-20'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/b4455c6e6f3e4d5bb9d673081be7bc47
notion_id: b4455c6e-6f3e-4d5b-b9d6-73081be7bc47
---

## 定义

security-guidance 是 Claude Code 官方插件中的安全护栏工具，负责在后台监控命令与文件操作，帮助减少提示注入、危险调用与高风险改动带来的工程风险。

## 关键要点

- 面向命令执行与文件修改场景提供持续性安全检查

- 可作为 AI 编程流程中的默认护栏，降低高危操作误触发概率

- 体现了 Claude Code 从“能写代码”走向“能安全执行”的工程化方向

## 关联概念

- [Claude Code](entities/Claude Code.md)

- [Claude Code Hooks](concepts/Claude Code Hooks.md)

## 来源引用

- [摘要：用了这么久 Claude Code，很多人都在研究 CLAUDE.md、Hooks、Sub-Agent，但其实它 GitHub 仓库里还藏着一批官方插件，很多人根本没注意到。](summaries/摘要：用了这么久 Claude Code，很多人都在研究 CLAUDE.md、Hooks、Sub-Agent，但其实它 GitHub 仓库里还藏着一批官方插件，很多人根本没注意到。.md)（[原文](https://x.com/sitinme/status/2045127135195439279)）
