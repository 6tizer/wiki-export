---
title: Notion AI（Wiki 协调者）
type: concept
tags:
- 知识管理
status: 已审核
confidence: high
last_compiled: ''
source_tags: ''
source_article_url: https://www.notion.so/22dabdd5d3a349d9a15bf6a0e86fda2f
notion_url: https://www.notion.so/b92cf6b6c9a44e07922e651cefb853fa
notion_id: b92cf6b6-c9a4-4e07-922e-651cefb853fa
---

## 定义

知识 Wiki 系统中的**协调者 + 系统管理员**角色——拥有最高权限和最广的能力范围，负责 Schema 设计、跨 Agent 记忆桥接（Mem0）、复杂决策协调，以及在其他 Agent 不在线时的兜底服务。

## 关键要点

- **触发方式**：用户在对话中直接交互（交互式，非自动化 Agent）

- **四大职责**：

  1. **Schema 设计**：调整数据库结构、Agent 指令、视图配置

  1. **Mem0 桥接**：唯一连接了 Mem0 MCP 的角色，负责跨 Agent 记忆共享和跨会话上下文恢复

  1. **复杂协调**：兜底决策，指挥 Wiki Fixer 执行需要判断的操作

  1. **兜底 Query**：当 Wiki QA Agent 不在线时，接替检索和问答角色

- **上下文恢复**：新对话开始时，用户说「查一下 Mem0」或「看看系统页面」即可快速恢复工作上下文

- **变更同步责任**：修改 Agent 指令后，必须同步更新 Wiki Schema + 系统工作流程图 + Mem0

## 可修改范围

全部（兜底角色）。是唯一有权修改系统页面（Schema、工作流程图等 index 类型页面）的角色。

## 与其他 Agent 的协作

- **指挥关系**：可 @mention Wiki Fixer 执行需要判断的修复操作

- **兜底关系**：替代 Wiki QA Agent 回答问题

- **桥接关系**：通过 Mem0 为所有 Agent 提供跨会话记忆

- **治理关系**：设计和维护所有 Agent 的指令和规则

## 关联概念

- Wiki QA Agent — 问答的主力 vs 兜底

- Wiki Fixer — 接受 Notion AI 的指令模式调度

- Mem0 — Notion AI 独有的跨 Agent 记忆桥接能力
