---
title: 摘要：用 Agent 动力学，和 40 个 Agents 一起为「人 + AI」做产品｜42章经
type: summary
tags:
- Agent 协作模式
- 多Agent协作
- Harness 工程
- CLI 工具
status: 已审核
confidence: high
last_compiled: '2026-04-26'
source_tags: ''
source_article_url: https://www.notion.so/34e701074b688112b033ff1e924e734a
notion_url: https://www.notion.so/ed3633905c734a64b78b6dd2dd91e232
notion_id: ed363390-5c73-4a64-b78b-6dd2dd91e232
---

## 一句话摘要

这篇访谈系统阐述了 RC 从 Kimi CLI 到 Slock 的思路演进：CLI 只是 Agent 交互的起点，真正关键的是 harness、外部记忆与多 Agent 协作机制，而未来产品竞争会越来越转向“人 + AI”团队的组织设计。

## 关键洞察

- 面向 Agent 设计的 CLI，与传统给人用的 CLI 不同，重点在于输入输出要足够清晰、结构化、低歧义，方便模型稳定调用。

- Kimi CLI 的真正价值不止于命令行壳层，而在于其底层 local agent harness；有了这层能力，后续可以继续封装 Web UI、VS Code 扩展等不同界面。

- Slock 试图解决的不是“一个全能 Agent 替你做事”，而是“多人 + 多 Agent”如何在同一平台中沟通、分工、共享信息与沉淀长期记忆。

- 多 Agent 协作不是线性叠加生产力，而是伴随 token 成本、沟通摩擦、角色分化与组织文化形成的复杂系统，这也是 RC 所说的“Agent 动力学”。

- 在 Agent 时代，可复制和可出售的核心资产不再只是 skill 或代码，而是外部记忆、长程调教记录与渐进式披露式的知识组织方式。

## 提取的概念

- [Slock](entities/Slock.md)

- [Kimi CLI](entities/Kimi CLI.md)

- [Harness Engineering](concepts/Harness Engineering.md)

- [Multi-Agent 群聊](concepts/Multi-Agent 群聊.md)

- [Agent 动力学](concepts/Agent 动力学.md)

- [渐进式披露](concepts/渐进式披露.md)

- [外部记忆](concepts/外部记忆.md)

- [任务认领机制](concepts/任务认领机制.md)

## 原始文章信息

- 作者：42章经

- 来源：微信

- 发布时间：2026-04-26 21:01（Asia/Shanghai）

- 原文链接：[https://mp.weixin.qq.com/s?__biz=MzIyMDE5OTYyMw==&mid=2651051564&idx=1&sn=babc1b1e75b77826a63d304d33c348e0&chksm=8dd911d417729de737132383124e9f75bf193b1c2ce831b08c3e001f0552438ebac7eae45e1d#rd](https://mp.weixin.qq.com/s?__biz=MzIyMDE5OTYyMw%3D%3D&mid=2651051564&idx=1&sn=babc1b1e75b77826a63d304d33c348e0&chksm=8dd911d417729de737132383124e9f75bf193b1c2ce831b08c3e001f0552438ebac7eae45e1d#rd)

## 个人评注

这篇内容对 Tizer 当前的 OpenClaw / HITL / 内容流水线很有参考价值：它提醒我们，真正可复用的不是单次 prompt，而是 harness、外部记忆、任务认领与共享文档这些“组织层能力”。如果未来要把内容编译、知识沉淀、任务协作进一步自动化，Slock 所代表的多 Agent 协作范式值得持续跟踪。
