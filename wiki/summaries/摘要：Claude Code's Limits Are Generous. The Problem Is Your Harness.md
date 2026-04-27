---
title: 摘要：Claude Code's Limits Are Generous. The Problem Is Your Harness.
type: summary
tags:
- Harness 工程
- 上下文管理
- 推理优化
status: 已审核
confidence: high
last_compiled: '2026-04-27'
source_tags: ''
source_article_url: https://www.notion.so/34f701074b68813099eae2bddfa58375
notion_url: https://www.notion.so/Tizer/fedbc45900d146469cb4670d6307142f
notion_id: fedbc459-00d1-4646-9cb4-670d6307142f
---

## 一句话摘要

Claude Code 的用量限额已经足够宽裕——真正消耗额度的是用户自己的 Harness 工程缺陷：缓存未命中、上下文膨胀、推理档位错配和输入格式低效。

## 关键洞察

- **Prompt Cache 是最大杠杆**：缓存读取仅为输入价格的 0.1×，但中途切换工具或模型会使缓存前缀失效、触发全量重读；会话启动时锁定工具和模型是保持 ~90% 命中率的核心纪律

- **1M 上下文是成本陷阱**：禁用 1M 上下文回退到 200K，并将 auto-compact 阈值设为 80%；在 50% 时主动 /compact、不相关工作间 /clear、走偏时 /rewind，搭配 Subagent 隔离机械任务上下文

- **Effort 分级按 prompt 而非 session 设置**：默认推理消耗约为 medium 的 2×，大多数任务用 medium 即可；xhigh 仅用于 agentic coding，max 边际收益递减

- **模型路由双层策略**：Opus 会话做主规划 + 委托，Haiku 跑机械活、Sonnet 跑限定研究；或直接路由到 OpenRouter 上的 GLM-5.1（约 Opus 1/12 成本）

- **输入格式优化**：用 agent-browser 的可访问性树替代截图（省 ~90% Token）、用 pdftotext 替代 Read 工具、用 code-review-graph 的 AST 图谱替代原始文件读取（最高 49× 节省）

## 提取的概念

- [Prompt Cache](concepts/Prompt Cache.md)

- [Claude Code 上下文管理](concepts/Claude Code 上下文管理.md)

- [Subagents 并行](concepts/Subagents 并行.md)

- [Claude Code Effort 分级](concepts/Claude Code Effort 分级.md)

- [agent-browser](entities/agent-browser.md)

- [code-review-graph](entities/code-review-graph.md)

## 原始文章信息

- **作者**：@PawelHuryn（Paweł Huryn）

- **来源**：X 书签

- **发布时间**：2026-04-25

- **原文链接**：[https://x.com/PawelHuryn/status/2048170309396926577](https://x.com/PawelHuryn/status/2048170309396926577)

## 个人评注

本文是一份系统化的 Claude Code 成本控制手册，对 Tizer 的日常 Harness 工程实践有直接参考价值。其中 Subagent 委托模式（Haiku 跑机械活、Sonnet 跑研究）与 OpenClaw 的多 Agent 编排理念高度一致；Effort 分级调控和缓存纪律可直接应用到内容编译 pipeline 中。GLM-5.1 作为 Opus 替代的路由方案也值得在低优先级批量任务中测试。
