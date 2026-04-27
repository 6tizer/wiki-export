---
title: '摘要：Agents 201: The Unit Shrank'
type: summary
tags:
- 多Agent协作
- Agent 协作模式
status: 已审核
confidence: high
last_compiled: '2026-04-27'
source_tags: ''
source_article_url: https://www.notion.so/34f701074b6881b488c5c5386e4156b5
notion_url: https://www.notion.so/Tizer/52611ee41a0e40d9bd614a56f63f305c
notion_id: 52611ee4-1a0e-40d9-bd61-4a56f63f305c
---

## 一句话摘要

多 Agent 系统的原子单元正从「Agent」转变为「Worker」——职责单一、可替换、可组合的工作单元，而 Supervisor/Swarm/Hierarchical 等编排模式不过是同一组原语（Worker、Function、Trigger）的不同触发器组合。

## 关键洞察

- **Monolithic Agent 的三重困境**：Token 经济爆炸（15K→60K）、专业化损失（一个模型身兼数职）、Vibes 调试（出错只能重跑），这是生产环境中单体 Agent 必然遇到的问题

- **原子单元的转变**：三个月前 Agent 是最小单元，现在 Worker 才是——有明确身份、定义的输入输出、只做一件事，Agent 只是组合后的称呼

- **三原语统一编排**：iii 框架提出 Worker + Function + Trigger 三个原语，将 Supervisor、Swarm、Hierarchical 等「架构」还原为触发器组合，消除了架构选型的伪命题

- **分层模型分配**：不同 Worker 使用不同成本的模型（如 Haiku 做执行、Opus 做编排），从架构层面解决 Token 成本问题，而非只靠压缩上下文

- **n+1 扩展而非 n²**：新能力加入只需连接一个 Worker，无需更新消费者服务、网关配置或注册表，协调成本趋近于零

## 提取的概念

- [iii](entities/iii.md)（开源后端统一与编排系统，三原语模型的具体实现）

- [Worker 模式](concepts/Worker 模式.md)（以窄范围 Worker 为原子单元的 Agent 架构范式）

- [Supervisor 模式](concepts/Supervisor 模式.md)（中央协调者分发任务的经典多 Agent 编排模式）

- [Agent Swarms](concepts/Agent Swarms.md)（去中心化状态触发的 Agent 协作模式）

## 原始文章信息

- **作者**：@ghumare64（Rohit Ghumare）

- **来源**：X 书签

- **发布时间**：2026-04-23

- **原文链接**：[https://x.com/ghumare64/status/2047401813364683007](https://x.com/ghumare64/status/2047401813364683007)

## 个人评注

这篇文章的核心洞察与 Tizer 的 OpenClaw 多 Agent 架构高度相关：

- **Worker 分解思路**可直接应用于 OpenClaw 的 Claw Groups——每个 Claw 本质上就是一个窄范围 Worker，专注于特定领域的代码生成或审查

- **分层模型分配**正是 HITL 内容管线中已在实践的策略——用轻量模型做初筛/提取，用强模型做最终审核

- **沙箱即 Worker** 的理念为 OpenClaw 的安全代码执行提供了一种更优雅的抽象：将沙箱视为 Function 而非基础设施

- iii 的 Function-Trigger-Worker 原语体系值得关注，其"所有编排模式都是触发器组合"的思路可能简化 OpenClaw 的 Agent 编排层设计
