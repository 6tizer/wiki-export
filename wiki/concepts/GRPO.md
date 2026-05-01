---
title: GRPO
type: concept
tags:
- 训练/微调
status: 审核中
confidence: medium
last_compiled: '2026-04-26'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/1be96817a6634f57a7f79c29ac55dfd4
notion_id: 1be96817-a663-4f57-a7f7-9c29ac55dfd4
---

## 定义

GRPO 是一种用于强化学习优化的策略更新方法，在 Agent 场景中可用来根据过程奖励信号逐步调整模型行为。

## 关键要点

- 适合利用好坏反馈对策略进行渐进更新

- 常作为在线 RL 管线中的核心优化器之一

- 能把用户交互中的偏好反馈转成可训练目标

## 来源引用

- [摘要：OpenClaw-RL：让 AI Agent 在对话中自我进化](summaries/摘要：OpenClaw-RL：让 AI Agent 在对话中自我进化.md)｜X书签文章

- 《GrandCode：AI 首次在 Codeforces 现场赛中击败全部人类选手》｜X书签文章｜原文链接：[https://x.com/deep_reinforce/status/2039344412946284791](https://x.com/deep_reinforce/status/2039344412946284791)｜来源条目：[摘要：GrandCode：AI 首次在 Codeforces 现场赛中击败全部人类选手](summaries/摘要：GrandCode：AI 首次在 Codeforces 现场赛中击败全部人类选手.md)

- [摘要：让大模型理解真实医疗视频，全球首个开源技术方案来了！](summaries/摘要：让大模型理解真实医疗视频，全球首个开源技术方案来了！.md)｜MedGRPO 为 GRPO 在医疗视频理解领域的扩展，引入跨数据集奖励归一化和医学 LLM 评审

- [摘要：How top AI labs are building RL agents in 2026 (using Karpathy's system prompt learning idea)](summaries/摘要：How top AI labs are building RL agents in 2026 (using Karpathy's system prompt learning idea).md)（[原文](https://x.com/_avichawla/status/2049037299334472015)）｜详细阐述 GRPO 与 RULER 的配合，及从 PPO 四模型到 GRPO 双模型的简化过程

- [摘要：刚刚，DeepSeek最新成果，节前发布！](summaries/摘要：刚刚，DeepSeek最新成果，节前发布！.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzIyNjM2MzQyNg%3D%3D&mid=2247722411&idx=1&sn=bdec00adace587c9737956cd7554bdb4&chksm=e900cea0128d25e4398f9e439ce550cf8de63aabb709f43fd4040baeceb7cd184cf5104f51f7#rd)）｜GRPO 用于训练 Visual Primitives 的 box/point 专家模型
