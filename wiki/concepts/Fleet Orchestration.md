---
title: Fleet Orchestration
type: concept
tags:
- Agent 编排
- 工作流
status: 审核中
confidence: high
last_compiled: '2026-04-23'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/09cd4b4063064c1199c91a3c71e75951
notion_id: 09cd4b40-6306-4c11-99c9-1a3c71e75951
---

**定义**：Fleet Orchestration 是把多个长时运行智能体组织成协同舰队，由协调者分发任务、跟踪状态并在多个专长 agent 之间完成交接的编排模式。

### 关键要点

- 它强调协调者 / 专家式分工，而不是单一万能 agent。

- 每个 specialist agent 应独立拥有权限边界、策略约束与运行状态。

- 这种模式延续了分布式系统中的 coordinator/worker 思路，但把对象换成了 agent。

### 来源引用

- [摘要：5 Agent Design patterns for Long-running AI Agents](summaries/摘要：5 Agent Design patterns for Long-running AI Agents.md)（[原文](https://x.com/GoogleCloudTech/status/2046989964077146490)）
