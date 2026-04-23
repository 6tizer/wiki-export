---
title: Obsidian Skills
type: concept
tags:
- Agent 技能
- 知识管理
- 笔记工具
status: 审核中
confidence: high
last_compiled: '2026-04-23'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/6b071241e7084429951aa919b164490e
notion_id: 6b071241-e708-4429-951a-a919b164490e
---

## 定义

Obsidian Skills 是 Obsidian CEO Kepano 开源的一组 Agent Skills，让 AI 编码助手（如 Claude Code）深度理解 Obsidian 的特有语法和功能，实现对 Obsidian 知识库的精准读写操作。

## 关键要点

- 三大核心 Skill：obsidian-markdown（622 行 Wikilink/Callout/Frontmatter 等语法指南）、obsidian-bases（620 行数据库视图操作）、json-canvas（644 行画布规范）

- 三层加载机制：元数据层（始终加载）→ 指令层（按需加载）→ 资源层（执行时加载），高效利用上下文窗口

- 解决通用 AI 不识别 `[[Wikilink]]`、`![[embed]]`、`> [!callout]` 等 Obsidian 特有语法的核心痛点

- 与 obsidian-cli 配合使用可安全操作文件而不破坏双向链接

- GitHub: kepano/obsidian-skills

## 来源引用

- [摘要：Obsidian Skills 如何重塑知识工作流](summaries/摘要：Obsidian Skills 如何重塑知识工作流.md)（Draco正在VibeCoding，2026-01-19）

- [摘要：用OpenClaw+Obsidian搭建内容工厂](summaries/摘要：用OpenClaw+Obsidian搭建内容工厂.md)（饼干哥哥AGI，2026-03-01）

- [摘要：Obsidian-agent-client 插件——多 AI Agent 无缝切换](summaries/摘要：Obsidian-agent-client 插件——多 AI Agent 无缝切换.md)（哒啦猫，2026-02-08）

- [摘要：OpenClaw + Obsidian：用 AI 智能体打造 7×24 小时内容工厂](summaries/摘要：OpenClaw + Obsidian：用 AI 智能体打造 7×24 小时内容工厂.md)（bggg_ai，2026-03-06）

## 关联概念

- [obsidian-cli](concepts/obsidian-cli.md)

- [内容工厂工作流](concepts/内容工厂工作流.md)

- [OpenClaw](entities/OpenClaw.md)
