---
title: 摘要：OpenClaw 与 Hermes Agent 官方核心文档架构对比
type: summary
tags:
- Agent 框架
- 知识管理
status: 已审核
confidence: high
last_compiled: '2026-04-16'
source_tags: ''
source_article_url: https://www.notion.so/344701074b6880dd995acb5fdc19fb2a
notion_url: https://www.notion.so/0a61eb4a268c476298e3494d6c769074
notion_id: 0a61eb4a-268c-4762-98e3-494d6c769074
---

### 一句话摘要

这篇文章基于官方文档对比了 OpenClaw 与 Hermes Agent 的核心文档架构，结论是前者更偏向可审计、文件驱动的人工作业体系，后者更偏向自进化、动态最小化的上下文组装体系。

### 关键洞察

- OpenClaw 采用 workspace 多 Markdown 文件分层，把人格、操作规则、用户模型、工具约定与长期记忆拆开治理。

- Hermes Agent 将稳定人格、记忆快照、技能索引与项目上下文分配到明确的 prompt 层级里，整体更偏工程化与最小化。

- 两者都使用 Markdown 文件承载 Agent 的长期结构，但 OpenClaw 更强调“文件即大脑”的透明与可控，Hermes 更强调按需加载与持续演化。

- 在 Hermes 中，[SOUL.md](http://soul.md/) 是全局固定身份槽位，Skills 以索引加按需加载的方式进入上下文，这与 OpenClaw 的固定手册式工作空间形成鲜明对比。

- 对 Tizer 的工作流而言，OpenClaw 的文件分层适合沉淀稳定操作规范，Hermes 的程序性记忆思路更适合降低上下文膨胀并持续优化执行链路。

### 提取的概念

- [OpenClaw](entities/OpenClaw.md)

- [Hermes Agent](entities/Hermes Agent.md)

- [文件即大脑](concepts/文件即大脑.md)

- [程序性记忆](concepts/程序性记忆.md)

### 原始文章信息

- 作者：未填写

- 来源：X书签文章数据库

- 发布时间：未填写

- 原文链接：未填写

- 源文章：[OpenClaw 与 Hermes Agent 官方核心文档架构对比](https://www.notion.so/344701074b6880dd995acb5fdc19fb2a)

### 个人评注

这篇对比最有价值的地方，在于把“稳定手册”和“自生长技能”两种 Agent 组织方式拆开讲清楚了。若用于 Tizer 的 HITL、OpenClaw 与内容流水线场景，可以把 OpenClaw 式文件分层视为长期稳定层，再把 Hermes 式程序性记忆与按需加载视为增量优化层。
