---
title: cc-harness
type: entity
tags:
- OpenClaw
status: 草稿
confidence: medium
last_compiled: '2026-04-11'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/921cb1bf712a48b9b2a2f13f952d54dc
notion_id: 921cb1bf-712a-48b9-b2a2-f13f952d54dc
---

## 定义

cc-harness 是卡尔的AI沃兹开源的跨平台 Skill 集，将 Claude Code 泳露源码中最有价值的六种模式提炼为可在 Claude Code、Codex、OpenClaw、OpenCode 等多平台使用的 Skill。

GitHub: [https://github.com/LearnPrompt/cc-harness-skills](https://github.com/LearnPrompt/cc-harness-skills)

## 6 个 Skills

1. **CC Dream Memory**：当对话和记忆文件越堆越乱时，把最近会话、日志和旧记忆合并整理成一份短小稳定的长期记忆

1. **CC Memory Extractor**：每转协作结束后，从最近对话里提取用户偏好、反馈、项目约束

1. **CC Context Compressor**：切上下文或交给别的 Agent 时，把当前进展压成5 段式结构化摘要

1. **CC Verification Gate**：任务看起来已完成时，拉一次只读验证视角专门检查是否真的完成

1. **CC Swarm Coordinator**：任务太大跨文件时，拆成 research/synthesis/implementation/verification 四段分工

1. **CC Kairos Lite**：定义轻量主动任务，小范围、慢节奏的定时巡检

## 来源引用

- [摘要：我把ClaudeCode源码里学到的都做Skill！（cc-harness）](summaries/摘要：我把ClaudeCode源码里学到的都做Skill！（cc-harness）.md)
