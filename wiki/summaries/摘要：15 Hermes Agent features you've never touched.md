---
title: 摘要：15 Hermes Agent features you've never touched
type: summary
tags:
- Harness 工程
- 上下文管理
- AI 产品
status: 已审核
confidence: medium
last_compiled: '2026-04-29'
source_tags: ''
source_article_url: https://www.notion.so/351701074b688122932ed4dd07e5b385
notion_url: https://www.notion.so/Tizer/5e779d976694447191510a486e3a521d
notion_id: 5e779d97-6694-4471-9151-0a486e3a521d
---

## 一句话摘要

Hermes Agent 远不止一个智能聊天机器人——大多数用户只用了它 8% 的能力，本文按影响力排序介绍了 15 个被忽视的高级功能，涵盖持久人格/记忆、会话分支、运行中纠偏、多模型路由、17 平台网关和可编程技能系统。

## 关键洞察

- **持久人格与记忆**：通过 [SOUL.md](http://soul.md/) 定义 Agent 永久人格，[MEMORY.md](http://memory.md/) + [USER.md](http://user.md/) 提供跨会话持久记忆，消除「每次重新解释自己是谁」的低效循环

- **会话版本控制**：`/branch` 实现对话分支、`/rollback` 实现文件系统回滚、`/snapshot` 实现全局状态快照，三者构成完整的「后悔药」体系

- **运行中纠偏**：`/steer` 允许在 Agent 执行多步任务时插入方向修正，无需中断当前轮次或丢失 prompt 缓存

- **辅助模型路由**：可为上下文压缩、摘要、标题生成等子任务分配独立的轻量模型，避免用顶级模型处理低复杂度工作，显著降低 token 成本

- **技能即斜杠命令**：Hermes 内置 100+ 可组合技能，用户还可编写自定义 Skill 永久绑定到所有会话和平台，真正实现工作流的复合积累

## 提取的概念

- [Hermes Agent](entities/Hermes Agent.md)

- [Hermes Skills](concepts/Hermes Skills.md)

- [Agent 会话分支](concepts/Agent 会话分支.md)

- [Steer 机制](concepts/Steer 机制.md)

- [辅助模型路由](concepts/辅助模型路由.md)

## 原始文章信息

- **作者**：@sharbel

- **来源**：X 书签

- **发布时间**：2026-04-28

- **原文链接**：[x.com/sharbel/status/2049158152709382177](http://x.com/sharbel/status/2049158152709382177)

## 个人评注

本文是一篇 Hermes Agent 的深度功能盘点，对 Tizer 的工作流有以下参考价值：

- [**SOUL.md**](http://soul.md/)** / **[**MEMORY.md**](http://memory.md/)** 模式**与 OpenClaw 的 Agent 人格持久化需求高度相关——可以借鉴其文件级持久记忆的设计思路

- **Skills 系统**的「声明式工作流封装 + 斜杠命令触发」范式，与 content pipeline 中的自动化编译流程理念一致

- **辅助模型路由**策略可直接应用于当前多 LLM 调用场景，在保持推理质量的同时控制成本

- **Cron + Webhook** 内置调度能力对比当前 Notion Agent 的定时触发模式，提供了另一种轻量级自动化思路
