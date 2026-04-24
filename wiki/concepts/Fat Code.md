---
title: Fat Code
type: concept
tags:
- Coding Agent
- Agent 编排
status: 审核中
confidence: high
last_compiled: '2026-04-15'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/69d4d0a299064adeb189a5d4a7ec794e
notion_id: 69d4d0a2-9906-4ade-b189-a5d4a7ec794e
---

## 定义

Fat Code 是 Agentic Engineering 中承担确定性执行的代码层，用来承载需要精确控制、可测试、可复现的逻辑，而不是把这部分工作交给模型临场发挥。

## 关键要点

- 把 API 调用、数据转换、校验、调度等稳定逻辑下沉到代码层

- 代码层追求可测试、可复现、可观测，减少模型在关键路径上的随机性

- 当某段自动化需要明确输入输出、错误处理和边界约束时，应优先进入 Fat Code

- Fat Code 与 Skills 分工明确：Skills 负责判断与流程策略，Code 负责确定性执行

## 关联概念

- [Agentic Engineering](concepts/Agentic Engineering.md)

- [Thin Harness, Fat Skills](concepts/Thin Harness, Fat Skills.md)

## 来源引用

- [摘要：「不就是几个 Markdown 文件」：一场关于 Agentic 工程本质的争论](summaries/摘要：「不就是几个 Markdown 文件」：一场关于 Agentic 工程本质的争论.md)（[原文](https://x.com/garrytan/status/2045371983312097409)）

- [原文链接](https://x.com/chenchengpro/status/2043697811993350611)｜《Garry Tan 提炼了他在 agentic engineering 领域的核心心法：Fat Skills, Fat Code, Thin Harness。》｜源文章：Garry Tan 的 Agent 工程心法：Fat Skills、Fat Code、Thin Harness
