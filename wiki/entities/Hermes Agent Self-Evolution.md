---
title: Hermes Agent Self-Evolution
type: entity
tags:
- Harness 工程
- Agent 安全
status: 审核中
confidence: high
last_compiled: '2026-04-20'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/d7b1bdca3e3843d4bfebdce9b91804e1
notion_id: d7b1bdca-3e38-43d4-bfeb-dce9b91804e1
---

## 定义

Hermes Agent Self-Evolution 是 Nous Research 为 Hermes Agent 构建的自进化优化仓库，用 DSPy + GEPA 对 skill、工具描述、system prompt 乃至代码进行演化式改进。

## 关键要点

- 通过 API 调用完成候选变异、评估与筛选，不依赖 GPU 训练。

- 当前重点是技能文件优化，后续路线覆盖工具描述、system prompt、代码演化与持续优化闭环。

- 优化过程依赖测试、体积限制、语义保持与人工 PR 审核等 guardrails，避免失控改写。

- 单次优化成本约 2–10 美元，适合作为 Coding Agent 的实验性持续优化管线。

## 来源引用

- [原文链接](https://x.com/KKaWSB/status/2043119101028274268)｜《Evolutionary self-improvement for Hermes Agent》｜来源条目：[摘要：Evolutionary self-improvement for Hermes Agent](summaries/摘要：Evolutionary self-improvement for Hermes Agent.md)

- [原文链接](https://mp.weixin.qq.com/s?__biz=MzI3MTA0MTk1MA%3D%3D&mid=2652692364&idx=1&sn=806ef08f63d5bf567d421f8808528c22&chksm=f047438bdb7b8b7734f13ec8b0c731b8c3a0085d501b9d6454c92b66b5d973bec5e7bce653ea#rd)｜《Hermes Agent抄袭中国团队代码实锤！被锤后回应：你删号》｜来源条目：[摘要：Hermes Agent抄袭中国团队代码实锤！被锤后回应：你删号](summaries/摘要：Hermes Agent抄袭中国团队代码实锤！被锤后回应：你删号.md)

- 源文章：Hermes Agent 核心文档优化指南：让你的 AI 助手真正「越用越聪明」｜来源条目：[摘要：Hermes 核心文档架构详尽分析与优化方案指南](summaries/摘要：Hermes 核心文档架构详尽分析与优化方案指南.md)

- [原文链接](https://mp.weixin.qq.com/s?__biz=Mzg3MTk3NzYzNw%3D%3D&mid=2247506451&idx=1&sn=aec841a1c8c8ec2a99d64536babf7eae&chksm=cf1f5a4baf411e277ea71f2add117a204ea05d54a3884c6c63f8d79ec931d7d3a48694ae7f43#rd)｜《妈耶 HermesAgent直播回应抄没抄国内开发者》｜来源条目：[摘要：妈耶 HermesAgent直播回应抄没抄国内开发者](summaries/摘要：妈耶 HermesAgent直播回应抄没抄国内开发者.md)

- [摘要：Interesting insights, especially this: Hermes starts off as any other agent does, inefficient and often not sure how to complete a task that is training didnt have priors for. However, solve it once a](summaries/摘要：Interesting insights, especially this- Hermes starts off as any other agent does, inefficient and often not sure how to complete a task that is training didnt have priors for. However, solve it once a.md)（[原文](https://x.com/Teknium/status/2046001396819067008)）

- [摘要：1 Month with Hermes - I've been using Hermes wrong all along](summaries/摘要：1 Month with Hermes - I've been using Hermes wrong all along.md)（[原文](https://x.com/0xJeff/status/2048678335950311860)）

## 关联概念

- [Hermes Agent](entities/Hermes Agent.md)

- [技能自我进化](concepts/技能自我进化.md)

- [System Prompt 工程](concepts/System Prompt 工程.md)

- [EvoMap](entities/EvoMap.md)

- [Evolver](entities/Evolver.md)

- [GEPA](concepts/GEPA.md)

- [GEP 协议](concepts/GEP 协议.md)

- [AI洗代码](concepts/AI洗代码.md)

- [自我进化 Agent](concepts/自我进化 Agent.md)

- [EVOLUTION.md](concepts/EVOLUTION.md.md)

- [USER.md](concepts/USER.md.md)
