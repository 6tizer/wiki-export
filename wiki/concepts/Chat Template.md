---
title: Chat Template
type: concept
tags:
- LLM
- Agent 技能
status: 审核中
confidence: high
last_compiled: '2026-04-16'
source_tags: LLM, Agent, 开发者工具
source_article_url: ''
notion_url: https://www.notion.so/3c2ff03b613a4d1fb649c9101acccfae
notion_id: 3c2ff03b-613a-4d1f-b649-c9101acccfae
---

## 定义

Chat Template 是将多轮消息、系统提示、工具调用结果等结构化对话数据渲染为模型最终 prompt 的模板层，也是模型、推理框架与客户端之间的重要协议边界。

## 关键要点

- 它不仅决定 prompt 长什么样，也决定 tool message、system prompt、assistant turn 等结构能否被模型正确理解

- 一旦模板对消息格式的假设过窄，就可能出现工具结果丢失、上下文失真或循环调用等问题

- 本文案例中，GLM-5.1 的旧模板只接受 string 形式的工具结果，无法兼容 vLLM 转换后的 array parts

## 来源引用

- [原文链接](https://x.com/Zai_org/status/2044741938604093443)｜《GLM-5.1 的 Tool Calling 循环死锁：一个 Chat Template 引发的「幽灵 Bug」》｜源文章：GLM-5.1 的 Tool Calling 循环死锁：一个 Chat Template 引发的「幽灵 Bug」

## 关联概念

- [GLM-5.1](entities/GLM-5.1.md)

- [Tool Calling](concepts/Tool Calling.md)
