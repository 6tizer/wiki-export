---
title: Prompt Stack
type: concept
tags:
- 提示工程
- AI 设计
status: 草稿
confidence: medium
last_compiled: '2026-05-02'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/6afdfa7297b94e48b2651b4b6cf2055d
notion_id: 6afdfa72-97b9-4e48-b265-1b4b6cf2055d
---

## 定义

Prompt Stack（提示词堆栈）是一种三层结构化提示词组装模式，用于将系统级指令、设计规范和任务工作流分层注入 AI Agent 的上下文中。该模式在 Open Design 项目中被用于控制 AI 设计生成的质量和一致性。

## 关键要点

- **三层结构**：

  1. 基础系统提示词（System Prompt）——通用规则和约束

  1. Design System 内容——当前选定的视觉规范（配色、字体、布局等）

  1. Skill 工作流——当前任务的具体执行流程和结构要求

- Agent 按 Skill 声明的 `od.design_system.sections` 字段，只读取 Design System 中需要的 Section，节省 token 消耗

- 与 Anti-AI-Slop 机制配合，在 Prompt Stack 中硬编码质量规则（如 RULE 1：首轮必须返回 Discovery Form）

- 这种分层架构使得 Skill × Design System 可自由组合，理论组合超过 1,300 种

## 关联概念

- [Open Design](entities/Open Design-49d51ec0.md)

- [Anti-AI-Slop](concepts/Anti-AI-Slop.md)

- [DESIGN.md](concepts/DESIGN.md.md)

## 来源引用

- [摘要：Open Design开源AI设计平台操作指南](summaries/摘要：Open Design开源AI设计平台操作指南.md)（[原文](https://mp.weixin.qq.com/s?__biz=Mzg2MjIwODc3Mw%3D%3D&mid=2247518546&idx=1&sn=b7e340057327e37eaa414da8f73f2c54&chksm=cf03bb2e5e663169f8ac4d30e861142ad85293ab74b7795fb00b0d259549bef37aa984e1a38e#rd)）
