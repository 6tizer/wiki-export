---
title: 摘要：The Ultimate Hermes Guide - from one agent to a 4-profile team that still
  feels coherent on day 30
type: summary
tags:
- Agent 协作模式
- 多Agent协作
- 长期记忆
status: 已审核
confidence: high
last_compiled: '2026-04-16'
source_tags: ''
source_article_url: https://www.notion.so/344701074b688169975fcd49392034b2
notion_url: https://www.notion.so/Tizer/80322e9ec3974bb69b28254b374cbf9a
notion_id: 80322e9e-c397-4bb6-9b28-254b374cbf9a
---

## 一句话摘要

这篇文章提出，Hermes 多 Agent 团队真正能在 30 天后保持角色清晰的关键，不是继续优化 prompt，而是基于隔离 profile、交接契约、记忆健康指标、权限门控与统一调度表建立一套长期可运维的 operator layer。

## 关键洞察

- 单个 agent 同时承担研究、写作、编码和编排职责时，长期运行后会因为共享记忆与语气逐渐“糊成一个人”，隔离 profile 才是根本解法。

- Hermes 的 profile 不只是换人格外壳，而是同时隔离配置、session、memory、skills、个性、cron 状态与 gateway 状态。

- 多 Agent 系统是否能长期稳定，取决于 handoff contract 是否可执行、memory KPI 是否定期审计、各角色 policy gate 是否严格分层。

- [SOUL.md](http://soul.md/) 应定义稳定身份，[AGENTS.md](http://agents.md/) 应承载当前项目上下文，两者混用会导致角色漂移与提示词膨胀。

- 真正的长期失败常见于四类问题：profile drift、handoff rot、[SOUL.md](http://soul.md/) bloat 与 cron collision。

## 提取的概念

- [Hermes Agent](entities/Hermes Agent.md)

- [隔离式 Agent](concepts/隔离式 Agent.md)

- [SOUL.md](concepts/SOUL.md.md)

- [AGENTS.md](concepts/AGENTS.md.md)

- [Handoff 文档](concepts/Handoff 文档.md)

- [Memory KPI](concepts/Memory KPI.md)

- [Policy Gate](concepts/Policy Gate.md)

- [team-agents.md](concepts/team-agents.md.md)

- [Gateway](concepts/Gateway.md)

- [Cron 自动化](concepts/Cron 自动化.md)

## 原始文章信息

- 作者：@nyk_builderz

- 来源：X书签

- 发布时间：2026-04-15

- 原文链接：[https://x.com/nyk_builderz/status/2044472463279710344](https://x.com/nyk_builderz/status/2044472463279710344)

## 个人评注

这篇文章对 Tizer 当前的多 Agent 工作流很有参考价值，尤其适合用于梳理 HITL 编排、角色边界、记忆卫生和内容流水线的长期维护规则。它强调的不是“更强的提示词”，而是把角色隔离、交接规范和审计机制产品化，这与 OpenClaw 协作、多角色内容生产和知识管线治理高度一致。
