---
title: Gene Map
type: concept
tags:
- 记忆系统
status: 审核中
confidence: high
last_compiled: '2026-04-15'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/d4025e60abb64a0b976ab32507fa03a1
notion_id: d4025e60-abb6-4a0b-976a-b32507fa03a1
---

## 定义

Gene Map 是 Helix 中用于存储失败修复经验的本地知识库机制，会为每一次修复策略记录可随结果更新的 Q-value，用来决定下次遇到同类错误时优先采用哪种修复方案。

## 关键要点

- 把“错误 → 修复 → 结果”沉淀为结构化经验，而不是只保留日志

- 通过强化学习式打分，让成功策略被提升，失效策略被降权

- 对重复错误可跳过 LLM 诊断，直接召回已验证修复路径

- 当前版本强调本地记忆，后续愿景是跨 Agent 共享的失败免疫网络

## 来源引用

- [原文链接](https://x.com/dapanji_eth/status/2044088577773154722)｜《AI Agents Have No Memory for Failure. So We Gave Them One.》｜来源条目：Helix：给 AI Agent 装上「免疫系统」，让它记住每一次失败
