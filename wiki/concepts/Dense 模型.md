---
title: Dense 模型
type: concept
tags:
- LLM
status: 审核中
confidence: high
last_compiled: '2026-04-23'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/296c5957d6194728922bccc89433f1a3
notion_id: 296c5957-d619-4728-922b-ccc89433f1a3
---

## 定义

Dense 模型指一次前向计算中大部分或全部参数都会参与激活的模型架构，相对 MoE 更强调推理路径稳定、部署简单与资源利用的可预期性。

## 关键要点

- 在相同能力目标下，Dense 模型通常更容易部署与调优

- 对本地推理、私有数据处理和稳定时延场景更友好

- 在 Coding Agent 场景中，实际价值不仅取决于基准分数，也取决于 IDE 循环里的延迟、吞吐与长任务稳定性

## 关联概念

- [Qwen3.6-27B](entities/Qwen3.6-27B.md)

- [Qwen3.6-35B-A3B](entities/Qwen3.6-35B-A3B.md)

- [MoE 架构](concepts/MoE 架构.md)

- [SWE-bench](concepts/SWE-bench.md)

- [Terminal-Bench 2.0](entities/Terminal-Bench 2.0.md)

- [Agentic Coding](concepts/Agentic Coding.md)

## 来源引用

- [摘要：With 3.6-27b release, the dense-over-MoE gap is shrinking, which is good for local AI as MoE like 35b-a3b are more friendly on low-budget GPU and support much longer context (256k full easily on 24gb](summaries/摘要：With 3.6-27b release, the dense-over-MoE gap is shrinking, which is good for local AI as MoE like 35b-a3b are more friendly on low-budget GPU and support much longer context (256k full easily on 24gb.md)（[原文](https://x.com/hxiao/status/2047004358500614152)）

- [摘要：Qwen3.6-27B](summaries/摘要：Qwen3.6-27B.md)（[原文](https://x.com/Alibaba_Qwen/status/2046939764428009914)）
