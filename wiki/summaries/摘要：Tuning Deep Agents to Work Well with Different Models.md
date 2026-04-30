---
title: 摘要：Tuning Deep Agents to Work Well with Different Models
type: summary
tags:
- Harness 工程
- 提示工程
- 模型评测
status: 已审核
confidence: high
last_compiled: '2026-04-30'
source_tags: ''
source_article_url: https://www.notion.so/352701074b6881fcb9cee136fdbc83cb
notion_url: https://www.notion.so/Tizer/ed4841ed337f4e82893a316b9b06cab7
notion_id: ed4841ed-337f-4e82-893a-316b9b06cab7
---

## 一句话摘要

Deep Agents 引入 Harness Profile 机制，通过为不同 LLM 模型家族定制提示词、工具命名与中间件，在 tau2-bench 子集上实现 10-20 个百分点的性能提升。

## 关键洞察

- **单一 harness 无法适配所有模型**：不同模型家族（OpenAI、Anthropic、Google）有各自的提示指南和工具约定，通用 harness 必然在某些模型上表现欠佳

- **Harness Profile 是声明式覆盖层**：通过 YAML 或 Python 注册 per-model 配置（提示词前后缀、工具包含/排除、中间件选择），框架在 `create_deep_agent()` 时自动适配，调用方代码零改动

- **具体优化差异显著**：Codex 模型需要 apply_patch 工具替换默认 file_edit 并重命名为 shell_command；Claude 模型需要增加 tool_result_reflection 与 tool_usage 提示段

- **Harness 工程的杠杆效应惊人**：同一模型在不同 harness 中表现差距极大——此前 gpt-5.2-codex 通过 harness 层变更从 52.8% 提升至 66.5%（Terminal-Bench 2.0 排名 Top 30 → Top 5）

- **开放生态设计**：Profile 支持自定义覆盖、插件分发和社区 PR 贡献，Builder 可以为自己的任务场景版本化管理 harness 配置

## 提取的概念

- [Deep Agents](entities/Deep Agents.md)

- [Harness Profile](concepts/Harness Profile.md)

- [tau2-bench](entities/tau2-bench.md)

- [Terminal-Bench 2.0](entities/Terminal-Bench 2.0.md)

## 原始文章信息

- **作者**：@Vtrivedy10 (Viv)

- **来源**：X 书签

- **发布时间**：2026-04-29

- **原文链接**：[X 推文](https://x.com/Vtrivedy10/status/2049535740233523600)

## 个人评注

Harness Profile 的核心思路——按模型定制执行环境——与 OpenClaw 的 harness 工程理念高度一致。对于 Tizer 的内容管道和 HITL 流程，这意味着：(1) 当切换底层模型时，不应只换 API key，而应同步调整提示词和工具配置；(2) Profile 的版本化管理模式可以直接借鉴到 OpenClaw 的多模型支持策略中；(3) tau2-bench 等多轮工具使用基准测试值得关注，可作为评估 Agent 改进的参考标准。
