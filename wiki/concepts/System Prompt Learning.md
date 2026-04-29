---
title: System Prompt Learning
type: concept
tags:
- 训练/微调
- 提示工程
status: 草稿
confidence: medium
last_compiled: '2026-04-29'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/82af1c3d6a6041d7a7b70446e0ec0a64
notion_id: 82af1c3d-6a60-41d7-a7b7-0446e0ec0a64
---

## 定义

System Prompt Learning 是 Andrej Karpathy 于 2025 年提出的学习范式概念，核心观点是：system prompt 携带的信号比标量 reward 更丰富，RL 训练应该找到方法直接利用 system prompt 中的指令作为奖励信号，而非依赖手工编写的 reward function。

别名：系统提示学习

## 关键要点

- Karpathy 认为 LLM 缺少一种重要的学习范式——能从 system prompt 的自然语言指令中直接学习行为偏好

- 传统 RLHF 依赖人类标注或手写 reward，无法扩展到所有 agentic 场景

- System Prompt Learning 的理念催生了 RULER 等工具：让 LLM judge 阅读 system prompt 后对输出打分，间接实现「从 system prompt 学习」

- Anthropic 的 Constitutional AI（宪法 AI）可视为该方向的早期实践——用一组写下的原则替代人类评估者

- OpenAI 的 Universal Verifiers 也在探索类似方向——将 RL 从可验证领域扩展到通用领域

## 与相关概念的关系

- 是 RULER 的理论动机：RULER 将 system prompt 当作隐式 reward function

- 与 Constitutional AI 共享核心思路：用文档化的规则替代人类 in-the-loop

- 可视为 RLHF → RLVR → 下一代范式的演进方向

## 来源引用

- [摘要：How top AI labs are building RL agents in 2026 (using Karpathy's system prompt learning idea)](summaries/摘要：How top AI labs are building RL agents in 2026 (using Karpathy's system prompt learning idea).md)（[原文](https://x.com/_avichawla/status/2049037299334472015)）
