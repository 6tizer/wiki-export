---
title: uAI-NEXUS-MedVLM
type: entity
tags:
- 多模态
- AI 产品
status: 草稿
confidence: high
last_compiled: '2026-04-28'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/92d78f174c7243cc8fadff5ffb76f1fb
notion_id: 92d78f17-4c72-43cc-8fad-ff5ffb76f1fb
---

## 定义

uAI-NEXUS-MedVLM（元智医疗视频理解大模型）是由联影智能发布的全球首个、规模最大的医疗视频理解领域大模型。该模型能够从空间、时间、语义三个维度理解真实临床医疗视频，覆盖腹腔镜、开放手术、机器人手术及护理操作等核心临床场景。

**别名**：元智医疗视频理解大模型

## 关键要点

- 基于 Qwen2.5-VL-7B 底座，采用 SFT + 强化学习（MedGRPO）两阶段训练

- 在 MedVidBench 全部 8 项任务中全面超越 GPT-5.4、Gemini-3.1 等通用大模型

- CVS（关键安全视野评估）准确率达 89.4%，是 GPT-5.4（16.4%）的近 50 倍

- 4B 小模型 + RL 配置下多数任务表现已超过 7B SFT 基线，证明训练方法论比堆参数更关键

- 相关研究成果被 CVPR 2026 收录

- 已完全开源（模型、代码、数据集）

## 档案信息

- **开发方**：联影智能（联影集团子公司）

- **论文**：MedGRPO: Multi-Task Reinforcement Learning for Heterogeneous Medical Video Understanding

- **论文链接**：[https://arxiv.org/pdf/2512.06581](https://arxiv.org/pdf/2512.06581)

- **项目主页**：[https://uii-ai.github.io/MedGRPO/](https://uii-ai.github.io/MedGRPO/)

- **开源仓库**：[https://github.com/UII-AI/MedGRPO-Code](https://github.com/UII-AI/MedGRPO-Code)

- **所属大模型体系**：uAI NEXUS 医疗大模型（文本、影像、视觉、语音、混合五大模型）

## 来源引用

- [摘要：让大模型理解真实医疗视频，全球首个开源技术方案来了！](summaries/摘要：让大模型理解真实医疗视频，全球首个开源技术方案来了！.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzA3MzI4MjgzMw%3D%3D&mid=2651030763&idx=1&sn=9c3e8e595c0f07a91388a3bb94a271ab&chksm=854fb7d136df13086ee1a41b12aa402ab1c7c4fce28d91dbf4f46dc0d1a0cc280c2f0dd9a785#rd)）
