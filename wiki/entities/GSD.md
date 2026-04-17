---
title: GSD
type: entity
tags:
- Coding Agent
- 工作流
status: 草稿
confidence: medium
last_compiled: '2026-04-16'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/81316188dee44e678458b7fd25d1a2eb
notion_id: 81316188-dee4-4e67-8458-b7fd25d1a2eb
---

## 定义

GSD（get-shit-done）是一套面向 Claude Code 等 AI 编程工具的工程化工作流系统，核心目标是通过阶段化流程、质量门禁与上下文管理机制，降低 AI 编程过程中的 Context Rot。

## 关键要点

- 以 `/gsd-new-project`、`/gsd-plan-phase`、`/gsd-execute-phase`、`/gsd-verify-work`、`/gsd-ship` 等命令组织从需求到 PR 的完整流程

- 核心价值不是“更会聊天”，而是让 AI 编程过程更稳定、更可追踪、更可验收

- 通过 Schema drift detection、Security enforcement、Scope reduction detection 等门禁，提前拦截输出跑偏

- 兼容 Claude Code、Cursor、Codex、Gemini CLI、Trae 等多种 AI 编程环境

## 来源引用

- [原文链接](https://mp.weixin.qq.com/s?__biz=Mzk0MjcxOTM2Nw%3D%3D&mid=2247502908&idx=1&sn=781cf89e36526cf2ced56337406ae43c&chksm=c2ee5c17dbde042bf7dbe3e5b84da84512262606a3d3b9259740ab2613aab4fcde99397b23c2#rd)｜《GSD框架解析：解决AI编程工具Context Rot的工程化方案》｜源文章：GSD框架解析：解决AI编程工具Context Rot的工程化方案
