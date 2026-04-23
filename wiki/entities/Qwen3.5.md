---
title: Qwen3.5
type: entity
tags:
- LLM
- 多模态
- Agent 技能
status: 审核中
confidence: high
last_compiled: '2026-04-23'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/9ca4df1f0e36481893c1234787ee2fa0
notion_id: 9ca4df1f-0e36-4818-93c1-234787ee2fa0
---

## 定义

Qwen3.5 是阿里通义实验室发布的开源大模型，采用 MoE + 线性注意力混合架构（397B 总参 / 17B 激活），具备原生多模态能力和 Agent 能力，支持 201 种语言。

## 核心要点

- MoE 架构：397B 总参但仅激活 17B，256K 上下文下解码吞吐量是 Qwen3-Max 的 19 倍

- 原生多模态：无需外挂视觉编码器，天生能看懂像素，支持 1M token 上下文

- Agent 能力：边思考、边搜索、边调用工具，可操作电脑/手机界面

- 201 种语言：词表 25 万，编码/解码效率提升 10-60%

- 性能超越 Qwen3-Max、Gemini-3-Pro、GPT-5.2

## 本地运行

推荐通过 **LM Studio**（图形界面）或 **Ollama**（命令行）在 Apple Silicon Mac 上运行，MLX 加速后性能较好。Qwen3.5-35B-A3B 4-bit 量化后约 20GB，可运行在 32GB 统一内存 Mac Mini 上。

## 典型应用

与 OpenClaw 配合使用时作为内部“肌肉”负责执行层任务（占 API 消耗的 90%），前沿模型负责规划层（占 10%）——大幅降低 API 费用。

## 来源引用

- [摘要：quantization](summaries/摘要：quantization.md)（[原文](https://x.com/leftcurvedev_/status/2044700338817564814)）

- [摘要：Qwen3.5 开源多模态大模型](summaries/摘要：Qwen3.5 开源多模态大模型.md)（开源星探，2026-02-17）

  - GitHub: [https://github.com/QwenLM/Qwen3.5](https://github.com/QwenLM/Qwen3.5)

- [摘要：OpenClaw + 本地模型：用 Mac Mini 打造零成本、无限量的私人 AI 智能体](summaries/摘要：OpenClaw + 本地模型：用 Mac Mini 打造零成本、无限量的私人 AI 智能体.md)

## 关联概念

- [GLM-5.1](entities/GLM-5.1.md)

- [模型蒸馏](concepts/模型蒸馏.md)

- [模型量化](concepts/模型量化.md)

- [GGUF](concepts/GGUF.md)

- [MLX 框架](entities/MLX 框架.md)

- [Qwen3.5-9B-GLM5.1-Distill-v1](entities/Qwen3.5-9B-GLM5.1-Distill-v1.md)
