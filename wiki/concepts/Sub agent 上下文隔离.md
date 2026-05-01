---
title: Sub agent 上下文隔离
type: concept
tags:
- 多Agent协作
- 上下文管理
status: 审核中
confidence: high
last_compiled: '2026-04-30'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/eabdce1ef9de4f4c852d11bad9ee6ad4
notion_id: eabdce1e-f9de-4f4c-852d-11bad9ee6ad4
---

## 定义

通过子线程或子 Agent 承担检索、试错和工具调用，让这些中间过程停留在独立 context 中，主线程只接收最终结论。

## 关键要点

- 隔离的不是任务本身，而是中间噪音、原始检索结果和临时试验。

- 子线程边界能降低主对话被大段资料污染的风险。

- 这种方式天然支持并行查询、失败隔离和后端替换。

- 在 Notion AI 中，`createAndRunThread` 是实现该模式的核心能力之一。

## 来源引用

- [摘要：Notion AI × Sub Agent：把检索隔离写进长期指令的实战](summaries/摘要：Notion AI × Sub Agent：把检索隔离写进长期指令的实战.md)（[原始对话](https://www.notion.so/)）

- [摘要：A new way to think about composing skills to increase leverage: Skill Graphs 2.0](summaries/摘要：A new way to think about composing skills to increase leverage- Skill Graphs 2.0.md)（[原文](https://x.com/shivsakhuja/status/2047124337191444844)）

- [摘要：Keep your Claude Code context clean with Subagents](summaries/摘要：Keep your Claude Code context clean with Subagents.md)（[原文](https://x.com/dani_avila7/status/2048486242321662189)）

- [摘要：1M 上下文时代太费 Token，告诉你我的 Coding Agent 省钱方法](summaries/摘要：1M 上下文时代太费 Token，告诉你我的 Coding Agent 省钱方法.md)（[原文](https://mp.weixin.qq.com/s?__biz=MjM5ODQ2MDIyMA%3D%3D&mid=2650734353&idx=1&sn=ed1c3514623d29bffc28e1856c920dd8&chksm=bf1f3acf64e4e5b746803a7ac4aaf8bfc0f5d216e8dcbdb8f89d5f6d4d961af981b37393dba6#rd)）

- [摘要：Sub-Agents vs Agent Teams: The Architecture Decision That Changes Everything](summaries/摘要：Sub-Agents vs Agent Teams- The Architecture Decision That Changes Everything.md)（[原文](https://x.com/NainsiDwiv50980/status/2049529787300090344)）

## 关联概念

- [Skill Graph](concepts/Skill Graph.md)

- [原子-分子-化合物技能分层](concepts/原子-分子-化合物技能分层.md)

- [Brain RAM 杠杆模型](concepts/Brain RAM 杠杆模型.md)
