---
title: Tool Calling
type: concept
tags:
- Agent 技能
- LLM
status: 草稿
confidence: high
last_compiled: '2026-04-15'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/33902eb0e13e405b8c2de8c7bff64b0c
notion_id: 33902eb0-e13e-405b-8c2d-e8c7bff64b0c
---

## 定义

Tool Calling 是指 LLM 先输出结构化工具请求，再由外部执行器调用真实工具并把结果返回给模型的协作机制，是 Agent 能连接外部世界的基础接口。

## 关键要点

- 模型本身不会执行工具，只会决定何时调用什么工具以及如何使用结果

- 工具调用结果必须返回到对话上下文里，模型才能继续推理下一步

- 单次 Tool Calling 解决的是“调用一次工具”，而 Agent Loop 解决的是“持续调用直到任务完成”

- Tool Calling 让天气查询、提醒设置、搜索、代码执行这类外部能力可被模型编排

## 关联概念

- [Prompt Engineering](concepts/Prompt Engineering.md)

- [Context Engineering](concepts/Context Engineering.md)

- [GLM-5.1](entities/GLM-5.1.md)

- [vLLM](entities/vLLM.md)

- [SGLang](entities/SGLang.md)

- [Chat Template](concepts/Chat Template.md)

- [Agentic RAG](concepts/Agentic RAG.md)

- [Claude Skills](entities/Claude Skills.md)

- [fireworks-tech-graph](entities/fireworks-tech-graph.md)

## 来源引用

- 《Chat Bot 加一个循环，就进化成了 Agent》｜X书签文章｜原文链接：[https://x.com/LawrenceW_Zen/status/2042236281988812919](https://x.com/LawrenceW_Zen/status/2042236281988812919)｜源文章：Chat Bot 加一个循环，就进化成了 Agent

- 《GLM-5.1 的 Tool Calling 循环死锁：一个 Chat Template 引发的「幽灵 Bug」》｜X书签文章｜原文链接：[https://x.com/Zai_org/status/2044741938604093443](https://x.com/Zai_org/status/2044741938604093443)｜源文章：GLM-5.1 的 Tool Calling 循环死锁：一个 Chat Template 引发的「幽灵 Bug」

- [原文链接](https://mp.weixin.qq.com/s?__biz=MzY5NzIxODM2MQ%3D%3D&mid=2247484388&idx=1&sn=d2f897dce455cb4abdcaa39f7f91a864&chksm=f5f28e3e3d180a1e33285f77fa24c32d02bd1a720aa00b7f6b5850934693a9f64e247fac389a#rd)｜《fireworks-tech-graph：用自然语言生成工业级架构图，Claude Code 绘图神器！》｜来源条目：[摘要：fireworks-tech-graph：用自然语言生成工业级架构图，Claude Code 绘图神器！](summaries/摘要：fireworks-tech-graph：用自然语言生成工业级架构图，Claude Code 绘图神器！.md)
