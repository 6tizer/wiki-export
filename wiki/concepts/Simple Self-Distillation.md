---
title: Simple Self-Distillation
type: concept
tags:
- LLM
- Coding Agent
status: 审核中
confidence: high
last_compiled: '2026-04-12'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/da21c21f5f7a4af696ae1d46c106eaee
notion_id: da21c21f-5f7a-4af6-96ae-1d46c106eaee
---

## 定义

Simple Self-Distillation 是一种让模型用自身采样输出反过来做监督微调的后训练方法，目标是在不依赖 RL 或验证器的前提下提升代码生成表现。

## 关键要点

- 先采样，再直接 SFT，最后用单独调优的推理温度运行

- 不需要外部教师模型、奖励模型或代码执行反馈

- 代表代码模型后训练向“低资源高收益”的简单方案回摆

## 来源引用

- [原文链接](https://x.com/berryxia/status/2040570633042690194)｜《苹果研究院：三步自蒸馏，代码生成提升30%，不需要RL也不需要验证器》｜源文章：苹果研究院：三步自蒸馏，代码生成提升30%，不需要RL也不需要验证器
