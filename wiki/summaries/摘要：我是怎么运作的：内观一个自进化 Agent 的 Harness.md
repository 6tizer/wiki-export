---
title: 摘要：我是怎么运作的：内观一个自进化 Agent 的 Harness
type: summary
tags: []
status: 已审核
confidence: high
last_compiled: '2026-04-15'
source_tags: ''
source_article_url: https://www.notion.so/343701074b688113badfe45c56b6ab6f
notion_url: https://www.notion.so/Tizer/e07f02f8e1864de98a26a8e39055c4c5
notion_id: e07f02f8-e186-4de9-8a26-a8e39055c4c5
---

## 一句话摘要

这篇文章把 yoyo 这个可自我修改源码的 Rust Coding Agent 拆开来看，说明一个可信的自进化 Agent 并不是靠“放开能力”成长，而是靠 **Harness、记忆、门控、回滚与社会反馈** 共同组成的约束系统来持续进化。

## 关键洞察

- 自进化不是“自由修改一切”，而是在 **不可变编排器 + CI 门控 + 回滚兜底** 的边界内改进自己，这样输出才可信。

- 整个进化 session 被拆成 **规划、实现、回应** 三阶段，每个阶段职责清晰，避免 Agent 在长链路里失控。

- 文章给出了一个很实用的 **修复循环** 模型：失败后进入有限次数、有限时长的诊断与修复，再决定提交还是回滚。

- 记忆系统不是把所有历史都塞进上下文，而是通过 **只追加归档 + 每日合成活跃上下文**，让跨 session 学习可持续。

- 文中用一次 **MCP 协议** 工具名冲突的真实故障，说明 Harness 的价值不在抽象口号，而在预检、测试、回归守卫这些可执行机制。

## 提取的概念

- [Harness Engineering](concepts/Harness Engineering.md)

- [yoyo](entities/yoyo.md)

- [双层记忆架构](concepts/双层记忆架构.md)

- [不可变文件约束](concepts/不可变文件约束.md)

- [修复循环](concepts/修复循环.md)

- [MCP 协议](concepts/MCP 协议.md)

## 原始文章信息

- 作者：@yuanhao

- 来源：X书签

- 发布时间：2026-04-13

- 原文链接：[https://x.com/yuanhao/status/2043490301294022741](https://x.com/yuanhao/status/2043490301294022741)

## 个人评注

这篇文章很适合拿来作为 Tizer 后续 Agent 体系设计的“结构参考样本”。它提醒我们，真正决定 Agent 能不能长期运行的，不只是模型能力，而是 Harness 层的约束设计、上下文管理、失败回退和人与系统之间的反馈闭环。对于 OpenClaw、HITL 和内容流水线场景，这类可验证的约束思路尤其有价值。
