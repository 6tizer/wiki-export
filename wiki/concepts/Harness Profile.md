---
title: Harness Profile
type: concept
tags:
- Harness 工程
- 提示工程
status: 草稿
confidence: high
last_compiled: '2026-04-30'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/6a5a4c467d504bafbb5411af79dffbea
notion_id: 6a5a4c46-7d50-4baf-bb54-11af79dffbea
---

## 定义

Harness Profile 是一种声明式的配置覆盖层，用于根据不同 LLM 模型家族定制 Agent 的执行环境参数，包括系统提示词前后缀、工具纳入与命名、中间件选择、子 Agent 配置和技能组合。通过 Profile 机制，同一个 Agent 框架可以针对 OpenAI、Anthropic、Google 等不同模型自动适配最优的 harness 配置，而无需修改调用代码。

别名：模型配置文件、Per-model Profile

## 关键要点

- **声明式覆盖**：Profile 以 YAML 或 Python 对象定义，涵盖 system_prompt_suffix、excluded_tools、excluded_middleware 等字段

- **按模型/提供商注册**：通过 `register_harness_profile()` 为特定模型（如 gpt-5.4、opus-4.7）注册专属配置

- **自动适配**：在 `create_deep_agent()` 调用时，框架根据传入的 model 参数自动加载对应 Profile，调用方代码无需变更

- **实测效果显著**：在 tau2-bench 子集上，启用 Profile 后性能提升 10-20 个百分点

- **可扩展**：支持自定义 Profile 覆盖默认值、插件分发、社区贡献

## 典型应用

- OpenAI Codex 模型：覆盖默认 file_edit 为 apply_patch 工具，重命名 execute 为 shell_command

- Anthropic Claude 模型：增加 tool_result_reflection 和 tool_usage 提示段，强调工具优先的工作模式

- Google Gemini 模型：加载 Google 特定提示约定

## 关联概念

- [Deep Agents](entities/Deep Agents.md)

- [tau2-bench](entities/tau2-bench.md)

- [Terminal-Bench 2.0](entities/Terminal-Bench 2.0.md)

## 来源引用

- [摘要：Tuning Deep Agents to Work Well with Different Models](summaries/摘要：Tuning Deep Agents to Work Well with Different Models.md)（[原文](https://x.com/Vtrivedy10/status/2049535740233523600)）
