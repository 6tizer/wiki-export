---
title: Agent-first 架构
type: concept
tags: []
status: 审核中
confidence: high
last_compiled: '2026-04-20'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/ae7df4889be443aa80242347ec1501c5
notion_id: ae7df488-9be4-43aa-8024-2347ec1501c5
---

## 定义

Agent-first 架构是指把 AI 编码助手本身作为工作流的主编排器，由 Agent 读取清单、调用工具、执行自检、管理状态，并在关键节点请求人工确认，而不是依赖一段写死的代码编排器。

## 关键要点

- 编排逻辑主要写在 YAML 清单与 Markdown 技能文件里，而不是硬编码在单一程序里

- Agent 既负责调用工具，也负责阅读规则、做阶段决策与执行质量检查

- 这种架构让视频生产流程更容易被审计、修改和复用

- 它特别适合需要多阶段、多工具、带人工审批的复杂生产任务

## 来源引用

- [摘要：Cognition 用 $250M 抄底 Windsurf：当 IDE 变成 Agent 指挥中心，谁来审这些代码？](summaries/摘要：Cognition 用 $250M 抄底 Windsurf：当 IDE 变成 Agent 指挥中心，谁来审这些代码？.md)（[原文](https://x.com/aakashgupta/status/2044619554706604356)）

- 源文章：OpenMontage：用 AI 编程助手当导演，$0.69 拍一条完整产品广告｜原帖：[https://x.com/heygurisingh/status/2042811095703031969](https://x.com/heygurisingh/status/2042811095703031969)

- [摘要：Intercom 如何用 Claude Code 实现研发效率 3 倍提升：一份来自真实大厂的完整账单](summaries/摘要：Intercom 如何用 Claude Code 实现研发效率 3 倍提升：一份来自真实大厂的完整账单.md)（[原文](https://x.com/darraghcurran/status/2044847768313987522)）
