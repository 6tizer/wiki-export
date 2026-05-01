---
title: Prompt Hooks
type: concept
tags:
- Agent 安全
- 提示工程
status: 审核中
confidence: high
last_compiled: '2026-04-18'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/9e465bb7b8a9491b89a4e6e0f1adf696
notion_id: 9e465bb7-b8a9-491b-89a4-e6e0f1adf696
---

## 定义

Prompt Hooks 是 Claude Code Hooks 中让模型额外做一次判断的执行类型，适用于“是否安全”“是否应放行”这类难以用硬规则完全覆盖的主观决策。

## 核心要点

- 适合数据库迁移风险、代码安全性等需要语义判断的场景。

- 每触发一次都相当于额外进行一次模型调用，因此延迟和成本高于 Command Hooks。

- 它弥补了纯规则系统的刚性，但不适合放在所有高频热路径里滥用。

## 来源引用

- [摘要：打造可靠的 AI 编程环境：Claude Code Hooks 完整开发者指南](summaries/摘要：打造可靠的 AI 编程环境：Claude Code Hooks 完整开发者指南.md)（[原文](https://mp.weixin.qq.com/s?__biz=MjM5NzA1NzMyOQ%3D%3D&mid=2247486947&idx=1&sn=92ca2b4f44cadd181eb6b40087a2531b&chksm=a7e11bb1d385c29bce1587e79207574fba3835086a7fbed287fbf12e86194e37111fb2982d78#rd)）

## 关联概念

- [Claude Code Hooks](concepts/Claude Code Hooks.md)

- [Agent Hooks](concepts/Agent Hooks.md)

- [PreToolUse](concepts/PreToolUse.md)
