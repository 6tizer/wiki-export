---
title: social-media-skills
type: entity
tags:
- 内容自动化
- 提示工程
status: 草稿
confidence: medium
last_compiled: '2026-04-28'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/0a492a13515f447c96235d5f8f98e972
notion_id: 0a492a13-515f-447c-9623-5d5f8f98e972
---

## 定义

social-media-skills 是 Charlie Hills 开源的 Claude Skills 库，包含 17 个模块化社交媒体技能，覆盖 LinkedIn、Instagram、Substack、X、YouTube 等平台的内容创作全流程。

别名：Social Media Skills for AI Agents

## 档案

- **作者**：Charlie Hills（@charliejhills）

- **GitHub**：[charlie947/social-media-skills](https://github.com/charlie947/social-media-skills)

- **Stars**：300+

- **语言**：Shell

- **协议**：MIT

- **创建时间**：2026-04-22

## 关键要点

- 所有技能以 Markdown 文件形式分发，安装到 `~/.claude/skills/` 即可使用

- 核心架构：`voice-builder` 作为基础技能，生成 `about-me.md` 和 `voice.md`，其余 16 个技能都会读取这两个文件以保持语调一致

- 技能分为六大类：语音基础（voice-builder、newsletter-voice）、LinkedIn（profile-optimizer、post-writer、post-scorer 等）、内容规划（content-matrix、niche-research）、图形设计（graphic-designer、gemini-infographic、gemini-carousel）、视频（reels-scripting、youtube-thumbnail）、社群（pinned-comment、quote-post）

- 部分技能依赖 Apify（post-scorer、reels-scripting）和 Gemini API（视频分析）

- 支持多种安装方式：Claude Code plugin marketplace、git clone、zip 上传、git submodule

## 来源引用

- [摘要：Contributions welcome.](summaries/摘要：Contributions welcome.md)（[原文](https://x.com/charliejhills/status/2048428282174156996)）

## 关联概念

- [Claude Code Skills](concepts/Claude Code Skills.md)

- [Skill Collection](concepts/Skill Collection.md)
