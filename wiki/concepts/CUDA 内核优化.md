---
title: CUDA 内核优化
type: concept
tags:
- 开发工具
- Coding Agent
status: 草稿
confidence: high
last_compiled: '2026-04-15'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/1f24e3e2e8094ec18021b6e59d0f91c9
notion_id: 1f24e3e2-e809-4ec1-8021-b6e59d0f91c9
---

## 定义

CUDA 内核优化是围绕 GPU 计算核心代码进行性能调优的工程过程，目标是在具体硬件约束下提升吞吐、降低延迟并改善能效。在本文里，它被用来检验多智能体系统是否能胜任传统上高度依赖专家经验的低层软件优化任务。

## 关键要点

- 这类问题具有明确可测的目标，非常适合作为多轮搜索与评测闭环的任务载体

- 优化不仅涉及算子本身，还涉及指令选择、调度、内存访问与问题规模适配

- 文中结果表明，多智能体系统已经能在部分真实 CUDA 问题上逼近甚至超过人工优化基线

## 关联概念

- [Agent Harness](concepts/Agent Harness.md)

- [Cursor](entities/Cursor.md)

## 来源引用

- [原文链接](https://cursor.com/blog/multi-agent-kernels)｜《Speeding up GPU kernels by 38% with a multi-agent system》｜源文章：Cursor × NVIDIA：多智能体系统用 3 周把 CUDA kernel 加速了 38%
