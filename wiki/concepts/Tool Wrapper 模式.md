---
title: Tool Wrapper 模式
type: concept
tags:
- Agent 协作模式
- 上下文管理
- 提示工程
status: 审核中
confidence: high
last_compiled: '2026-04-26'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/8fbac6a5ad37467bac26138413e8ba0e
notion_id: 8fbac6a5-ad37-467b-ac26-138413e8ba0e
---

## 定义

Tool Wrapper 模式是把某个库、框架或 API 的核心用法封装进 Skill，让 Agent 在需要时按需加载“领域专家”能力。

## 关键要点

- 适合快速变化或细节繁多的工具文档场景

- 能减少把整份说明塞进系统提示词的上下文浪费

- 本质是在 Skill 层封装专家知识而不是封装执行代码

## 来源引用

- [原文链接](https://x.com/KKaWSB/status/2034196862794961299)｜[摘要：Google 发布 5 个 Agent Skill 设计模式：告别乱写 SKILL.md 的时代](summaries/摘要：Google 发布 5 个 Agent Skill 设计模式：告别乱写 SKILL.md 的时代.md)

- [原文链接](https://x.com/oragnes/status/2034221173970796776)｜《Google Cloud 的 5 种 [SKILL.md](http://skill.md/) 设计模式：让 AI 编程助手更听话的「抄作业」指南》
