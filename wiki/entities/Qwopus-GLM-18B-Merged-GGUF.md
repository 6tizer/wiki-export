---
title: Qwopus-GLM-18B-Merged-GGUF
type: entity
tags:
- 模型部署
- 推理优化
- 加密资产
status: 审核中
confidence: medium
last_compiled: '2026-04-20'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/93457011c3fc41c694272e9ca2978285
notion_id: 93457011-c3fc-41c6-9427-2e9ca2978285
---

## 定义

Qwopus-GLM-18B-Merged-GGUF 是一个将 Qwopus 与 GLM-5.1 推理能力合并到同一权重中的实验性 18B 本地模型，主打 12GB VRAM 可运行、较强推理表现与本地 Agent 场景适配。

## 关键要点

- 属于典型的 frankenmerge / merge model 路线，通过拼接不同模型能力来追求更高性价比

- 传播卖点是 **单张 RTX 3060 可跑**、约 9.8GB GGUF 体积，以及在若干测试中压过更大模型

- 目标能力不仅是聊天，还包括 tool calling 与 agentic reasoning 等 Agent 工作负载

- 从社区反馈看，当前稳定性仍然不足，存在乱码、循环思考与输出失真等实验性问题

## 来源引用

- [摘要：Okay this one is insane. A new 18B frankenstein model was just released on @huggingface — Beats the new Qwen3.6-35B-A3B on a 44-test suite despite requiring 12GB VRAM instead of 24GB 🤯](summaries/摘要：Okay this one is insane. A new 18B frankenstein model was just released on @huggingface — Beats the new Qwen3.6-35B-A3B on a 44-test suite despite requiring 12GB VRAM instead of 24GB 🤯.md)（[原文](https://x.com/leftcurvedev_/status/2045449352827580602)）

## 关联概念

- [模型合并](concepts/模型合并.md)

- [Agentic Reasoning](concepts/Agentic Reasoning.md)

- [GLM-5.1](entities/GLM-5.1.md)

- [Qwen3.6-35B-A3B](entities/Qwen3.6-35B-A3B.md)

- [GGUF](concepts/GGUF.md)

- [Tool Calling](concepts/Tool Calling.md)
