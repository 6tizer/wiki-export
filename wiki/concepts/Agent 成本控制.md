---
title: Agent 成本控制
type: concept
tags:
- OpenClaw
status: 审核中
confidence: high
last_compiled: '2026-04-26'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/0a3709a770704b8a969bbd21e21d6211
notion_id: 0a3709a7-7070-4b8a-969b-bd21e21d6211
---

## 定义

Agent 成本控制是指在 AI Agent 运行过程中，通过配置、架构设计和监控手段来管理和优化 token 消耗与 API 调用成本的实践方法。

## 关键要点

- **子 Agent 模型分级**：子 Agent 默认继承主 Agent 模型，需通过 `subagents.model` 单独配置低成本模型（如数据抓取用 gpt-4o-mini，分析用 Sonnet，决策留给主 Agent）

- **超时控制**：`runTimeoutSeconds` 防止子 Agent 无限消耗 token，生产建议日常任务 120s，复杂分析 600s

- **Token 消耗黑洞四大原因**：Context 装了不该装的、子 Agent 重复抓取相同数据、Prompt 模糊导致反复确认、截图分辨率未控制

- **并发控制**：`maxConcurrent`（子 Agent 并发上限）与 `maxConcurrentRuns`（Cron 并发上限）是两个不同字段

- **可视化工具**：`/usage full` 开关显示每条回复的 token 用量和估算费用

## 来源引用

- [摘要：OpenClaw 进阶手册 Vol.3：跑稳之后，才是真的开始](summaries/摘要：OpenClaw 进阶手册 Vol.3：跑稳之后，才是真的开始.md)（[请致天下.AI](http://xn--ghqv4yd56a5mi.ai/), 2026-02-28）— 第一章完整讲述成本控制 5 个技巧

- [摘要：方舟Coding Plan——国产模型一键调用按请求计费](summaries/摘要：方舟Coding Plan——国产模型一键调用按请求计费.md)（沃垠AI，2026-03-02）— 火山引擎按请求次数计费而非按 Token，解决 Agent 高 Token 消耗的成本痛点

- [摘要：AI创业公司们，困在“眼前一黑”的账单里](summaries/摘要：AI创业公司们，困在“眼前一黑”的账单里.md)（硅星人Pro，2026-04-16，[原文](https://mp.weixin.qq.com/s?__biz=MzkyNjU2ODM2NQ%3D%3D&mid=2247627553&idx=1&sn=ca51a04a0641220cd517383bc40fcd20&chksm=c30473cf1fe2951be164c86c7015a839df8e9e645d6256ef93cdf5e93120d42e43f428539ad3#rd)) — 文章从商业化角度说明高性能模型调用、主动式执行链路和单位经济之间的成本张力。
