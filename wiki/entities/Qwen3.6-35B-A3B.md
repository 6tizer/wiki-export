---
title: Qwen3.6-35B-A3B
type: entity
tags:
- LLM
- Coding Agent
status: 草稿
confidence: high
last_compiled: '2026-04-20'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/1491972f0db242eaa1e8c04710c655ec
notion_id: 1491972f-0db2-42ea-a1e8-c04710c655ec
---

## 定义

Qwen3.6-35B-A3B 是阿里 Qwen 发布的开源稀疏 MoE 大模型，总参数 35B，推理时激活 3B，主打 Agentic Coding、多模态感知与推理，以及更低部署门槛。

## 关键要点

- 稀疏 MoE 设计，将总参数量与单次推理激活量解耦

- 官方强调其 Agentic Coding 表现可与激活规模约 10 倍的模型相比

- 支持多模态感知与推理，并提供思考 / 非思考两种模式

- 采用 Apache 2.0 许可证，适合商用部署与二次集成

- 已同步提供 Qwen Studio、Hugging Face、ModelScope 等入口

## 来源引用

- [摘要：ThinkInAI Weekly AI周刊 VOL.42 Opus 4.7 来了、Qwen 开源 35B、Agent 工具链全面升级](summaries/摘要：ThinkInAI Weekly AI周刊 VOL.42 Opus 4.7 来了、Qwen 开源 35B、Agent 工具链全面升级.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzA4ODg0NDkzOA%3D%3D&mid=2247514009&idx=1&sn=bf15a5a46c8fceb7d84d0b3760d4ade9&chksm=91d6d8d58aad639487948529ced9d124bf6b7e77e01022df6a25570b93843ec362146982cbe9#rd)）

- [摘要：Qwen3.6 35B-A3B dropped yesterday, so I ran it on 4 GPUs to see how it performs:](summaries/摘要：Qwen3.6 35B-A3B dropped yesterday, so I ran it on 4 GPUs to see how it performs-.md)（[原文](https://x.com/stevibe/status/2045087373516492954)）

- [原文链接](https://x.com/Alibaba_Qwen/status/2044768734234243427)｜《⚡ Meet Qwen3.6-35B-A3B：Now Open-Source！🚀🚀》｜源文章：Qwen3.6-35B-A3B：用3B的算力跑35B的智慧，阿里最强开源编程模型来了

- [官方博客](https://qwen.ai/blog?id=qwen3.6-35b-a3b)

- [Hugging Face](https://huggingface.co/Qwen/Qwen3.6-35B-A3B)

- [ModelScope](https://modelscope.cn/models/Qwen/Qwen3.6-35B-A3B)

- [摘要：Okay this one is insane. A new 18B frankenstein model was just released on @huggingface — Beats the new Qwen3.6-35B-A3B on a 44-test suite despite requiring 12GB VRAM instead of 24GB 🤯](summaries/摘要：Okay this one is insane. A new 18B frankenstein model was just released on @huggingface — Beats the new Qwen3.6-35B-A3B on a 44-test suite despite requiring 12GB VRAM instead of 24GB 🤯.md)（[原文](https://x.com/leftcurvedev_/status/2045449352827580602)）

## 关联概念

- [Qwopus-GLM-18B-Merged-GGUF](entities/Qwopus-GLM-18B-Merged-GGUF.md)

- [模型合并](concepts/模型合并.md)

- [Agentic Reasoning](concepts/Agentic Reasoning.md)

- [Ollama](entities/Ollama.md)

- [vLLM](entities/vLLM.md)

- [SGLang](entities/SGLang.md)

- [LM Studio](entities/LM Studio.md)
