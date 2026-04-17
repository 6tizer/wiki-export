---
title: 摘要：Notion Custom Agents复盘：三年重写5次，Notion 历史上最成功的新功能之一
type: summary
tags:
- Agent 框架
- Coding Agent
status: 已审核
confidence: high
last_compiled: '2026-04-15'
source_tags: ''
source_article_url: https://www.notion.so/343701074b6881c99eb7cda0ba10dbb0
notion_url: https://www.notion.so/0193e95a75334ff880ae98e8e5681808
notion_id: 0193e95a-7533-4ff8-80ae-98e8e5681808
---

## 一句话摘要

Notion 用三年五次重写证明，真正可用的 Agent 产品不是把模型硬塞进原系统，而是围绕模型习性重构表达层、查询层、评测体系、权限边界和后台工作流，并把 Coding Agent 视为更长期的核心方向。

## 关键洞察

- Notion 在 2022 年就开始做 Agent，但直到模型、工具调用和上下文能力成熟后，产品才真正进入可发布状态

- 他们最大的工程教训是不要把内部复杂数据结构直接暴露给模型，而要改用模型熟悉的表示形式，比如 Markdown 和 SQL

- Notion 把 evals 视为理解模型边界、定义 headroom 和优化用户旅程的基础设施，而不只是传统意义上的测试

- 团队判断 MCP 很有价值，但更看好 CLI 这类可自举、可调试、可渐进暴露能力的执行环境

- 未来的软件工程会更多变成对 Agent 系统的设计、监督与维护，而不是人逐行写代码

## 提取的概念

- [Notion Custom Agents](entities/Notion Custom Agents.md)

- [Agent Harness](concepts/Agent Harness.md)

- [Coding Agent](concepts/Coding Agent.md)

- [软件工厂](concepts/软件工厂.md)

- [Evals](concepts/Evals.md)

- [Notion 风格 Markdown](concepts/Notion 风格 Markdown.md)

- [MCP 协议](concepts/MCP 协议.md)

## 原始文章信息

- 作者：Founder Park

- 来源：微信

- 发布时间：2026-04-15 20:50

- 原文链接：[微信文章](https://mp.weixin.qq.com/s?__biz=Mzg5NTc0MjgwMw%3D%3D&mid=2247523808&idx=1&sn=0a6aea0c1f3f9c5c6e86eff9592fd30b&chksm=c17464df982ee29fa92c7272b71d87b2dc6c54287a5fd8e61657920ebeb34565f22f3d893ff4#rd)

- 源页面：Notion Custom Agents复盘：三年重写5次，Notion 历史上最成功的新功能之一

## 个人评注

- 对 Tizer 的工作流来说，这篇文章最重要的启发不是“Agent 很强”，而是先把页面写入格式、数据库查询方式和权限边界做成模型友好的接口

- 如果后续继续建设 OpenClaw、内容管线或 HITL 流程，这篇材料提供了三个可直接复用的抓手：优先用 Markdown 和 SQL 承接交互、用 eval 体系驱动迭代、把确定性任务尽量代码化而不是反复消耗模型调用
