---
title: 摘要：多Agent团队协作才是Hermes Agent的正确打开方式。
type: summary
tags:
- Agent 编排
- Agent 框架
status: 已审核
confidence: medium
last_compiled: '2026-04-26'
source_tags: ''
source_article_url: https://www.notion.so/343701074b688113b009e44a58a6ebd6
notion_url: https://www.notion.so/8686e90c56df4849a1e46bc6568af627
notion_id: 8686e90c-56df-4849-a1e4-6bc6568af627
---

### 一句话摘要

Hermes 更适合被组织成职责清晰的多 Agent 团队，而不是把所有需求都塞给单个 Agent；其关键做法是克隆独立 profile、用 [SOUL.md](http://soul.md/) 定义角色边界、用 [AGENTS.md](http://agents.md/) 共享项目背景，并分别调用各自的 agent。

### 关键洞察

- 单 Agent 容易出现上下文拥挤、记忆混杂和任务串行等待的问题

- `hermes profile create "xxx" --clone` 可以快速复制一套已调好的基础配置，同时保持记忆与会话独立

- [SOUL.md](http://soul.md/) 用来定义每个 agent 是谁、擅长什么、不能碰什么，是职责拆分的边界层

- [AGENTS.md](http://agents.md/) 适合作为项目级共享背景，沉淀目录结构、协作规则和当前进度

- 真正有效的多 Agent 协作，不是把一切继续塞回主 agent，而是让各个 agent 单独调用、各司其职

### 提取的概念

- [Hermes Agent](entities/Hermes Agent.md)

- [多 Agent 协作工作流](concepts/多 Agent 协作工作流.md)

- [SOUL.md](concepts/SOUL.md.md)

- [AGENTS.md](concepts/AGENTS.md.md)

### 原始文章信息

- 作者：@Saccc_c

- 来源：X书签

- 发布时间：2026-04-14

- 原文链接：[https://x.com/Saccc_c/status/2044018336673964207](https://x.com/Saccc_c/status/2044018336673964207)

### 个人评注

- 这套方法对 Tizer 的内容管线很有参考价值。研究、整理、发布可以拆成不同 agent，用 [AGENTS.md](http://agents.md/) 共享项目背景，再用 [SOUL.md](http://soul.md/) 约束每个 agent 的职责边界。

- 如果后续接入 OpenClaw 或 HITL 流程，这种“共享任务背景 + 独立记忆”的做法有助于降低上下文污染，提高分工、复盘和持续迭代的稳定性。
