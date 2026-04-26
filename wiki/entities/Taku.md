---
title: Taku
type: entity
tags:
- Agent 框架
status: 审核中
confidence: medium
last_compiled: '2026-04-11'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/d6b7705aa0ea4fe98a2a2b5076f60a57
notion_id: d6b7705a-a0ea-4fe9-8a2a-2b5076f60a57
---

## 定义

Taku 是一个早期阶段的多应用后端互通 Harness 平台，通过三层架构将开发、运行、串联、分发整合为完整闭环，实现不同生成物（Agent、工具、纯软件脚本）之间的自主协作。

## 三层 Harness 架构

**第一层：Runtime**

- 生成完直接运行，不需要部署配环境

- 原子化拼装：把 A 软件的 AI 能力拔出来，嵌入到 B 软件中

**第二层：统一后端通讯协议**

- 所有在 Taku 生态内的生成物（Multi-agent、纯软件脚本、AI Skill）共享同一套 Agent 接口

- 主 Agent 可无缝调用任何工具的后端，无需手动配接口

**第三层：跨应用 context 和记忆共享**

- 在一个应用积累的数据和使用习惯，自动同步给所有相关应用

- 系统自主识别关联，自动更新所有相关 Agent 和应用

## 核心洞察

- **开发者 vs 普通人的需求反转**：Claude Code 默认项目隔离（对开发者合理），普通人想要的恰恰是默认打通

- **知识稀缺而非代码稀缺**：代码可以原子化分发 + 按次付费，稀缺的是背后的专业知识

## 和 OpenClaw 的差异

- OpenClaw：每个项目的记忆是孤立的

- Taku：不同应用之间后端互通、context 自动同步

## 典型场景

- 将纯量化脚本和 AI Hedge Fund（Multi-agent）一句话串联

- 将 FlashCut 的 AI 视频生成能力嵌入 OpenCut（无 AI 的开源剪辑工具）

## 当前状态

- 测试阶段，需申请 waiting list

- 尚未融资，团队规模小

## 来源引用

- 摘要：昆仑万维连发3个王炸模型，亮出2026年AGI战略（Taku 团队对话来源）
