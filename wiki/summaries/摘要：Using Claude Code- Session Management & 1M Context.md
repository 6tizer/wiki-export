---
title: '摘要：Using Claude Code: Session Management & 1M Context'
type: summary
tags: []
status: 已审核
confidence: high
last_compiled: '2026-04-16'
source_tags: ''
source_article_url: https://www.notion.so/344701074b68817d8ebce127c9a648a3
notion_url: https://www.notion.so/Tizer/072d72417f1843088024c0facd1557d0
notion_id: 072d7241-7f18-4308-8024-c0facd1557d0
---

## 一句话摘要

这篇文章系统解释了在 Claude Code 的 1M 上下文时代，为什么“继续对话、回退、开新会话、压缩上下文、调用子代理”本质上都是会话管理决策，以及这些决策如何直接影响长任务的稳定性与质量。

## 关键洞察

- 1M 上下文窗口虽然延长了 Claude Code 的连续自治能力，但也放大了上下文污染带来的副作用

- **Context Rot** 往往会先于硬性窗口上限出现，因此“还没满”并不等于“状态还好”

- **Rewind** 往往比在错误路径上继续修补更有效，因为它能直接丢弃失败分支的噪声

- **Context Compaction** 与开新会话并不等价，前者是模型主导的有损摘要，后者是用户主导的干净重启

- **Subagents** 的价值不只是并行处理，更在于把高噪声中间过程隔离在独立上下文里

## 提取的概念

- [Claude Code](entities/Claude Code.md)

- [Claude Code 上下文管理](concepts/Claude Code 上下文管理.md)

- [Context Rot](concepts/Context Rot.md)

- [Context Compaction](concepts/Context Compaction.md)

- [Rewind](concepts/Rewind.md)

- [Subagents 并行](concepts/Subagents 并行.md)

## 原始文章信息

- 作者：@trq212

- 来源：X书签

- 发布时间：2026/04/15

- 原文链接：[https://x.com/trq212/status/2044548257058328723](https://x.com/trq212/status/2044548257058328723)

## 个人评注

- 对 Tizer 当前的 HITL 与内容编译流程很有参考价值。长链路任务不应该默认一直续写，而应在任务切换、分支失败或上下文膨胀时主动做回退、摘要交接或上下文重置。

- 如果后续把 Wiki 编译、资料整理、内容改写和多 Agent 协作串成一条流水线，这套“错误分支及时切断 + 中间产物外置 + 子任务隔离上下文”的方法，可以明显降低长任务中的降智与噪声累积。
