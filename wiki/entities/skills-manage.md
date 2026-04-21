---
title: skills-manage
type: entity
tags:
- Coding Agent
- Agent 技能
status: 草稿
confidence: medium
last_compiled: '2026-04-21'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/d1082bb71fe544869be84679ae78470d
notion_id: d1082bb7-1fe5-4486-9be8-4679ae78470d
---

## 定义

skills-manage 是一个面向多平台 AI Coding Agent 的 Skill 管理桌面应用，用中心目录统一维护 Skill，再通过安装和分发机制同步到不同平台。

## 关键要点

- 以 `~/.agents/skills/` 作为中心 Skill 目录，强调一处维护、多端复用。

- 支持 Claude Code、Cursor、Gemini CLI、Codex、OpenClaw、Hermes 等多种平台。

- 提供仓库导入、市场浏览、Markdown 预览、AI 解释、集合管理等能力，说明它不只是同步脚本，而是在做 Skill 管理层产品化。

- 用符号链接而非文件复制来安装 Skill，减少项目目录污染。

## 来源引用

- [摘要：统一编排 Skill，按项目精准分发到不同 Agent CLI。](summaries/摘要：统一编排 Skill，按项目精准分发到不同 Agent CLI。.md)（[原文](https://x.com/iamzhihui/status/2046063506609635552)）

## 关联概念

- Agent Skills

- 符号链接注入

- 项目级 Skills 分发

- SkillStar
