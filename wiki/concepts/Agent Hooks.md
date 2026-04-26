---
title: Agent Hooks
type: concept
tags:
- Agent 协作模式
- 多Agent协作
- 上下文管理
status: 审核中
confidence: high
last_compiled: '2026-04-18'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/e8913df93ac44af8aee0f20c86a67bc0
notion_id: e8913df9-3ac4-4af8-aee0-f20c86a67bc0
---

## 定义

Agent Hooks 是 Claude Code Hooks 中最强但也最重的一类执行方式：它会启动一个带工具能力的子 Agent，在做决定前先读取文件、搜索代码或检查项目约定。

## 核心要点

- 适合命名规范校验、复杂代码审查、项目约定核对等必须结合上下文才能判断的高风险场景。

- 相比 Command Hooks 与 Prompt Hooks，Agent Hooks 更慢、更复杂，但能获得更强的上下文感知能力。

- 它体现了“让另一个 Agent 先审，再决定是否执行”的分层治理思路。

## 来源引用

- [摘要：打造可靠的 AI 编程环境：Claude Code Hooks 完整开发者指南](summaries/摘要：打造可靠的 AI 编程环境：Claude Code Hooks 完整开发者指南.md)（[原文](https://mp.weixin.qq.com/s?__biz=MjM5NzA1NzMyOQ%3D%3D&mid=2247486947&idx=1&sn=92ca2b4f44cadd181eb6b40087a2531b&chksm=a7e11bb1d385c29bce1587e79207574fba3835086a7fbed287fbf12e86194e37111fb2982d78#rd)）

## 关联概念

- [Claude Code Hooks](concepts/Claude Code Hooks.md)

- [HTTP Hooks](concepts/HTTP Hooks.md)

- [PreToolUse](concepts/PreToolUse.md)
