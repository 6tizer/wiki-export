---
title: Test-time Training
type: concept
tags:
- LLM
- 记忆系统
status: 草稿
confidence: medium
last_compiled: '2026-04-13'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/0ac98d718cef4ed48e4d869cbdb09a3e
notion_id: 0ac98d71-8cef-4ed4-8e4d-869cbdb09a3e
---

### 定义

Test-time Training 指模型在推理阶段或接近推理阶段，通过额外适配、更新或局部学习过程来提升当前任务表现的一类方法。

### 关键要点

- 文中将它列为与 continual learning 边界相互纠缠的一组相关概念之一。

- 它体现了“模型在使用过程中继续学习”的直觉，但并不等于持续学习的全部。

- 在工程实践里，这类能力通常会带来安全、可观测性与合规复杂度。

### 来源引用

- 《前两天看到 Dario Amodei 在一个采访里说，continual learning已经 solved 了。》｜X书签｜2026/04/12｜主链接：[X 原文](https://x.com/AI_Whisper_X/status/2043279143496769940)｜源页面：Continual Learning 究竟有没有被「解决」？Dario 与蔡天乐的框架之争

### 关联概念

- 与 Continual Learning、Agentic Context Management 一起构成“模型能否在运行中继续扩展能力”的讨论范围。
