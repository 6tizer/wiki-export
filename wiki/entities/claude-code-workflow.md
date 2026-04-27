---
title: claude-code-workflow
type: entity
tags:
- Harness 工程
- CLI 工具
status: 草稿
confidence: high
last_compiled: '2026-04-28'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/7cd777c739eb472facfc354acf22c0d2
notion_id: 7cd777c7-39eb-472f-acfc-354acf22c0d2
---

## 定义

claude-code-workflow 是由 @runes_leo（Leo）开源的 Claude Code 工作流模板，从多项目日常使用中提炼而成，涵盖记忆管理、上下文工程与任务路由。GitHub 仓库地址：[https://github.com/runesleo/claude-code-workflow（666](https://github.com/runesleo/claude-code-workflow（666) Stars）。

> 别名：Claude Code 工作流模板

## 核心架构

**三层加载架构：**

- **Layer 0（自动加载规则）**：行为规范、调试流程、触发器，始终驻留上下文（约 2K token）

- **Layer 1（按需文档）**：任务路由、安全防护、Agent 协作，需要时加载

- **Layer 2（热数据）**：当天进度、跨 session 任务状态，工作记忆

- **Layer 3（v2 新增）**：PreToolUse Hook 层，在工具调用时强制执行规则，不再依赖模型自觉

**v2 关键改进：**

- 14 条 P0 铁律、[patterns.md](http://patterns.md/) 2366 行

- PreToolUse Hook 强制拦截：规则不再是「希望你自觉」，而是「准备动手前强制注入」

- 复杂任务的计划门禁

- 强制子 Agent 分派检查清单

- 10 条 P0 规则改写为事件驱动硬规则

**包含组件：**

- 5 个实战 Skill（session-end / verification-before-completion / systematic-debugging / planning-with-files / experience-evolution）

- 3 个自定义 Agent（pr-reviewer / security-reviewer / performance-analyzer）

- 4 个 Slash Command（debug / deploy / exploration / review）

## 设计哲学

1. 结构 > 单条神 Prompt

1. 记忆 > 智商

1. 验证 > 感觉

1. 分层加载 > 平铺配置

1. 自动保存 > 靠人记得

## 关联概念

- [Claude Code Hooks](concepts/Claude Code Hooks.md)

- [L0/L1/L2 分层加载](concepts/L0-L1-L2 分层加载.md)

- [Memory Flush](concepts/Memory Flush.md)

- [完成前验证](concepts/完成前验证.md)

- [多档任务路由](concepts/多档任务路由.md)

- [SSOT 路由表](concepts/SSOT 路由表.md)

## 来源引用

- [摘要：Claude Code 工作流模板 v2](summaries/摘要：Claude Code 工作流模板 v2.md)（[原文](https://x.com/runes_leo/status/2048013195563172162)）
