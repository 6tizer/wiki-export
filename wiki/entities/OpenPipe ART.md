---
title: OpenPipe ART
type: entity
tags:
- 训练/微调
- AI 产品
status: 草稿
confidence: high
last_compiled: '2026-04-29'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/2b49104d688041c0b901a18103a86fb8
notion_id: 2b49104d-6880-41c0-b901-a18103a86fb8
---

## 定义

OpenPipe ART（Agent Reinforcement Training）是 OpenPipe 开源的 Agent RL 训练框架（GitHub: OpenPipe/ART，9k+ stars），提供从轨迹采集、RULER 评分到 GRPO 训练的端到端 pipeline，让开发者无需手写 reward function 即可对 Agent 进行强化学习微调。

## 档案

- **类型**：开源框架

- **GitHub**：[https://github.com/OpenPipe/ART](https://github.com/OpenPipe/ART)

- **许可证**：待确认

- **Stars**：9,000+

## 核心组件

- **Trajectory / TrajectoryGroup**：封装 Agent 交互历史（system + user + assistant messages），作为训练和评分的基本单元

- **RULER**：内置的 LLM-as-judge 奖励函数，支持相对排名打分

- **gather_trajectory_groups**：编排轨迹采集与评分的异步函数

- **model.train()**：基于 GRPO 的 LoRA 权重更新

## 典型训练循环

1. 为每个 scenario 生成 4-8 条轨迹（rollout）

1. RULER 对每组轨迹做相对评分

1. GRPO 根据组内归一化后的 advantage 更新 LoRA 权重

1. 重复至收敛

## 关键要点

- 将 RLHF 的四模型架构（policy + reference + reward model + critic）简化为接近单模型

- 支持 OpenAI SDK 标准类型，可直接复用已有推理代码

- 内置 Colab notebook 用于端到端训练演示

## 来源引用

- [摘要：How top AI labs are building RL agents in 2026 (using Karpathy's system prompt learning idea)](summaries/摘要：How top AI labs are building RL agents in 2026 (using Karpathy's system prompt learning idea).md)（[原文](https://x.com/_avichawla/status/2049037299334472015)）
