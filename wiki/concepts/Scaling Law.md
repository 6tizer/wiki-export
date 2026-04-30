---
title: Scaling Law
type: concept
tags:
- 训练/微调
status: 草稿
confidence: high
last_compiled: '2026-04-30'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/e52a540617bf4d0384e4bc0d37a4d5a7
notion_id: e52a5406-17bf-4d03-84e4-bc0d37a4d5a7
---

## 定义

Scaling Law（缩放定律）指大型语言模型的性能随模型参数量、训练数据量和计算量的增大而可预测地提升的经验规律。由 Kaplan et al.（2020）系统提出，是当前 LLM 研发的核心指导原则之一。

## 关键要点

- 模型性能（以 loss 衡量）与参数量、数据量、计算预算之间存在幂律关系

- 三个关键变量中，通常计算预算是最终瓶颈

- Chinchilla 研究（Hoffmann et al., 2022）修正了早期的缩放策略，强调数据量与参数量应等比例扩展

- talkie 项目证实：即使训练数据仅限于 1931 年前的文本，Scaling Law 依然成立——模型规模越大，解出编程题的能力越强

- Scaling Law 的适用范围可能超越训练数据分布本身，暗示模型学到的是更基础的语言结构和推理能力

## 关联概念

- [talkie](entities/talkie.md)

- [Alec Radford](entities/Alec Radford.md)

## 来源引用

- [摘要：GPT之父：只用上世纪数据训AI，它居然也会写Python？！](summaries/摘要：GPT之父：只用上世纪数据训AI，它居然也会写Python？！.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzIzNjc1NzUzMw%3D%3D&mid=2247887945&idx=1&sn=4ae7aef7f33377a3b2bda14bc320f454&chksm=e9fe95de1c4f7605027c82909abd4a6e791ed37aa6ba23b5e165b4402f416faa98811d2c6bcc#rd)）
