---
title: thin control over thick state
type: concept
tags:
- Agent 协作模式
- 上下文管理
- 长期记忆
status: 审核中
confidence: high
last_compiled: '2026-04-26'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/f3a9f2bfb39242059115c7e4f93e8ee7
notion_id: f3a9f2bf-b392-4205-9115-c7e4f93e8ee7
---

> 一句话定义：thin control over thick state 是一种将轻量控制层与厚重项目状态分离设计的长程 Agent 组织原则。

### 定义

该思路主张让顶层控制只负责阶段判断、任务推进和委派，而把论文分析、计划、代码、日志和中间结论等需要跨阶段继承的内容沉淀到工作区中。

### 关键要点

- 控制层保持轻量，减少上下文负担。

- 状态层保持厚重，承载长期可复用的项目证据。

- 它的目标不是增加对话轮次，而是提高跨轮次继承与重用的稳定性。

### 来源引用

- [摘要：AI 真能把一篇论文一路做到实验结果吗？人大团队提出 AiScientist，长程研究工程迈出关键一步](summaries/摘要：AI 真能把一篇论文一路做到实验结果吗？人大团队提出 AiScientist，长程研究工程迈出关键一步.md)（[原文](https://mp.weixin.qq.com/s?__biz=Mzg2NzU4MDgzMA%3D%3D&mid=2247557693&idx=1&sn=367f8f10f46f5c95eecef42bd9280dc9&chksm=cf967e47a56f2e2647889686f1659551c441eaf8328436186303bca812623542fdfc4e646bf3#rd)，作者：机智流，源页面：AI 真能把一篇论文一路做到实验结果吗？人大团队提出 AiScientist，长程研究工程迈出关键一步）
