---
title: 摘要：OpenAI Codex CLI 实用最佳实践
type: summary
tags:
- CLI 工具
- 代码生成
- 推理优化
status: 已审核
confidence: medium
last_compiled: '2026-04-11'
source_tags: Codex, 教程/实战, 经验分享
source_article_url: ''
notion_url: https://www.notion.so/Tizer/034916f4979b4c8b825b0449c81cccb8
notion_id: 034916f4-979b-4c8b-825b-0449c81cccb8
---

**一句话摘要**：Codex CLI 的最佳实践核心是"最小干预"原则：[AGENTS.md](http://agents.md/) 手动维护策略而非细节，模型按"难度×成本×长度"三维选择，Token 精准管理，强弱模型分阶段使用。

**关键洞察**

- [AGENTS.md](http://agents.md/) 是手动维护的 AI 行为策略文件，应聚焦策略/优先级/约束，而非逐步操作；过度定制会引入副作用

- 模型选择三维公式：高难度推理用最强推理模型，机械性工作用小型高性价比模型，长上下文用大窗口模型

- 按阶段锁定模型（设计→实现→验证），确保可复现性

- Token 管理：用 `rg` 精准定位代码，分段读取不超过 250 行，跨轮次传递关键假设摘要而非完整历史

- 成本优化：决策用强模型，执行用弱模型；先本地验证再扩大范围

**提取的概念**

- [AGENTS.md](concepts/AGENTS.md.md)（Codex CLI 行为策略配置文件）

- Codex（已有词条）

**原始文章信息**

- 作者：AI 启蒙小伙伴

- 来源：微信公众号

- 发布时间：2026-03-17

- 链接：[https://mp.weixin.qq.com/s?__biz=MzkwNDExODE4Nw==&mid=2247495476&idx=1&sn=07f2ff0438d508a3956445fe724fbedd](https://mp.weixin.qq.com/s?__biz=MzkwNDExODE4Nw%3D%3D&mid=2247495476&idx=1&sn=07f2ff0438d508a3956445fe724fbedd)

**个人评注**

与 HITL 工作流密切相关——强弱模型分阶段使用的策略，可以直接应用于 OpenClaw 的 Skill 设计中，在决策节点用强模型、执行节点用弱模型，有效降低成本。
