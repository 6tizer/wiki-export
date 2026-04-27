---
title: Bitter Lesson 原则
type: concept
tags:
- Harness 工程
status: 草稿
confidence: high
last_compiled: '2026-04-27'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/9c68d16b45e04c45b1c8144adf50eb03
notion_id: 9c68d16b-45e0-4c45-b1c8-144adf50eb03
---

## 定义

Bitter Lesson 原则源自 Rich Sutton 2019 年的经典文章《The Bitter Lesson》，核心论点是：利用通用计算能力（搜索与学习）的方法，长期来看总是碾压依赖人类先验知识的手工特征方法。在 Agent 工程领域，这一原则被延伸为：不要用抽象层包裹 LLM，也不要包裹它的工具——给模型最大动作空间，再逐步约束。

## 关键要点

- 原始出处是 Rich Sutton 在 AI 领域 70 年历史中的观察：人工注入的领域知识短期有效，但长期不敌可扩展的通用方法

- Browser Use 团队将此原则应用到 Agent Harness 设计：从包裹 click()、type() 等抽象，转向直接暴露 CDP 原始接口

- 不仅模型的框架层是抽象，工具层（helpers）同样是抽象，同样应被精简甚至让模型自行编写

- 与 Harness Engineering 中「Thin Harness, Fat Skills」理念高度一致

## 来源引用

- [摘要：The Bitter Lesson of Agent Harnesses](summaries/摘要：The Bitter Lesson of Agent Harnesses.md)（[原文](https://x.com/gregpr07/status/2047358189327520166)）

## 关联概念

- [Agent Harness](concepts/Agent Harness.md)

- [Thin Harness, Fat Skills](concepts/Thin Harness, Fat Skills.md)

- [Harness Engineering](concepts/Harness Engineering.md)

- [Browser Harness](entities/Browser Harness.md)
