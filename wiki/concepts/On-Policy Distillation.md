---
title: On-Policy Distillation
type: concept
tags:
- 训练/微调
status: 审核中
confidence: medium
last_compiled: '2026-05-03'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/55a9086eb2894243b0dc933e9e221bdb
notion_id: 55a9086e-b289-4243-b0dc-933e9e221bdb
---

## 定义

On-Policy Distillation 是一种把当前交互过程中的高质量纠正或示范直接蒸馏回模型策略的学习方式，用于提高在线纠偏效率。

## 关键要点

- 相比纯标量奖励，能提供更细粒度的教师信号

- 适合把用户明确纠正转成方向性训练数据

- 常与强化学习并行使用，形成组合式在线学习

## 来源引用

- [摘要：OpenClaw-RL：让 AI Agent 在对话中自我进化](summaries/摘要：OpenClaw-RL：让 AI Agent 在对话中自我进化.md)（X书签文章）

- [摘要：OpenClaw-RL：让你的本地 Agent 边聊边进化](summaries/摘要：OpenClaw-RL：让你的本地 Agent 边聊边进化.md)（[原文](https://x.com/RoundtableSpace/status/2031501603547787569)）

- [摘要：OpenClaw-RL：边用边训练，用对话驯化你的专属 AI Agent](summaries/摘要：OpenClaw-RL：边用边训练，用对话驯化你的专属 AI Agent.md)（[原文](https://x.com/Sumanth_077/status/2032459588390502566)）

- [摘要：刚刚，DeepSeek最新成果，节前发布！](summaries/摘要：刚刚，DeepSeek最新成果，节前发布！.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzIyNjM2MzQyNg%3D%3D&mid=2247722411&idx=1&sn=bdec00adace587c9737956cd7554bdb4&chksm=e900cea0128d25e4398f9e439ce550cf8de63aabb709f43fd4040baeceb7cd184cf5104f51f7#rd)）｜On-Policy Distillation 用于将 box/point 两个专家模型统一蒸馏

## 关联概念

- [OpenClaw-RL](entities/OpenClaw-RL.md)

- [Next-State Signal](concepts/Next-State Signal.md)

- [Binary RL](concepts/Binary RL.md)
