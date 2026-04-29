---
title: 摘要：sentrux：一个开源的代码架构传感器，让大模型守住代码底线！
type: summary
tags:
- Harness 工程
- CLI 工具
status: 已审核
confidence: high
last_compiled: '2026-04-29'
source_tags: ''
source_article_url: https://www.notion.so/351701074b68818f96ccc7946e18f797
notion_url: https://www.notion.so/Tizer/526ac202a9df4cc49c764df11a072e40
notion_id: 526ac202-a9df-4cc4-9c76-4df11a072e40
---

## 一句话摘要

sentrux 是一个纯 Rust 开源实时架构传感器，通过可视化 + 五维指标评分 + 质量门禁 + MCP 集成，为 AI 编码 Agent 提供闭环架构质量反馈，将「失控的 AI 代码生成」转化为「受约束的架构演进」。

## 关键洞察

- **AI 编码的核心问题不是模型变差，而是项目代码架构在 Agent 高频修改下逐渐失控**——开发者无法 100% review AI 生成的代码，慢慢失去对架构的掌控

- **sentrux 的解决思路是「传感器 + 规则引擎 + 执行器」闭环**：不做更好的规划，而是提供即时的架构健康感知，让 Agent 自己感知并修正架构退化

- **五维 MADER 指标体系**（Modularity、Acyclicity、Depth、Equality、Redundancy）给出 0-10000 的连续评分，毫秒级计算，适合嵌入 Agent 工作流

- **Quality Gate 机制**可在 Agent 会话前后自动对比架构评分，捕获退化并阻止合并，类似架构层面的「单元测试」

- **通过 MCP 协议原生集成各类 AI IDE**（Claude Code、Cursor、Windsurf、Trae 等），Agent 可实时查询架构健康状态并据此调整编码行为

## 提取的概念

- [sentrux](entities/sentrux.md)

- [架构质量门禁](concepts/架构质量门禁.md)

- [Tree-sitter](entities/Tree-sitter.md)

- [MCP 协议](concepts/MCP 协议.md)

## 原始文章信息

- **作者**：AI开源提效指南

- **来源**：微信公众号

- **发布时间**：2026-04-29

- **原文链接**：[sentrux：一个开源的代码架构传感器，让大模型守住代码底线！](https://mp.weixin.qq.com/s?__biz=MzY5NzIxODM2MQ%3D%3D&mid=2247484673&idx=1&sn=9a52bf97b7c11eef0414da5f957caba2&chksm=f544a6ba6d1eae6bf4261adba920e882c604a63f51e87a21903d6ed42087d1a09eb0224e9d2d#rd)

## 个人评注

sentrux 的「传感器闭环」思路与 OpenClaw 的 Harness 工程理念高度契合——都强调对 AI Agent 输出的实时约束和质量守护。在 HITL 工作流中，sentrux 可以作为 Agent 编码阶段的架构守卫层，与代码审查形成互补。其 MCP 集成方式也值得参考：通过标准协议暴露架构健康数据，让任何支持 MCP 的 Agent 都能消费，这是典型的「工具即服务」模式。
