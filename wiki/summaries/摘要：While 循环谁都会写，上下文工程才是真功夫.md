---
title: 摘要：While 循环谁都会写，上下文工程才是真功夫
type: summary
tags:
- Coding Agent
- Agent 编排
status: 已审核
confidence: high
last_compiled: '2026-04-15'
source_tags: ''
source_article_url: https://www.notion.so/343701074b688144a138c4a7eafb9495
notion_url: https://www.notion.so/4441bde5ded64b9db93e0c95b5b2783a
notion_id: 4441bde5-ded6-4b9d-b93e-0c95b5b2783a
---

## 一句话摘要

这篇文章指出，Agent 的 while 循环只是最小骨架，真正决定效果的是如何在每一轮里组织系统提示词、工具描述与历史记录，也就是上下文工程。

## 关键洞察

- Agent 的连续推理能力并不来自模型“有记忆”，而来自每一轮都把前文决策和工具结果重新塞回上下文

- 工具对 LLM 来说首先是一段文字说明，名称、描述和参数定义是否清晰，会直接决定调用质量

- 上下文会随着循环不断膨胀，而上下文窗口是有限的，这使得保留、压缩和裁剪历史成为核心工程问题

- Agent 工程的大量时间并不花在循环代码本身，而是花在系统提示词、工具描述、历史管理和结果清洗上

- 从 Prompt Engineering 到 Context Engineering，关键能力始终是把复杂任务转化为模型能稳定理解和执行的文本结构

## 提取的概念

- [Context Engineering](concepts/Context Engineering.md)

- [Agent Loop](concepts/Agent Loop.md)

- [工具描述](concepts/工具描述.md)

- [上下文窗口](concepts/上下文窗口.md)

- [System Prompt 工程](concepts/System Prompt 工程.md)

- [Prompt Engineering](concepts/Prompt Engineering.md)

## 原始文章信息

- 作者：@LawrenceW_Zen

- 来源：X书签

- 发布时间：2026-04-13

- 原文链接：[https://x.com/LawrenceW_Zen/status/2043580374501249175](https://x.com/LawrenceW_Zen/status/2043580374501249175)

- Notion 源页面：上下文工程：Agent 真正的核心能力不是写循环，是管好喂给 LLM 的那串文字

## 个人评注

这篇内容对 Tizer 的工作流有直接参考价值。无论是 OpenClaw 相关实验、HITL 流程，还是内容管线里的多步自动化，稳定性往往都不取决于循环外壳，而取决于上下文注入是否清楚、节制且可复用。
