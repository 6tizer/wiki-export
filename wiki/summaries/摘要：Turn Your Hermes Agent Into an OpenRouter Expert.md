---
title: 摘要：Turn Your Hermes Agent Into an OpenRouter Expert
type: summary
tags:
- 模型部署
- CLI 工具
- Harness 工程
status: 已审核
confidence: high
last_compiled: '2026-04-27'
source_tags: ''
source_article_url: https://www.notion.so/34f701074b68815b898cf9586d291e45
notion_url: https://www.notion.so/Tizer/60a711f8314d4b9dbaf5704d8d210115
notion_id: 60a711f8-314d-4b9d-baf5-704d8d210115
---

## 一句话摘要

本文是 OpenRouter 官方发布的实战教程，教用户将 Hermes Agent 连接至 OpenRouter，并通过 Skill 系统创建可复用的 openrouter-expert 技能，使 Hermes 在后续会话中自动查阅最新文档、选择正确 SDK 路径。

## 关键洞察

- **Hermes 是 provider-agnostic 的 Agent 框架**：内置记忆、工具调用和自进化 Skill 系统，使用越多越智能

- **OpenRouter 提供统一模型路由**：通过单一 API 访问数百个模型，支持统一计费、自动故障转移和智能路由

- **Skill 机制是核心亮点**：通过让 Hermes 读取 llms.txt（OpenRouter 的 LLM 可消费文档索引）自动生成 openrouter-expert 技能文件，避免硬编码模型 ID、价格等易变信息

- **OpenRouter Agent SDK（****`@openrouter/agent`****）**：TypeScript 工具包，`callModel` 原语封装了多轮工具调用、流式输出、状态管理和审批模式

- **决策框架优于死记硬背**：Skill 文件包含路由表、注意事项和验证步骤，让 Agent 每次会话都从正确上下文开始

## 提取的概念

- [Hermes Agent](entities/Hermes Agent.md)

- [OpenRouter](entities/OpenRouter.md)

- [OpenRouter Agent SDK](entities/OpenRouter Agent SDK.md)

- [llms.txt](concepts/llms.txt.md)

## 原始文章信息

- **作者**：@OpenRouter

- **来源**：X 书签

- **发布日期**：2026-04-24

- **原文链接**：[原文](https://x.com/OpenRouter/status/2047506176447783155)

## 个人评注

这篇文章展示了一种「Agent + 统一模型路由 + 自进化技能」的组合范式。对于 Tizer 的工作流有几个启示：

1. **Skill 自进化思路**与 OpenClaw 的 Dreaming 记忆机制异曲同工——都是让 Agent 在使用中积累可复用知识

1. **llms.txt 格式**值得关注，可考虑在知识 Wiki 中生成类似的结构化索引供 Agent 消费

1. **Provider-agnostic 架构**的实用价值——不绑死单一模型供应商，通过 OpenRouter 实现灵活切换，对降低依赖风险和成本优化都有帮助
