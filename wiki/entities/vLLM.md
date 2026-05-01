---
title: vLLM
type: entity
tags: []
status: 审核中
confidence: high
last_compiled: '2026-04-27'
source_tags: LLM, Agent, 开发者工具
source_article_url: ''
notion_url: https://www.notion.so/Tizer/e0e3be7d69c4408bb2714a2630763a10
notion_id: e0e3be7d-69c4-408b-b271-4a2630763a10
---

## 定义

vLLM 是面向大语言模型推理服务的高性能部署框架，强调吞吐优化、统一 OpenAI 兼容接口与多模型生产化部署能力。

## 关键要点

- 适合用 `/v1/chat/completions` 这类标准接口承接上层 Agent 或应用

- 在工具调用场景里，消息格式、chat template 与服务端协议兼容性会直接影响结果正确性

- 本文案例里，vLLM 会把 tool message 的纯文本内容转换为结构化 array parts，进而暴露出模板兼容问题

## 来源引用

- [摘要：Qwen3.6 35B-A3B dropped yesterday, so I ran it on 4 GPUs to see how it performs:](summaries/摘要：Qwen3.6 35B-A3B dropped yesterday, so I ran it on 4 GPUs to see how it performs-.md)（[原文](https://x.com/stevibe/status/2045087373516492954)）

- [原文链接](https://x.com/Zai_org/status/2044741938604093443)｜《GLM-5.1 的 Tool Calling 循环死锁：一个 Chat Template 引发的「幽灵 Bug」》｜源文章：GLM-5.1 的 Tool Calling 循环死锁：一个 Chat Template 引发的「幽灵 Bug」

- [摘要：Worklanes, not just tabs.](summaries/摘要：Worklanes, not just tabs.md)（[原文](https://x.com/iotcoi/status/2046950805568164168)）

- [摘要：Apple Silicon 上的 vLLM 终于原生 Swift/Metal 了！](summaries/摘要：Apple Silicon 上的 vLLM 终于原生 Swift-Metal 了！.md)（[原文](https://x.com/berryxia/status/2047523226272862372)）

- [摘要：Recipes for serving LLMs locally on RTX 3090s.](summaries/摘要：Recipes for serving LLMs locally on RTX 3090s.md)（[原文](https://x.com/Alibaba_Qwen/status/2049462758211772663)）

## 关联概念

- [Qwen3.6-35B-A3B](entities/Qwen3.6-35B-A3B.md)

- [GLM-5.1](entities/GLM-5.1.md)

- [Tool Calling](concepts/Tool Calling.md)

- [Qwen3.6-27B](entities/Qwen3.6-27B.md)

- [DFlash](concepts/DFlash.md)

- [DDTree](concepts/DDTree.md)

- [Speculative Decoding](concepts/Speculative Decoding.md)

- [vllm-swift](entities/vllm-swift.md)
