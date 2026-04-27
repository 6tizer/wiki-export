---
title: 摘要：Managed Agents > Memory stores
type: summary
tags:
- 长期记忆
- Harness 工程
- AI 产品
status: 已审核
confidence: medium
last_compiled: '2026-04-27'
source_tags: Agent, LLM, Claude, 记忆
source_article_url: https://www.notion.so/34f701074b6881f28595cd70fd7e5bca
notion_url: https://www.notion.so/Tizer/0e92c3291690450db2e6598d06593f2e
notion_id: 0e92c329-1690-450d-b2e6-598d06593f2e
---

## 一句话摘要

Anthropic 宣布 Claude Managed Agents 的 Memory stores 功能进入公开测试，Agent 可基于文件系统的记忆层跨会话持续学习。

## 关键洞察

- **Memory 进入 Public Beta**：Claude Managed Agents 新增持久化记忆层，Agent 能从每次会话中学习并在后续会话复用

- **文件系统架构**：记忆基于文件系统实现，Agent 复用已有的 bash/代码执行工具读写记忆，无需独立检索栈

- **作用域隔离**：记忆按 session + agent 维度默认隔离，跨 Agent 共享需严格权限控制

- **企业级审计**：支持 scoped permissions + 完整审计日志 + 回滚，满足生产环境合规需求（Netflix 已在使用）

- **Provenance 挑战**：社区讨论指出记忆条目缺乏决策时间戳时，过时信息可能被当作权威信息复用，记忆放大错误的风险需要关注

## 提取的概念

- [Claude Managed Agents](entities/Claude Managed Agents.md)

- [持久化跨会话记忆](concepts/持久化跨会话记忆.md)

- [文件系统记忆架构](concepts/文件系统记忆架构.md)

## 原始文章信息

- **作者**：@claudeai

- **来源**：X 书签

- **发布时间**：2026-04-23

- **原文链接**：[https://x.com/claudeai/status/2047421844311949513](https://x.com/claudeai/status/2047421844311949513)

## 个人评注

这是 Anthropic 在 Agent 基础设施上的又一步棋——将记忆层托管到平台内部。从 Tizer 的视角看：

- **Memory Lock-in 风险加深**：与 Harrison Chase 之前警告的一致，记忆存在平台侧意味着迁移成本更高

- **OpenClaw 启示**：文件系统记忆架构的思路值得 OpenClaw 的 Dreaming 模块参考——用文件读写而非专用 API 管理记忆，降低耦合度

- **内容管道适用性**：对于 Wiki Compiler 这样的编译型 Agent，跨会话记忆可用于记住已编译条目的模式和偏好，提升一致性
