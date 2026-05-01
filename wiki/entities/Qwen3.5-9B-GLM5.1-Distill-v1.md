---
title: Qwen3.5-9B-GLM5.1-Distill-v1
type: entity
tags: []
status: 审核中
confidence: medium
last_compiled: '2026-04-20'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/d9f387e4ba0f46019bd34b59598a9667
notion_id: d9f387e4-ba0f-4601-9bd3-4b59598a9667
---

## 定义

Qwen3.5-9B-GLM5.1-Distill-v1 是一个以 **Qwen3.5-9B** 为底座、使用 **GLM-5.1** 推理数据进行蒸馏得到的 9B 开源模型，主打更强的结构化推理能力与更低的本地运行门槛。

## 关键要点

- 基于 Qwen3.5-9B 继续训练，核心改进方向是推理结构与回答稳定性，而不是单纯扩大参数规模。

- 该模型同时提供 **GGUF** 版本与 **MLX** 版本，分别面向本地 GPU 推理和 Apple Silicon 设备。

- 帖子强调其可在 **8GB VRAM** 场景下运行，这通常与量化部署方式直接相关。

- 当前发布阶段更像“社区实验型增强模型”，性能宣传点明确，但系统基准仍待后续补充。

## 来源引用

- [摘要：quantization](summaries/摘要：quantization.md)（[原文](https://x.com/leftcurvedev_/status/2044700338817564814)）

## 关联概念

- [Qwen3.5](entities/Qwen3.5.md)

- [GLM-5.1](entities/GLM-5.1.md)

- [模型蒸馏](concepts/模型蒸馏.md)

- [GGUF](concepts/GGUF.md)

- [MLX 框架](entities/MLX 框架.md)

- [模型量化](concepts/模型量化.md)
