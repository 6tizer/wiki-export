---
title: 摘要：The harness as the context manager
type: summary
tags:
- Harness 工程
- 上下文管理
- AI 产品
status: 已审核
confidence: high
last_compiled: '2026-04-30'
source_tags: ''
source_article_url: https://www.notion.so/352701074b68815885b0dad3ec8f7fe4
notion_url: https://www.notion.so/Tizer/8a8acd17d46b41799c90dd9cbc6b752f
notion_id: 8a8acd17-d46b-4179-9c90-dd9cbc6b752f
---

## 一句话摘要

Harness 的本质是分布式上下文管理系统——通过 PTC 沙箱执行、Sub-agent 上下文隔离、Compaction 状态压缩和搜索优先技能发现四种机制，解决长时程 Agent 的上下文膨胀问题。

## 关键洞察

- **性能增量来自 Harness 而非模型**：LangChain 仅靠 Harness 改进就在 Terminal-Bench 上提升 +13.7 分（模型不变）；Vercel 砍掉 80% 工具后可靠性更高、延迟降低 3.5x

- **Harness 重构的根因是工作量增长**：不仅是模型变强，而是我们给 Agent 布置了更多多步骤任务，每次工具调用、搜索结果和执行输出都在扩大上下文窗口

- **Programmatic Tool Calling (PTC) 取代对话式调用**：将工作流逻辑移入沙箱代码，20+ 次工具调用可在单次运行中完成，编排器只看摘要

- **Sub-agent 实现空间维度的上下文隔离**：编排 Agent 通过代码启动并行子 Agent，每个子 Agent 拥有独立上下文窗口和 Token 预算

- **Compaction 实现时间维度的状态保留**：对话压缩保留用户意图、决策记录和后续计划；工具输出压缩将大结果写入文件系统并替换为摘要+路径

- **搜索优先的技能发现三阶段**：先搜索索引 → 看候选短列表 → 执行时才加载完整 Schema，Agent 永远不付全量浏览的上下文税

## 提取的概念

- [Programmatic Tool Calling](concepts/Programmatic Tool Calling.md)

- [Context Compaction](concepts/Context Compaction.md)

- [Subagents 并行](concepts/Subagents 并行.md)

- [Progressive Disclosure](concepts/Progressive Disclosure.md)

- [AI Harness](concepts/AI Harness.md)

- [Glean](entities/Glean.md)

## 原始文章信息

- **作者**：@tonygentilcore（Tony Gentilcore，Glean 工程负责人）

- **来源**：X 书签

- **发布时间**：2026-04-29

- **原文链接**：[X 原文](https://x.com/tonygentilcore/status/2049482833111232694)

## 个人评注

本文是 Harness 工程领域的高质量一手实践总结。Glean 从企业搜索出发将 Harness 定义为「分布式上下文管理系统」，这与 OpenClaw 的架构思路高度共鸣——OpenClaw 同样面临长时程任务中的上下文膨胀问题。PTC 模式（代码即执行原语）可直接对标 OpenClaw 的 Skill 执行环境；Compaction 策略为 HITL 流程中的断点续传提供了参考；搜索优先的技能发现模式也与知识 Wiki 的渐进式检索理念一致。值得关注 Glean 后续在 Enterprise Graph 信号排序方面的演进。
