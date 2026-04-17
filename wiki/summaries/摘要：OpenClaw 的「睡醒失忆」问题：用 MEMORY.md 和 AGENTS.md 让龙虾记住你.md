---
title: 摘要：OpenClaw 的「睡醒失忆」问题：用 MEMORY.md 和 AGENTS.md 让龙虾记住你
type: summary
tags:
- OpenClaw
- 记忆系统
status: 已审核
confidence: high
last_compiled: '2026-04-11'
source_tags: OpenClaw, Agent, 自动化
source_article_url: https://www.notion.so/335701074b6881a3ac66ce6bbdeab9b9
notion_url: https://www.notion.so/01257919164d4acc90ffeff8d2ce26fe
notion_id: 01257919-164d-4acc-90ff-eff8d2ce26fe
---

### 一句话摘要

OpenClaw 的“失忆”并不是 bug，而是会话隔离与上下文压缩的设计结果，真正的解决方案是把关键事实和规则固化进持久化记忆文件。

### 关键洞察

- Session 重置与 /compact 压缩都会导致临时上下文中的关键信息丢失。

- [MEMORY.md](concepts/MEMORY.md.md) 负责长期记忆，[AGENTS.md](concepts/AGENTS.md.md) 负责项目规则，两者分工清晰。

- 重要约束不该只停留在聊天记录里，而应进入可读、可编辑、可版本化的文件层。

- 自动记忆能力能减轻手工维护成本，但前提仍是记忆结构被设计好。

### 提取的概念

- [OpenClaw](entities/OpenClaw.md)

- [MEMORY.md](concepts/MEMORY.md.md)

- [AGENTS.md](concepts/AGENTS.md.md)

- [Auto Memory](concepts/Auto Memory.md)

### 原始文章信息

- 作者：@YuLin807（QingYue）

- 来源：X书签

- 发布时间：未明确

- 链接：[原文链接](https://x.com/YuLin807/status/2034515832286708007)

### 个人评注

这篇内容和 Tizer 的工作流关系非常直接。无论是内容编译、HITL 规则还是 Agent 操作边界，凡是跨 session 还需要保留的，都不该只存在于上下文里，而该沉淀为显式知识资产。
