---
title: Symphony
type: concept
tags:
- Agent 编排
status: 审核中
confidence: high
last_compiled: '2026-04-29'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/1edab3c7d5b04b10acab1f2fb0b0cabf
notion_id: 1edab3c7-d5b0-4b10-acab-1f2fb0b0cabf
---

**定义**：Symphony 是 OpenAI 开源的 AI 编程自主管理框架，将每个工作任务变成独立的自主执行运行，实现工程师从"监督代码"到"管理工作"的范式转变。

**核心设计理念**

工程师的精力应花在定义目标和审批结果上，而不是盯着 AI 一行一行地写。

**三大设计亮点**

1. **隔离运行机制**：每个任务在独立环境中运行，互不干扰，失败不污染其他任务

1. **工作证明机制（Proof of Work）**：Agent 提交代码的同时附上 CI 结果 + PR review 反馈 + 复杂度分析，审批有具体依据可对照

1. **规格驱动 + 多语言实现**：[SPEC.md](http://spec.md/) 定义协议，官方提供 Elixir 参考实现，可用任意语言重新实现

**适用场景**

- 已有完整 CI/CD 和测试体系的代码库

- 团队已用 Codex 等工具，希望减少实时监督耗时

**注意事项**

- 目前为低调工程预览版，不建议直接用于生产环境

- 代码库需先做好"工具链工程（harness engineering）"实践

**来源引用**

- [摘要：OpenAI 开源 Symphony！四天狂揽 8.7K Star，AI 编程自主管理神器！](summaries/摘要：OpenAI 开源 Symphony！四天狂揽 8.7K Star，AI 编程自主管理神器！.md)

- [摘要：OpenAI刚刚开源的这个东西，感觉要把程序员的工作方式给整个改写了。](summaries/摘要：OpenAI刚刚开源的这个东西，感觉要把程序员的工作方式给整个改写了。.md)（[原文](https://x.com/AYi_AInotes/status/2049100434137026673)）
