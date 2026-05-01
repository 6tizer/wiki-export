---
title: 摘要：字节最火的开源Agent项目，如何思考Agent的自我进化？
type: summary
tags:
- Harness 工程
- 上下文管理
- 模型评测
status: 已审核
confidence: high
last_compiled: '2026-04-16'
source_tags: ''
source_article_url: https://www.notion.so/344701074b6881c0bf8dd109349c75a1
notion_url: https://www.notion.so/Tizer/1a125e0d1282489a8f6f875f6dc3fe67
notion_id: 1a125e0d-1282-489a-8f6f-875f6dc3fe67
---

## 一句话摘要

这篇文章提出，Agent 的持续学习不应只理解为模型微调，而应拆分为 **Model、Harness、Context** 三层，并围绕 traces、记忆与评测闭环来设计系统级进化路径。

## 关键洞察

- **Model / Harness / Context** 是三种完全不同的学习对象，更新频率、成本和落地方式都不同

- 对多数团队来说，最现实的推进顺序不是先训模型，而是先补齐 **Context learning** 与 **Harness optimization**

- **traces** 是三层学习共享的基础燃料，既服务故障复盘，也服务评测、记忆整理与后续训练

- **Meta-Harness** 说明 Agent 可以借助完整历史代码、分数与执行轨迹，去自动提出新的 harness 改动

- 文中用 **Claude Code** 与 **OpenClaw** 做映射，说明很多所谓“Agent 变聪明了”，本质上发生在上下文配置和运行机制层，而不是权重层

## 提取的概念

- [Agent 持续学习三层框架](concepts/Agent 持续学习三层框架.md)

- [Agent Traces](concepts/Agent Traces.md)

- [Harness Engineering](concepts/Harness Engineering.md)

- [Context Engineering](concepts/Context Engineering.md)

- [Meta-Harness](concepts/Meta-Harness.md)

- [DeerFlow 2.0](entities/DeerFlow 2.0.md)

- [Claude Code](entities/Claude Code.md)

- [OpenClaw](entities/OpenClaw.md)

- [ClawHub](entities/ClawHub.md)

## 原始文章信息

- 作者：Founder Park

- 来源：微信

- 发布时间：2026-04-16

- 链接：[原文链接](https://mp.weixin.qq.com/s?__biz=Mzg5NTc0MjgwMw%3D%3D&mid=2247523832&idx=1&sn=8a7013894ddc0668c0f1c9f935599450&chksm=c1b17f5bd2d0ca49ee848d1dc13c14fb122c8f551ba00b307b566dfa7edc4c20a52573051f79#rd)

## 个人评注

对 Tizer 当前的 HITL、Wiki 编译、OpenClaw 与内容工厂路线，这篇文章最直接的启发不是立刻做模型层学习，而是先把 **traces 采集、上下文分层、harness 回放与评测** 做成稳定基础设施。这样后续无论是知识编译 Agent、内容流水线还是 OpenClaw 相关实验，都能形成可复盘、可记忆、可迭代的学习闭环。
