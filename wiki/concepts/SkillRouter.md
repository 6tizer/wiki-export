---
title: SkillRouter
type: concept
tags:
- Agent 技能
- Agent 编排
status: 审核中
confidence: high
last_compiled: '2026-04-19'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/5c8777b7c4064c5eac4cbe9d73ce22d7
notion_id: 5c8777b7-c406-4c5e-ac4c-be9d73ce22d7
---

## 定义

SkillRouter 是一个面向大规模 Agent 技能库的技能路由方案，目标是在给定用户任务后，从海量 Skill 中检索并排序出最合适的技能组合。

## 关键要点

- 它强调技能的完整实现体（body）是路由精度的关键输入，而不是只看名称与描述。

- 典型流程是全文本向量召回、交叉编码器重排，再把筛出的技能信息注入 Agent。

- 该方案把“技能检索”从简单关键词匹配提升为面向执行逻辑的语义路由问题。

## 来源引用

- [摘要：技术动态 | OpenClaw带火的大量Skill如何做RAG？一项实验报告及学科图表转LaTeXcode强化学习思路](summaries/摘要：技术动态  OpenClaw带火的大量Skill如何做RAG？一项实验报告及学科图表转LaTeXcode强化学习思路.md)
