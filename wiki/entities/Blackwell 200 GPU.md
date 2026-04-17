---
title: Blackwell 200 GPU
type: entity
tags:
- 商业/生态
status: 草稿
confidence: high
last_compiled: '2026-04-15'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/a0fe0545f9a6484bb4079a4136df31f5
notion_id: a0fe0545-f9a6-484b-b407-9a4136df31f5
---

## 定义

Blackwell 200 GPU 是 NVIDIA 面向高性能 AI 训练与推理场景的 Blackwell 架构硬件平台。在这篇文章里，它是多智能体系统进行 CUDA 内核优化与性能评测的目标硬件。

## 关键要点

- 文中的 235 个优化问题都围绕 Blackwell 200 GPU 的真实工作负载展开

- 文章强调 agent 能从零开始学习面向 Blackwell 的优化策略，而不是只复用现成模板

- Blackwell 的硬件特性决定了指令级优化、调度策略与内存访问方式都要重新适配

## 关联概念

- [Cursor](entities/Cursor.md)

- [Agent Harness](concepts/Agent Harness.md)

## 来源引用

- [原文链接](https://cursor.com/blog/multi-agent-kernels)｜《Speeding up GPU kernels by 38% with a multi-agent system》｜源文章：Cursor × NVIDIA：多智能体系统用 3 周把 CUDA kernel 加速了 38%
