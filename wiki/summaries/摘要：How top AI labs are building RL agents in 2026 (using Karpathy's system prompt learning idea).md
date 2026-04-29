---
title: 摘要：How top AI labs are building RL agents in 2026 (using Karpathy's system
  prompt learning idea)
type: summary
tags:
- 训练/微调
- 模型评测
status: 已审核
confidence: high
last_compiled: '2026-04-29'
source_tags: ''
source_article_url: https://www.notion.so/351701074b6881dc80d4ea6cbef77834
notion_url: https://www.notion.so/Tizer/c9317dbdc375441da6e14757747493df
notion_id: c9317dbd-c375-441d-a6e1-4757747493df
---

## 一句话摘要

从 RLHF 到 RLVR 再到 RULER，本文完整梳理了强化学习应用于 LLM/Agent 训练的演进路线，展示了 AI 实验室如何将 Karpathy 的 System Prompt Learning 理念落地——用 system prompt 作为隐式 reward function，通过 LLM-as-judge 相对排名打分替代手写奖励函数，解决 agentic 任务无法自动评分的瓶颈。

## 关键洞察

- **RL 应用于 LLM 的核心瓶颈不是优化算法，而是奖励信号**：GRPO 已经足够好，但非可验证任务（RAG、客服、摘要）缺乏自动评分机制

- **RLHF → RLVR → RULER 的演进线**：RLHF 用人类偏好训练 reward model（四模型架构，昂贵）；RLVR 用规则验证器（数学/代码，二值奖励）+ GRPO 砍掉 critic 和 reward model；RULER 用 LLM judge 做相对排名，覆盖所有非可验证任务

- **相对评分是关键突破**：LLM 做绝对打分不稳定，但比较「哪条更好」非常可靠；RULER 利用这一特性，结合 GRPO 的组内归一化，产生有效的训练梯度

- **System Prompt 即 reward function**：judge 直接阅读 Agent 的 system prompt 理解评判标准，收紧 prompt 会自动收紧评分——无需修改任何代码

- **DeepSeek R1-Zero 的启示**：纯 RL 训练（GRPO + 二值奖励）让模型自发学会推理、自我验证和 chain-of-thought，AIME 2024 从 15.6% 飙升到 86.7%

## 提取的概念

- [RULER](concepts/RULER.md)

- [OpenPipe ART](entities/OpenPipe ART.md)

- [System Prompt Learning](concepts/System Prompt Learning.md)

- [RLHF](concepts/RLHF.md)

- [RLVR](concepts/RLVR.md)

- [GRPO](concepts/GRPO.md)

- [LLM-as-judge](concepts/LLM-as-judge.md)

## 原始文章信息

- **作者**：@_avichawla

- **来源**：X 书签

- **发布时间**：2026-04-28

- **原文链接**：[https://x.com/_avichawla/status/2049037299334472015](https://x.com/_avichawla/status/2049037299334472015)

## 个人评注

本文对 Tizer 的 OpenClaw 和 Agent 工作流有直接参考价值：

- **RULER 可用于 OpenClaw Agent 的行为评估**：如果 OpenClaw 的 Agent 需要做 RL 微调，RULER 提供了无需手写 reward 的评估方案

- **System Prompt 作为隐式训练目标**与 OpenClaw 的 [AGENTS.md](http://agents.md/) / [SKILL.md](http://skill.md/) 理念一脉相承——结构化指令既是运行时约束，也可以是训练信号

- **相对排名评分**可以借鉴到内容 pipeline 的质量评估环节——对比多条候选输出选最优，而非绝对打分
