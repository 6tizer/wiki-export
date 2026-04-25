---
title: Qwen3.6-35B-A3B
type: entity
tags:
- Coding Agent
- 多模态
- 模型部署
- AI 产品
status: 审核中
confidence: high
last_compiled: '2026-04-25'
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

- [摘要：With 3.6-27b release, the dense-over-MoE gap is shrinking, which is good for local AI as MoE like 35b-a3b are more friendly on low-budget GPU and support much longer context (256k full easily on 24gb](summaries/摘要：With 3.6-27b release, the dense-over-MoE gap is shrinking, which is good for local AI as MoE like 35b-a3b are more friendly on low-budget GPU and support much longer context (256k full easily on 24gb.md)（[原文](https://x.com/hxiao/status/2047004358500614152)）

- [摘要：ThinkInAI Weekly AI周刊 VOL.42 Opus 4.7 来了、Qwen 开源 35B、Agent 工具链全面升级](summaries/摘要：ThinkInAI Weekly AI周刊 VOL.42 Opus 4.7 来了、Qwen 开源 35B、Agent 工具链全面升级.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzA4ODg0NDkzOA%3D%3D&mid=2247514009&idx=1&sn=bf15a5a46c8fceb7d84d0b3760d4ade9&chksm=91d6d8d58aad639487948529ced9d124bf6b7e77e01022df6a25570b93843ec362146982cbe9#rd)）

- [摘要：Qwen3.6 35B-A3B dropped yesterday, so I ran it on 4 GPUs to see how it performs:](summaries/摘要：Qwen3.6 35B-A3B dropped yesterday, so I ran it on 4 GPUs to see how it performs-.md)（[原文](https://x.com/stevibe/status/2045087373516492954)）

- [原文链接](https://x.com/Alibaba_Qwen/status/2044768734234243427)｜《⚡ Meet Qwen3.6-35B-A3B：Now Open-Source！🚀🚀》｜源文章：Qwen3.6-35B-A3B：用3B的算力跑35B的智慧，阿里最强开源编程模型来了

- [官方博客](https://qwen.ai/blog?id=qwen3.6-35b-a3b)

- [Hugging Face](https://huggingface.co/Qwen/Qwen3.6-35B-A3B)

- [ModelScope](https://modelscope.cn/models/Qwen/Qwen3.6-35B-A3B)

- [摘要：Okay this one is insane. A new 18B frankenstein model was just released on @huggingface — Beats the new Qwen3.6-35B-A3B on a 44-test suite despite requiring 12GB VRAM instead of 24GB 🤯](summaries/摘要：Okay this one is insane. A new 18B frankenstein model was just released on @huggingface — Beats the new Qwen3.6-35B-A3B on a 44-test suite despite requiring 12GB VRAM instead of 24GB 🤯.md)（[原文](https://x.com/leftcurvedev_/status/2045449352827580602)）

- [摘要：3B的成本，35B的智力：Qwen 3.6 正在暴力拆解 AI 商业化的成本围墙](summaries/摘要：3B的成本，35B的智力：Qwen 3.6 正在暴力拆解 AI 商业化的成本围墙.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzU4OTY4MDU4MQ%3D%3D&mid=2247490900&idx=1&sn=823e360812006af69f9c2e01cf2d3601&chksm=fc955696662d95b68a7dfab13245552377720ba90794116217337957a434e9e8544f71d19a9d#rd)）

- [摘要：都是你能部署的：Qwen3.6和Gemma4，谁更适合作为你的下一代本地MoE模型？](summaries/摘要：都是你能部署的：Qwen3.6和Gemma4，谁更适合作为你的下一代本地MoE模型？.md)（[原文](https://mp.weixin.qq.com/s?__biz=Mzg4MzYxODkzMg%3D%3D&mid=2247508057&idx=1&sn=623ac3d5cea6bb2fb7f65d8b28514e75&chksm=ce0870dc9fc80dacdba48c8c3e27ae39f6c6bb655f67fa6a631ff7b3946e041f012431b96de8#rd)）

## 关联概念

- [MoE 架构](concepts/MoE 架构.md)

- [Dense 模型](concepts/Dense 模型.md)

- [Qwen3.6-27B](entities/Qwen3.6-27B.md)

- [Thinking Preservation](concepts/Thinking Preservation.md)

- [Agentic Coding](concepts/Agentic Coding.md)

- [SWE-bench](concepts/SWE-bench.md)

- [Terminal-Bench 2.0](entities/Terminal-Bench 2.0.md)

- [Gemma4-26B-A4B](entities/Gemma4-26B-A4B.md)

- [Qwen3.5-27B](entities/Qwen3.5-27B.md)

- [Qwopus-GLM-18B-Merged-GGUF](entities/Qwopus-GLM-18B-Merged-GGUF.md)

- [模型合并](concepts/模型合并.md)

- [Agentic Reasoning](concepts/Agentic Reasoning.md)

- [Ollama](entities/Ollama.md)

- [vLLM](entities/vLLM.md)

- [SGLang](entities/SGLang.md)

- [LM Studio](entities/LM Studio.md)

- [Agentic Workflow](concepts/Agentic Workflow.md)

- [自托管](concepts/自托管.md)
