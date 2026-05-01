---
title: 摘要：DeepSeek-V4 发布 10 小时，北大开源项目实现了自动化评测！
type: summary
tags:
- 模型评测
- Harness 工程
- 链上协议
status: 已审核
confidence: high
last_compiled: '2026-04-24'
source_tags: ''
source_article_url: https://www.notion.so/34c701074b6881969eb8d77d3c26dc2f
notion_url: https://www.notion.so/Tizer/24a65771096541a7b80467d44299c92e
notion_id: 24a65771-0965-41a7-b804-67d44299c92e
---

## 一句话摘要

One-Eval 是北京大学 DCAI 团队开源的面向大模型评测的交互式自动化框架，它把模型评测从“手工拼配置 + 跑脚本”重构为自然语言发起、自动规划、可中断、可追溯、可生成报告的完整工作流。

## 关键洞察

- One-Eval 把 benchmark 选择、数据下载、字段映射、参数配置和报告生成串成一条自动化链路，显著降低了评测搭建成本。

- 它强调 Human-in-the-Loop：方案规划与关键参数确认保留人工决策，不追求盲目的全自动。

- 它通过 Global State 驱动的执行架构记录评测全过程，使 Prompt、模型输出、解析与打分链路都可以追溯。

- 通过 Benchmark Gallery 与 Metric Library 的模块化设计，新增 benchmark、替换 metric、扩展评测逻辑不再需要重写整套适配层。

- 文中实测表明，One-Eval 不只适用于通用问答，也可覆盖代码、数学、RAG、长上下文与 Agent 任务等复杂评测场景。

## 提取的概念

- [One-Eval](entities/One-Eval.md)

- [DataFlow](entities/DataFlow.md)

- [Human-In-The-Loop](concepts/Human-In-The-Loop.md)

- [Global State 数据总线架构](concepts/Global State 数据总线架构.md)

- [Benchmark Gallery](concepts/Benchmark Gallery.md)

- [Metric Library](concepts/Metric Library.md)

## 原始文章信息

- 作者：北京大学 DCAI 团队

- 来源：微信 / Datawhale开源

- 发布时间：2026-04-24 23:15

- 原文链接：[文章链接](https://mp.weixin.qq.com/s?__biz=MzIyNjM2MzQyNg%3D%3D&mid=2247722249&idx=1&sn=7e9f29cb43e6948fe35c0a1435f013d8&chksm=e909fc8f9ecba3b58d11840fbdb88bf7db327e9a06421ac4903412691391c0edb1ef97cc7696#rd)

## 个人评注

One-Eval 的价值不只是“帮你跑 benchmark”，而是把评测流程做成一套可编排、可追溯、可插拔的系统。这和 Tizer 当前做内容编译、HITL 审核、知识沉淀的思路是同一条线：关键不是单点工具能力，而是把复杂流程抽象为可复用工作流，让人只在高价值节点介入。
