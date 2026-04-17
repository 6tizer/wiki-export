---
title: SGLang
type: entity
tags:
- LLM
- 开发工具
status: 草稿
confidence: medium
last_compiled: '2026-04-16'
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

- [原文链接](https://x.com/Zai_org/status/2044741938604093443)｜《GLM-5.1 的 Tool Calling 循环死锁：一个 Chat Template 引发的「幽灵 Bug」》｜源文章：GLM-5.1 的 Tool Calling 循环死锁：一个 Chat Template 引发的「幽灵 Bug」

## 关联概念

- [GLM-5.1](entities/GLM-5.1.md)

- [Tool Calling](concepts/Tool Calling.md)
