---
title: Evals
type: concept
tags:
- Harness 工程
- 模型评测
- Agent 协作模式
status: 审核中
confidence: high
last_compiled: '2026-04-12'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/7f8e64afe0bc4002ba4274c36ab8919c
notion_id: 7f8e64af-e0bc-4002-ba42-74c36ab8919c
---

## 定义

Evals 是一组用来检验 Agent 是否采取了正确行动、产生了正确结果的评测用例集合，在 Agent 工程里承担接近“梯度信号”的反馈作用。

## 关键要点

- 既可以来自真实生产 Trace，也可以来自人工标注或公开数据集

- 作用不是单次打分，而是持续暴露失败模式并指导系统迭代

- 在 Harness 优化里，Evals 的质量往往比单次模型替换更关键

## 关联概念

- [Agent Harness](concepts/Agent Harness.md)

- [Coding Agent](concepts/Coding Agent.md)

- [软件工厂](concepts/软件工厂.md)

- [Notion Custom Agents](entities/Notion Custom Agents.md)

## 来源引用

- [摘要：「不就是几个 Markdown 文件」：一场关于 Agentic 工程本质的争论](summaries/摘要：「不就是几个 Markdown 文件」：一场关于 Agentic 工程本质的争论.md)（[原文](https://x.com/garrytan/status/2045371983312097409)）

- [原文链接](https://x.com/berryxia/status/2042367800338260467)｜《Better-Harness：LangChain 用 Evals 当梯度信号，让 Agent 越跑越强》｜源文章：Better-Harness：LangChain 用 Evals 当梯度信号，让 Agent 越跑越强

- [原文链接](https://mp.weixin.qq.com/s?__biz=Mzg5NTc0MjgwMw%3D%3D&mid=2247523808&idx=1&sn=0a6aea0c1f3f9c5c6e86eff9592fd30b&chksm=c17464df982ee29fa92c7272b71d87b2dc6c54287a5fd8e61657920ebeb34565f22f3d893ff4#rd)｜《Notion Custom Agents复盘：三年重写5次，Notion 历史上最成功的新功能之一》｜源文章：Notion Custom Agents复盘：三年重写5次，Notion 历史上最成功的新功能之一
