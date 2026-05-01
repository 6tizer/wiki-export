---
title: GGUF
type: concept
tags: []
status: 审核中
confidence: medium
last_compiled: '2026-04-23'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/635fe6e1bfdd4750b13b1c6546ace4c9
notion_id: 635fe6e1-bfdd-4750-b13b-1c6546ace4c9
---

## 定义

GGUF 是面向本地大模型推理场景的一种模型文件格式，常用于 llama.cpp、Ollama 和 LM Studio 等工具链。

## 关键要点

- 它便于发布量化后的模型版本，降低本地部署门槛

- 适合消费级显卡和桌面环境快速加载运行

- 在开源模型分发中，GGUF 已成为本地推理生态的重要标准格式

## 来源引用

- 《Qwen3.5-27B 蒸馏 Claude Opus 推理能力：在消费级显卡上跑出媲美前沿模型的推理链》｜X书签文章｜原文链接：[https://x.com/HuggingModels/status/2036707417782964396](https://x.com/HuggingModels/status/2036707417782964396)

- [原文链接](https://x.com/berryxia/status/2043918551552274690)｜《卧槽！本地 AI 又出神器了 🔥》｜源文章：SuperGemma4-26B：本地跑起来的无审查多模态神器，Mac 用户专属

- [摘要：quantization](summaries/摘要：quantization.md)（[原文](https://x.com/leftcurvedev_/status/2044700338817564814)）

- [摘要：Okay this one is insane. A new 18B frankenstein model was just released on @huggingface — Beats the new Qwen3.6-35B-A3B on a 44-test suite despite requiring 12GB VRAM instead of 24GB 🤯](summaries/摘要：Okay this one is insane. A new 18B frankenstein model was just released on @huggingface — Beats the new Qwen3.6-35B-A3B on a 44-test suite despite requiring 12GB VRAM instead of 24GB 🤯.md)（[原文](https://x.com/leftcurvedev_/status/2045449352827580602)）

- [摘要：Meet Qwen3-Coder-30B-A3B-Instruct-GGUF: a specialized 30B parameter coding assistant that's been optimized for efficiency. This model isn't just another chatbot. It's a powerhouse fine-tuned for under](summaries/摘要：Meet Qwen3-Coder-30B-A3B-Instruct-GGUF- a specialized 30B parameter coding assistant that's been optimized for efficiency. This model isn't just another chatbot. It's a powerhouse fine-tuned for under.md)（[原文](https://x.com/HuggingModels/status/2047160797911216364)）

- [摘要：Meet ruvltra-claude-code: a GGUF-quantized model that's making waves in the AI community. This isn't just another code generator. It's a self-learning, swarm-optimized system that adapts as it works.](summaries/摘要：Meet ruvltra-claude-code- a GGUF-quantized model that's making waves in the AI community. This isn't just another code generator. It's a self-learning, swarm-optimized system that adapts as it works.md)（[原文](https://x.com/HuggingModels/status/2047160797772775537)）

## 关联概念

- [Qwopus-GLM-18B-Merged-GGUF](entities/Qwopus-GLM-18B-Merged-GGUF.md)

- [模型合并](concepts/模型合并.md)

- [SuperGemma4-26B-Abliterated-Multimodal](entities/SuperGemma4-26B-Abliterated-Multimodal.md)

- [Gemma 4](entities/Gemma 4.md)

- [模型量化](concepts/模型量化.md)

- [MLX 框架](entities/MLX 框架.md)

- [Qwen3.5-9B-GLM5.1-Distill-v1](entities/Qwen3.5-9B-GLM5.1-Distill-v1.md)

- [RuvLTRA Claude Code](entities/RuvLTRA Claude Code.md)

- [llama.cpp](entities/llama.cpp.md)
