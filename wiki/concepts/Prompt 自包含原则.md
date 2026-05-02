---
title: Prompt 自包含原则
type: concept
tags:
- 内容自动化
- 提示工程
status: 草稿
confidence: medium
last_compiled: '2026-05-02'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/9e0f95bcb8604800922e3e1ab2fbb34a
notion_id: 9e0f95bc-b860-4800-922e-3e1ab2fbb34a
---

## 定义

Prompt 自包含原则指在自动化/定时任务场景中，每条 Prompt 必须携带完成任务所需的全部上下文信息（目标、数据源地址、输出格式、通知渠道等），不依赖对话历史或外部会话状态。

## 关键要点

- 定时任务（Cron Job）执行时无对话上下文，Agent 只能看到 Prompt 本身

- Prompt 必须包含：操作目标（如仓库地址）、具体步骤、输出格式、通知渠道

- 违反此原则的常见表现：在 Prompt 中使用指代词（如「那个仓库」「上次的报告」）

- 测试方法：先在普通对话中执行完整 Prompt，确认输出符合预期后再放入 Cron

- 同样适用于异步 Agent 任务、Webhook 回调等无状态执行场景

## 来源引用

- [摘要：手把手配 3 个实用 Hermes 定时任务](summaries/摘要：手把手配 3 个实用 Hermes 定时任务.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzI3NjE4OTAyMg%3D%3D&mid=2247488709&idx=1&sn=e97ce62f2ff99e390c8fe93ad45c9413&chksm=ea0a5ab955dc7bb8b88b30460b5318465cae31892d997d3ffd88defb44bcd9dbdcc620ef7241#rd)）

## 关联概念

- [Hermes Agent](entities/Hermes Agent.md)

- [Cron 自动化](concepts/Cron 自动化.md)

- [自然语言定时任务](concepts/自然语言定时任务.md)
