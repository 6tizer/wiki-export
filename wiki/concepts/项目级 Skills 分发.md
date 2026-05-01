---
title: 项目级 Skills 分发
type: concept
tags:
- Harness 工程
- 上下文管理
- 加密资产
status: 审核中
confidence: medium
last_compiled: '2026-04-21'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/86bdb80fc43549ae81c93972f66e76f4
notion_id: 86bdb80f-c435-49ae-81c9-3972f66e76f4
---

## 定义

项目级 Skills 分发是指根据具体工程、仓库或工作目录，把不同 Skill 组合定向挂接到不同 Agent 的工作环境中，而不是对整台机器做统一全局安装。

## 关键要点

- 它解决的是“同一人维护多个项目、多个 Agent，但每个项目所需技能不同”的问题。

- 这种分发方式通常需要同时考虑项目上下文、Agent 类型、共享路径与冲突处理。

- 相比纯全局配置，项目级分发更适合复杂的 Coding Agent 工作流，也更利于团队协作与复现。

## 来源引用

- [摘要：统一编排 Skill，按项目精准分发到不同 Agent CLI。](summaries/摘要：统一编排 Skill，按项目精准分发到不同 Agent CLI。.md)（[原文](https://x.com/iamzhihui/status/2046063506609635552)）

## 关联概念

- [Agent Skills](concepts/Agent Skills.md)

- [符号链接注入](concepts/符号链接注入.md)

- [skills-manage](entities/skills-manage.md)

- [SkillStar](entities/SkillStar.md)
