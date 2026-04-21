---
title: Step 3.5 Flash
type: concept
tags:
- LLM
status: 审核中
confidence: medium
last_compiled: '2026-04-21'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/5eea43dcf716477db20930ea6ebfe708
notion_id: 5eea43dc-f716-477d-b209-30ea6ebfe708
---

## 定义

Step 3.5 Flash 是阶跃星辰（StepFun）发布的大语言模型，采用约 196B MoE 架构，专为 Agent 时代的极速推理和本地部署优化。

## 关键要点

- 约 196B 参数 MoE 架构，4-bit 量化后完美适配 128GB 内存

- 设计目标三个词：强逻辑、长上下文、快

- 在 OpenRouter 上调用量跻身全球第四，完全靠开发者自发选择

- 采用 SWA 结构（对投机采样最友好）+ 8 Group（适配 8 卡并行）

- 团队核心观点：模型尺寸到一定程度后，逻辑能力主要靠后训练技术

- 在 Reddit r/LocalLLaMA 进行了长达数小时的 AMA

## 来源引用

- [摘要：OpenClaw杀出中国黑马——Step 3.5 Flash 与 Agent 时代](summaries/摘要：OpenClaw杀出中国黑马——Step 3.5 Flash 与 Agent 时代.md)（新智元，2026-02-28）
