---
title: MoE 架构
type: concept
tags:
- LLM
status: 审核中
confidence: high
last_compiled: '2026-04-18'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/a9669a8629a347708a59fa2700716269
notion_id: a9669a86-29a3-4770-8a59-fa2700716269
---

## 定义

MoE（Mixture of Experts，混合专家）是一种模型架构，将参数分为多个「专家」模块，每次推理时只激活与当前输入最相关的少数专家，实现大参数量但低计算成本的高效推理。

## 核心要点

- 条件计算：不是每次都使用所有参数，而是通过路由机制选择最适合的专家

- 效率优势：总参数量大但激活参数少，如 Qwen3.5 的 397B/17B（总参/激活）

- 与线性注意力结合：Qwen3.5 使用 MoE + 线性注意力混合架构，进一步提升效率

- 吞吐量提升：在长上下文场景下优势明显，Qwen3.5 解码速度是密集模型的 7-19 倍

- 本地部署可行性：激活参数少使本地部署成为可能

## 来源引用

- [原文链接](https://x.com/googlegemma/status/2042310203845329311)｜《Gemma 4：Google 开源多模态新旗舰，逐字节的智能突破》｜来源条目：[摘要：Gemma 4：Google 开源多模态新旗舰，逐字节的智能突破](summaries/摘要：Gemma 4：Google 开源多模态新旗舰，逐字节的智能突破.md)

- 摘要：Qwen3.5 开源多模态大模型（开源星探，2026-02-17）

- 《OpenClaw杀出中国黑马》（新智元，2026-02-28）：Step 3.5 Flash 采用约 196B MoE 架构，4-bit 量化后完美适配 128GB 内存，团队刻意将尺寸控制在 128GB 甜点位内

- [原文链接](https://x.com/Alibaba_Qwen/status/2044768734234243427)｜《⚡ Meet Qwen3.6-35B-A3B：Now Open-Source！🚀🚀》｜源文章：Qwen3.6-35B-A3B：用3B的算力跑35B的智慧，阿里最强开源编程模型来了
