---
title: Qwen3.6-27B
type: entity
tags:
- LLM
- Coding Agent
status: 草稿
confidence: high
last_compiled: '2026-04-23'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/502b925a80be4c509d9349fc12b2d631
notion_id: 502b925a-80be-4c50-9d93-49fc12b2d631
---

## 定义

Qwen3.6-27B 是阿里通义千问发布的 27B 参数稠密开源模型，主打旗舰级 Agentic Coding，支持文本、图像、视频等多模态输入，并提供思考/非思考双模式与更适合长任务的 Thinking Preservation 能力。

## 关键要点

- 以 27B 体量强调高阶编码表现，突出“小模型高产出”的路线

- 官方表述称其在主要 coding benchmark 上超过 Qwen3.5-397B-A17B

- 采用 Apache 2.0 许可，便于本地部署、二次开发与商业使用

- 支持 262K 上下文窗口，并兼顾文本、多模态推理与本地部署场景

- 社区讨论集中在本地运行可行性、长任务链稳定性与 IDE/agent 工作流适配

## 关联概念

- [Agentic Coding](concepts/Agentic Coding.md)

- [思考/非思考双模式](concepts/思考-非思考双模式.md)

- [多模态推理](concepts/多模态推理.md)

- [Dense 模型](concepts/Dense 模型.md)

- [MoE 架构](concepts/MoE 架构.md)

- [Qwen3.6-35B-A3B](entities/Qwen3.6-35B-A3B.md)

- [SWE-bench](concepts/SWE-bench.md)

- [Terminal-Bench 2.0](entities/Terminal-Bench 2.0.md)

- [Thinking Preservation](concepts/Thinking Preservation.md)

- [DFlash](concepts/DFlash.md)

- [DDTree](concepts/DDTree.md)

- [vLLM](entities/vLLM.md)

- [Speculative Decoding](concepts/Speculative Decoding.md)

## 来源引用

- [摘要：With 3.6-27b release, the dense-over-MoE gap is shrinking, which is good for local AI as MoE like 35b-a3b are more friendly on low-budget GPU and support much longer context (256k full easily on 24gb](summaries/摘要：With 3.6-27b release, the dense-over-MoE gap is shrinking, which is good for local AI as MoE like 35b-a3b are more friendly on low-budget GPU and support much longer context (256k full easily on 24gb.md)（[原文](https://x.com/hxiao/status/2047004358500614152)）

- [摘要：Qwen3.6-27B](summaries/摘要：Qwen3.6-27B.md)（[原文](https://x.com/Alibaba_Qwen/status/2046939764428009914)）

- [摘要：Worklanes, not just tabs.](summaries/摘要：Worklanes, not just tabs.md)（[原文](https://x.com/iotcoi/status/2046950805568164168)）

- [摘要：Qwen 3.6 27B model is available on Ollama!](summaries/摘要：Qwen 3.6 27B model is available on Ollama!.md)（[原文](https://x.com/ollama/status/2047066252523507916)）
