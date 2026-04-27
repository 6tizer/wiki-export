---
title: 摘要：Design principles for building an Agent harness
type: summary
tags:
- Harness 工程
- 上下文管理
status: 已审核
confidence: high
last_compiled: '2026-04-27'
source_tags: Agent, harness
source_article_url: https://www.notion.so/34f701074b68816eb691fc2742b194d3
notion_url: https://www.notion.so/Tizer/7aa67755430446d1b7b81b5766c83919
notion_id: 7aa67755-4304-46d1-b7b8-1b5766c83919
---

## 一句话摘要

构建生产级 Agent Harness 需要在七个架构维度上做权衡，而其中三个最常见的直觉选择——工具越多越强、ReAct 优于 Planning、宽松权限更快出货——恰恰是错的。

## 关键洞察

- **工具膨胀是认知负荷而非能力提升**：Vercel 砍掉 v0 中 80% 的工具后 Agent 性能反而提升；Claude Code 按步骤动态加载工具，上下文占用降低 95%

- **Plan-and-Execute 在有界任务上比 ReAct 快 3.6 倍**：大多数步骤不需要重新推理，只需执行；ReAct 买的是适应性，Plan-and-Execute 买的是速度和可预测性

- **宽松 Harness 在生产环境会出事**：开发时无摩擦的 permissive harness 一旦上线，第一次不可逆操作就会引发事后分析；审批门控（gated tool call）才是真正的安全特性

- **七个架构决策维度**：Agent 数量、推理策略、上下文策略、验证机制、权限模型、工具范围（tool scoping）、harness 厚度

- **共性模式**：直觉优化的是开发体验（更多能力展示、更多推理、更少摩擦），正确答案优化的是真实负载下的表现（更少上下文压力、更少浪费的 LLM 调用、更少不可逆错误）

## 提取的概念

- [Agent Harness](concepts/Agent Harness.md)

- [ReAct Agent](concepts/ReAct Agent.md)

- [Plan-and-Execute 模式](concepts/Plan-and-Execute 模式.md)

- [Tool Scoping](concepts/Tool Scoping.md)

## 原始文章信息

- **作者**：@akshay_pachaar

- **来源**：X书签

- **发布时间**：2026-04-24

- **原文链接**：[https://x.com/akshay_pachaar/status/2047671145475068038](https://x.com/akshay_pachaar/status/2047671145475068038)

## 个人评注

这篇文章对 Agent Harness 的七维度架构决策框架非常系统化。对 Tizer 的 OpenClaw 项目有直接参考价值：

- Tool Scoping 原则可以指导 OpenClaw 的 Skill 注册策略——不要一次性暴露所有 Skills，按任务阶段动态加载

- Plan-and-Execute vs ReAct 的权衡对 OpenClaw 的批量内容处理流水线（如本 Wiki Compiler）尤其重要：结构化任务用 Plan 模式更高效

- 权限门控的思路与 Harness-as-Policy 理念一致，强化了「安全边界是 harness 的核心特性而非附加功能」的观点
