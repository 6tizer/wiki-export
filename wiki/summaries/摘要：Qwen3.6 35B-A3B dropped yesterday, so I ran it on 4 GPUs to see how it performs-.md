---
title: '摘要：Qwen3.6 35B-A3B dropped yesterday, so I ran it on 4 GPUs to see how it
  performs:'
type: summary
tags:
- LLM
- 开发工具
status: 已审核
confidence: medium
last_compiled: '2026-04-20'
source_tags: ''
source_article_url: https://www.notion.so/348701074b68812e95f2de552718912d
notion_url: https://www.notion.so/73c5e0d0e817431fbfbda94727c38824
notion_id: 73c5e0d0-e817-431f-bfbd-a94727c38824
---

## 一句话摘要

这篇实测用统一的 Q4_K_M 量化和 Ollama 后端，对 Qwen3.6-35B-A3B 在 4 种硬件上的“开箱即用”本地推理体验做了横向对比，结果显示 RTX 5090 吞吐最高，而 DGX Spark 的首 token 延迟最短。

## 关键洞察

- 作者刻意统一使用 Q4_K_M 量化，以避免因为只有部分硬件支持 NVFP4 而让对比失真。

- 在这组结果里，RTX 5090 的生成速度最高，RTX 4090 次之，RTX 3090 与 DGX Spark 更接近，但 DGX Spark 的 TTFT 更有优势。

- 这次测试强调的是“普通用户今晚就能复现”的默认体验，因此优先选择了 Ollama，而不是更激进的高性能推理栈。

- 回复区大量反馈表明，换用 vLLM、SGLang、llama.cpp 或 LM Studio 后，吞吐还有明显上探空间，说明后端选择会显著改变结论。

- 对本地 Agent 或内容流水线来说，这篇实测提醒我们：评估模型部署方案时，不能只看 tok/s，还要同时看易用性、TTFT 与量化兼容性。

## 提取的概念

- [Qwen3.6-35B-A3B](entities/Qwen3.6-35B-A3B.md)

- [Ollama](entities/Ollama.md)

- [vLLM](entities/vLLM.md)

- [SGLang](entities/SGLang.md)

- [LM Studio](entities/LM Studio.md)

## 原始文章信息

- 作者：@stevibe

- 来源：X书签

- 发布时间：2026-04-17

- 原文链接：[https://x.com/stevibe/status/2045087373516492954](https://x.com/stevibe/status/2045087373516492954)

## 个人评注

这类对比对 Tizer 的工作流很有参考价值：如果目标是快速搭建本地知识处理或 Agent 原型，Ollama 代表的是最低门槛路径；但如果后续要支撑更高并发、更长上下文或更稳定的生产化推理，就需要尽早把 vLLM / SGLang 这类高性能后端纳入评估，并把硬件吞吐、首 token 延迟与量化兼容性拆开看。
