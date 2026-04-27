---
title: 摘要：开源一个 PPT Skill｜压进了我 10 年的设计经验
type: summary
tags:
- AI 设计
- 提示工程
status: 已审核
confidence: high
last_compiled: '2026-04-27'
source_tags: ''
source_article_url: https://www.notion.so/34f701074b688199b44ed76a9ae4c254
notion_url: https://www.notion.so/Tizer/697d0c25318f4176808e8032b8b29be6
notion_id: 697d0c25-318f-4176-808e-8032b8b29be6
---

## 一句话摘要

设计师 @op7418 将十年排版经验编码为一套开源 AI Skill（guizang-ppt-skill），让 Claude Code 等 Agent 能自动生成高品质杂志风单文件 HTML 演示文稿。

## 关键洞察

- **Skill = 领域知识压缩包**：将设计规则（字体分级、色彩纪律、网格节奏）写进 [SKILL.md](http://skill.md/) 和 [checklist.md](http://checklist.md/)，AI 按规则逐条执行，实现「十年经验一键复用」

- **约束式设计优于自由度**：5 套主题仅暴露 6 个 CSS 变量，禁止用户自定义 hex；连续三页相同主题被判 P0 错误——通过严格约束保障美学一致性

- **澄清前置拦截返工**：AI 主动询问 6 个问题（受众、时长、素材、图片、主题、约束）后才开始生成，将「对齐」前移到开头，拦截 80% 返工

- **单文件 HTML 交付**：产物是一个可双击打开的 HTML 文件，支持键盘/滚轮/触屏翻页，无需担心字体和动画兼容问题

- **副产品 > 主产品**：原本为私享会准备的 PPT 工具反而成为最受欢迎的成果，验证了「用户在你没用心的地方帮你看见真需求」

## 提取的概念

- [guizang-ppt-skill](entities/guizang-ppt-skill.md)（entity）：本文介绍的开源 PPT Skill 工具

- [SKILL.md](concepts/SKILL.md.md)（concept）：Skill 生态核心描述文件，本文以 [SKILL.md](http://skill.md/) + [checklist.md](http://checklist.md/) 形式承载设计规则

- [Claude Code Skills](concepts/Claude Code Skills.md)（concept）：Claude Code 的技能扩展机制，本文 Skill 通过 `npx skills add` 安装

## 原始文章信息

- **作者**：@op7418（歸藏 / [guizang.ai](http://guizang.ai/)）

- **来源**：X 书签

- **发布时间**：2026-04-24

- **原文链接**：[https://x.com/op7418/status/2047486546300051478](https://x.com/op7418/status/2047486546300051478)

- **GitHub 仓库**：[github.com/op7418/guizang-ppt-skill](http://github.com/op7418/guizang-ppt-skill)

## 个人评注

这篇文章展示了 Skill 模式在**非编程领域**（设计/排版）的成功应用。与 OpenClaw 内容 pipeline 的关联在于：Skill 本质上是「把专家知识编码为 AI 可执行的 SOP」，与 HITL 工作流中的 Agent 指令设计思路一致。约束式设计哲学（「约束越严，风格越稳」）也可以迁移到 Agent 任务规范——给 Agent 更少选项反而产出更稳定的结果。
