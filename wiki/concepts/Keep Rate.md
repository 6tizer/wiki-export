---
title: Keep Rate
type: concept
tags:
- 模型评测
status: 草稿
confidence: high
last_compiled: '2026-05-03'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/e8f179e48ecf485a8dcb6da49196cb39
notion_id: e8f179e4-8ecf-485a-8dcb-6da49196cb39
---

## 定义

Keep Rate 是一种 Agent 产品质量指标，通过追踪 Agent 提交的代码改动在用户 codebase 中的留存率来衡量 Agent 工作质量。具体做法是：在固定时间间隔后检查 Agent 所做的改动是否仍然保留在代码库中——改动被改回、覆盖或回滚均视为质量负信号。

该指标由 Cursor 团队提出并在其 Agent Harness 持续改进实践中使用。

## 关键要点

- **被动捕获**：基于用户真实行为而非主观打分，无需额外交互即可获取

- **纵向可比**：可用于对比不同 harness 版本、不同模型、不同时间段的 Agent 质量

- **决策支持**：让团队能够基于数据拒绝"看起来美好但实际无用"的实验（如更贵的模型做 context 摘要）

- **可迁移思路**：客服 Agent 的 Keep Rate 类比是"对话结束后是否转人工"；写作 Agent 是"生成内容被保留的比例"；数据分析 Agent 是"生成查询是否被复用"

## 与其他指标的关系

- 区别于 benchmark 离线评估（如 CursorBench），Keep Rate 是线上真实行为指标

- 区别于 A/B 测试的过程指标（延迟、token 效率、cache 命中率），Keep Rate 直接反映最终产出质量

- 与 LLM 语义满意度判断互补——后者通过分析用户后续回复判断 Agent 是否完成任务

## 来源引用

- [摘要：精读 Cursor《Continually improving our agent harness》：一个 agent 产品团队的工程方法论全景](summaries/摘要：精读 Cursor《Continually improving our agent harness》：一个 agent 产品团队的工程方法论全景.md)（[原文](https://x.com/elliotchen100/status/2050757239364002193)）
