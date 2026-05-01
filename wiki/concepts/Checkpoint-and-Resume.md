---
title: Checkpoint-and-Resume
type: concept
tags:
- Agent 编排
- 工作流
status: 审核中
confidence: high
last_compiled: '2026-04-23'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/2fb99fec9a904261960be5d6c162863b
notion_id: 2fb99fec-9a90-4261-960b-e5d6c162863b
---

**定义**：Checkpoint-and-Resume 是一种让长时运行智能体在执行过程中定期保存进度，并在失败、暂停或重启后从最近检查点继续执行的模式。

### 关键要点

- 适用于跨小时或跨天的批处理任务，避免因单点失败而整批重跑。

- 检查点粒度需要在可靠性与开销之间平衡，既不能过密，也不能只在末尾保存。

- 本质上是把 agent 当作长期运行的工作流进程，而不是一次性请求处理器。

### 来源引用

- [摘要：5 Agent Design patterns for Long-running AI Agents](summaries/摘要：5 Agent Design patterns for Long-running AI Agents.md)（[原文](https://x.com/GoogleCloudTech/status/2046989964077146490)）
