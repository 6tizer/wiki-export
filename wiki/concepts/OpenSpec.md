---
title: OpenSpec
type: concept
tags:
- Coding Agent
status: 审核中
confidence: high
last_compiled: '2026-04-22'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/ccf2a761ab13419681d07eaa48c08637
notion_id: ccf2a761-ab13-4196-81d0-7eaa48c08637
---

## 定义

OpenSpec 是 Fission AI 推出的轻量级 Spec-Driven Development 框架，核心概念是 **Delta Spec**——增量规格文档，每次需求变更只描述 ADDED / MODIFIED / REMOVED 的部分，而非完整重写。

## 关键要点

- 用三个标签标记变动：ADDED（新增）、MODIFIED（修改）、REMOVED（移除）

- Token 消耗仅为 Spec Kit 的约三分之一

- 适合已有项目的日常迭代开发

- 不适合从零开始的新项目（缺少全景设计）

- 注意区分 Delta Spec（单次变更说明）和 Memory Bank（跨会话上下文记忆），两者解决不同问题

## 来源引用

- [摘要：AI开发范式——Spec Kit、OpenSpec、BMAD 全解析](summaries/摘要：AI开发范式——Spec Kit、OpenSpec、BMAD 全解析.md)（娄晨，2026-03-03）— 对比 OpenSpec 与 Spec Kit、BMAD 的适用场景
