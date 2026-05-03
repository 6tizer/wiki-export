---
title: 摘要：How to cut Claude Code costs by 3x (using Karpathy's context engineering
  principles)
type: summary
tags:
- 上下文管理
- MCP 协议
- 加密资产
status: 已审核
confidence: high
last_compiled: '2026-04-23'
source_tags: ''
source_article_url: https://www.notion.so/34b701074b688157bc39c058f210648c
notion_url: https://www.notion.so/Tizer/427638587db747e1a8e9784a98b318b2
notion_id: 42763858-7db7-47e1-a8e9-784a98b318b2
---

## 一句话摘要

这篇文章通过 Supabase 与 InsForge 的并行实测指出：决定 Claude Code 成本的往往不是模型本身，而是后端是否以适合 Agent 的方式提供文档、状态与错误上下文。

## 关键洞察

- 更强的模型不会自动弥补缺失上下文，反而会因为更深入地探索、重试和推理而放大 Token 消耗。

- Supabase MCP 的主要成本黑洞来自三类问题：文档返回过宽、后端状态可见性碎片化、错误上下文缺乏结构化信号。

- InsForge 把 Skills、CLI 与 MCP 分层使用：静态知识走 Skills，执行操作走 CLI，动态状态检查才走 MCP，因此显著减少无效往返。

- 文中用同一个 DocuRAG 项目对比两套后端，Supabase 会话消耗 10.4M tokens，而 InsForge 仅消耗 3.7M tokens，核心差异来自调试回路与上下文设计。

- 所谓后端层的 context engineering，本质是把 Agent 需要的结构化状态、可执行接口与诊断线索，在任务开始前就准备好。

## 提取的概念

- [Context Engineering](concepts/Context Engineering.md)

- [Claude Code](entities/Claude Code.md)

- [InsForge](entities/InsForge.md)

- [Supabase](entities/Supabase.md)

- [Backend Context Engineering](concepts/Backend Context Engineering.md)

- [渐进式披露](concepts/渐进式披露.md)

## 原始文章信息

- 作者：@_avichawla

- 来源：X书签

- 发布时间：2026-04-21

- 原文链接：[https://x.com/_avichawla/status/2046500537584218438](https://x.com/_avichawla/status/2046500537584218438)

## 个人评注

这篇文章对 Tizer 的启发很直接：如果要把内容编译、知识沉淀、代码工作流或 Agent 自动化做成稳定流水线，优化重点不能只放在 prompt 和模型选型上，还要把工具描述、运行时状态、错误反馈与知识入口做成更适合 Agent 消费的结构化上下文。
