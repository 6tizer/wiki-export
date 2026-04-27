---
title: guizang-ppt-skill
type: entity
tags:
- AI 设计
- 提示工程
status: 草稿
confidence: high
last_compiled: '2026-04-27'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/5f8d0fd4d93247deafbf002a796a7ca7
notion_id: 5f8d0fd4-d932-47de-afbf-002a796a7ca7
---

## 定义

guizang-ppt-skill 是由设计师 @op7418（歸藏）开源的一套 AI PPT 生成 Skill，将十年设计经验编码为结构化指令文件（[SKILL.md](http://skill.md/) + [checklist.md](http://checklist.md/)），供 Claude Code 等 AI Agent 自动生成高品质杂志风 HTML 演示文稿。

**别名**：guizang PPT Skill、归藏 PPT Skill

## 关键要点

- **产出格式**：单文件 HTML，双击浏览器即可查看，支持键盘/滚轮/触屏翻页

- **设计风格**：「电子杂志 × 电子墨水」——灵感来自《Monocle》《卫报》《NYT》印刷杂志版式传统，叠加 Kindle 电子纸阅读美学

- **10 种页面布局**：封面、章节幕封、数据大字报、左文右图、图片网格、Pipeline 流程、悬念问题、大引用、Before/After 对比、图文混排

- **5 套主题色预设**：墨水经典、靛蓝瓷、森林墨、牛皮纸、沙丘——每套仅 6 个 CSS 变量，禁止用户自定义 hex

- **约束式设计哲学**：「约束越严，风格越稳」——通过限制自由度保障美学一致性

- **字体三级分工**：衬线（观点）→ 非衬线（信息）→ 等宽（元数据）

- **协作流程**：AI 主动询问 6 个澄清问题（受众、时长、素材、图片、主题、约束）后生成大纲，对齐后再编码

- **安装方式**：`npx skills add op7418/guizang-ppt-skill` 或手动复制至项目

## 档案

- **作者**：@op7418（歸藏 / [guizang.ai](http://guizang.ai/)）

- **仓库**：[github.com/op7418/guizang-ppt-skill](http://github.com/op7418/guizang-ppt-skill)

- **发布时间**：2026-04-24

- **适用 Agent**：Claude Code、Bloome 等支持 Skill 文件的 AI Agent

## 来源引用

- [摘要：开源一个 PPT Skill｜压进了我 10 年的设计经验](summaries/摘要：开源一个 PPT Skill｜压进了我 10 年的设计经验.md)（[原文](https://x.com/op7418/status/2047486546300051478)）

## 关联概念

- [SKILL.md](concepts/SKILL.md.md)

- [Claude Code Skills](concepts/Claude Code Skills.md)
