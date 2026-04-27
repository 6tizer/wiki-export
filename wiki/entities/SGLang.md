---
title: SGLang
type: entity
tags:
- 推理优化
- Agent 协作模式
- 上下文管理
status: 审核中
confidence: medium
last_compiled: '2026-04-27'
source_tags: LLM, Agent, 开发者工具
source_article_url: ''
notion_url: https://www.notion.so/cb98fe3986d346249db65a05315dfd9d
notion_id: cb98fe39-86d3-4624-9db6-5a05315dfd9d
---

## 定义

SGLang 是面向大模型推理与多轮交互优化的服务框架，强调高吞吐、前缀缓存复用与 Agent 场景下的推理效率。

## 关键要点

- 适合多轮对话和长链路 Agent 任务

- 与 GLM-5.1 结合时，同样会受到 chat template 兼容问题影响

- 这说明本文中的死循环根因不在具体推理框架，而在消息渲染契约本身

## 来源引用

- [摘要：Qwen3.6 35B-A3B dropped yesterday, so I ran it on 4 GPUs to see how it performs:](summaries/摘要：Qwen3.6 35B-A3B dropped yesterday, so I ran it on 4 GPUs to see how it performs-.md)（[原文](https://x.com/stevibe/status/2045087373516492954)）

- [原文链接](https://x.com/Zai_org/status/2044741938604093443)｜[摘要：GLM-5.1 的 Tool Calling 循环死锁：一个 Chat Template 引发的「幽灵 Bug」](summaries/摘要：GLM-5.1 的 Tool Calling 循环死锁：一个 Chat Template 引发的「幽灵 Bug」.md)｜源文章：GLM-5.1 的 Tool Calling 循环死锁：一个 Chat Template 引发的「幽灵 Bug」

## 关联概念

- [Qwen3.6-35B-A3B](entities/Qwen3.6-35B-A3B.md)

- [GLM-5.1](entities/GLM-5.1.md)

- [Tool Calling](concepts/Tool Calling.md)
