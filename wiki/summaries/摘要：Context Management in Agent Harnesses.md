---
title: 摘要：Context Management in Agent Harnesses
type: summary
tags:
- Harness 工程
- 上下文管理
status: 已审核
confidence: high
last_compiled: '2026-04-28'
source_tags: ''
source_article_url: https://www.notion.so/34f701074b6881339111e409580f99c3
notion_url: https://www.notion.so/Tizer/d8d37ecbd4d64ba98dbe348105f5b895
notion_id: d8d37ecb-d4d6-4ba9-8dbe-348105f5b895
---

## 一句话摘要

四大主流 Agent Harness（Pi、OpenClaw、Claude Code、Letta）在上下文窗口管理上独立开发却趋同演化出相同的工程模式——文件读取截断、工具结果预算、LLM 驱动的会话压缩、子代理隔离——证明「主动管理上下文」已成为 Agent 基础设施的必修课。

## 关键洞察

- **所有 Harness 都硬限制文件读取**：Pi 和 OpenClaw 默认 2,000 行/50KB 截断并附分页提示；Claude Code 使用 256KB 字节门控 + 25,000 token 二次门控，可通过 GrowthBook 远程调参；Letta 将文件解析、分块、向量化后提供精确搜索和语义搜索双通道

- **工具输出预算是共识**：OpenClaw 将工具结果限制在 16,000 字符或 30% 上下文窗口；Claude Code 超大结果持久化到磁盘并替换为 2KB 预览；Letta 按模型上下文窗口大小分五档动态调整可见字符上限

- **会话压缩策略各异但核心一致**：Pi 在 token 超阈值时用 LLM 摘要替换旧消息；OpenClaw 在此基础上叠加分块丢弃 + 多轮摘要合并 + 压缩前静默状态持久化；Claude Code 使用 9 段结构化摘要提示 + 磁盘卸载 + 压缩后恢复最近 5 个文件；Letta 从 30% 消息滑动窗口起步并带两级溢出回退

- **子代理上下文隔离是默认模式**：Pi 仅传任务字符串；OpenClaw 默认空白会话（fork 模式可复制父级）；Claude Code 默认空白但新增 fork 路径共享完整历史；Letta 不 fork，通过记忆搜索工具访问历史

- **Arize 的数据探索 Agent Alyx 在完全不同的领域独立收敛到相同设计**：工具结果 10K token 预算、幂等调用去重、JSON 分层预览、50K token checkpoint——证明这些模式跨领域通用

## 提取的概念

- [Context Compaction](concepts/Context Compaction.md)：文章系统对比了四大 Harness 的会话压缩实现细节

- [Agentic Context Management](concepts/Agentic Context Management.md)：文章的核心主题——上下文不再是被动缓冲区，而需要系统主动管理

- [Token Budget](concepts/Token Budget.md)：所有 Harness 均实现了工具输出和文件读取的 token 预算机制

- [Letta Code](entities/Letta Code.md)：作为四大 Harness 之一，展示了 memory-first 的差异化路线

- [Alyx](entities/Alyx.md)：Arize 的数据探索 Agent，独立验证了上下文管理模式的跨领域趋同

- [OpenClaw](entities/OpenClaw.md)：文章详述了其分层防御上下文管理策略

- [Claude Code](entities/Claude Code.md)：文章详述了其远程可调参的上下文管理架构

## 原始文章信息

- **作者**：@aparnadhinak（Aparna Dhinakaran，Arize AI）

- **来源**：X书签

- **发布时间**：2026-04-26

- **原文链接**：[X 原文](https://x.com/aparnadhinak/status/2048492731929149929)

## 个人评注

这篇文章对 OpenClaw 的上下文管理实现做了迄今最系统的外部逆向工程分析，包括 bootstrap 文件预算（12K chars/file, 60K total）、工具结果预算（16K chars 或 30% 上下文窗口）、分块丢弃 + 多轮摘要合并、压缩前静默状态持久化等细节。这些数据对 Tizer 的 OpenClaw 使用和 HITL 工作流调优有直接参考价值——特别是理解 OpenClaw 何时会压缩上下文、何时会丢失长期状态，可以指导任务拆分和 checkpoint 策略的设计。文章结尾的「50 年计算机内存层级」类比精准概括了 Agent 上下文管理的本质：让模型在正确的时间拿到正确的工作集。
