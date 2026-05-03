---
title: Agent 模拟测试
type: concept
tags:
- 模型评测
- Agent 安全
status: 审核中
confidence: medium
last_compiled: '2026-04-28'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/9285ccb9acb94220897fe429b37869a0
notion_id: 9285ccb9-acb9-4220-897f-e429b37869a0
---

## 定义

Agent 模拟测试（Agent Simulation Testing）是指在 AI Agent 上线前，通过自动生成大量多轮对话场景（包括对抗性人设）来验证 Agent 行为的测试方法。目标是在生产环境暴露问题之前，发现幻觉、工具调用错误、PII 泄露等故障模式。

## 关键要点

- 模拟数千个多轮对话场景，覆盖文本和语音 Agent

- 使用对抗性人设（adversarial personas）来触发边界情况

- 与评估指标（eval metrics）联动，量化每个场景的通过率

- 不同类型 Agent（RAG、语音、Computer Use、编程）有不同的失败模式，需要分别模拟

- 核心价值：将「demo 能跑」到「生产可靠」之间的鸿沟用自动化手段填平

## 与相关概念的区别

- **模型评测**：侧重模型能力的基准测试；Agent 模拟测试侧重端到端工作流在复杂交互下的行为

- **Agent 可观测性**：事后观察线上行为；模拟测试是事前预防

- **Guardrails**：运行时拦截；模拟测试是部署前筛查

## 关联概念

- [Future AGI](entities/Future AGI.md)

- [Agent 可观测性](concepts/Agent 可观测性.md)

- [Agent Gateway](concepts/Agent Gateway.md)

- [Guardrails](concepts/Guardrails.md)

## 来源引用

- [摘要：Goodbye agents that silently hallucinate in production.](summaries/摘要：Goodbye agents that silently hallucinate in production.md)（[X Thread](https://x.com/hasantoxr/status/2047636566680760576)）
