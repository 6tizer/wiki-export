---
title: Laguna XS.2
type: entity
tags:
- 代码生成
- 模型部署
status: 草稿
confidence: high
last_compiled: '2026-04-29'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/35d7f6c8d4b14bc58a3f429d9e27adb1
notion_id: 35d7f6c8-d4b1-4bc5-8a3f-429d9e27adb1
---

## 定义

Laguna XS.2 是 Poolside 发布的首个开源权重编码模型，采用 33B 总参数 / 3B 激活参数的 MoE（Mixture of Experts）架构，专为 agentic coding 和长时域任务设计。使用 Apache 2.0 许可证开源，可在单块 GPU 上运行。

别名：Laguna XS 系列第二代

## 关键要点

- **架构**：MoE 模型，33B 总参数，每 token 激活 3B 参数，40 层（10 层全局注意力 + 30 层滑动窗口注意力），256 个专家 + 1 个共享专家

- **注意力机制**：使用 Sliding Window Attention（SWA）配合 per-head sigmoid gating 和 per-layer rotary scales，3:1 SWA/全局注意力比例

- **KV Cache**：量化至 FP8，降低每 token 内存占用

- **训练**：在 30 万亿 token 上预训练，使用 Muon 优化器，经历预训练、后训练和 Agent RL 三阶段

- **推理能力**：原生支持交织思考（interleaved thinking），可在工具调用间穿插推理

- **上下文窗口**：128K tokens

- **基准表现**：在 SWE-bench Pro、SWE-bench Verified、SWE-bench Multilingual 上表现出色，XS 级别模型中达到 62% SWE-bench Multilingual

- **部署支持**：首日支持 Transformers、vLLM、TRT-LLM、MLX/mlx-lm、Ollama

- **同系列**：Laguna M.1 为旗舰模型，XS.2 的训练经验来自 M.1

## 来源引用

- [摘要：Today we're releasing Laguna XS.2, Poolside's first open-weight model.](summaries/摘要：Today we're releasing Laguna XS.2, Poolside's first open-weight model.md)（[原文](https://x.com/poolsideai/status/2049144111626670282)）

## 关联概念

- [Poolside](entities/Poolside.md)

- [Agent RL](concepts/Agent RL.md)

- [Data Automixing](concepts/Data Automixing.md)

- [Shimmer](entities/Shimmer.md)
