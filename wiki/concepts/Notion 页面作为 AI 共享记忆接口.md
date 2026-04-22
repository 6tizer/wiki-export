---
title: Notion 页面作为 AI 共享记忆接口
type: concept
tags:
- 知识管理
- Agent 编排
status: 草稿
confidence: high
last_compiled: '2026-04-13'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/de0aaabaa75341e3bddd3c17fda77c9c
notion_id: de0aaaba-a753-41e3-bddd-3c17fda77c9c
---

## 定义

利用 Notion 页面作为 AI 对话窗口之间的持久化共享状态，弥补 AI 没有跨窗口记忆的根本缺陷。页面充当「外部记忆」角色，让不同 AI 实例能读写同一份结构化状态。

## 关键要点

- **两种应用模式**：

  - **跨窗口协作**（计划文档接力）：窗口 A 规划并写入计划页面 → 窗口 B 读取并执行 → 窗口 A 验证结果

  - **技能页面模式**（工具手册）：把 MCP 工具的调用方法、参数和使用场景写成技能页，AI 自动读取并遵循

- **核心价值**：把 AI 的短期记忆变成长期记忆，一次编写永久生效

- **结构化页面 > 口头交代**：执行清单、before/after 表格、mermaid 图比自然语言描述更精确

- **三角验证**：规划者、执行者、验证者分离，减少单窗口盲区

## 实践案例

- Untitled：把 5 个 MCP 工具的调用方法写成技能页，每次新对话自动继承

- [系统重设计方案：状态体系 + Dashboard V2](syntheses/系统重设计方案：状态体系 + Dashboard V2.md)：窗口 A 规划了完整方案 → 窗口 B 执行 Phase 1-3 → 窗口 A 检查结果

## 关联概念

- [Karpathy LLM Wiki 方法论](concepts/Karpathy LLM Wiki 方法论.md)：同样强调「用结构化文档作为 AI 的外部记忆」

## 来源引用

- Tizer Luo 与 Notion AI 的实践对话（2026-04-12/13）—— 在知识 Wiki 系统升级过程中发现并验证的工作模式
