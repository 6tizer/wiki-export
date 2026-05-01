---
title: 摘要：Defining Continual Learning
type: summary
tags:
- 训练/微调
- 模型评测
- Harness 工程
status: 已审核
confidence: high
last_compiled: '2026-04-23'
source_tags: ''
source_article_url: https://www.notion.so/34b701074b6881779892e6e3ed20ea2a
notion_url: https://www.notion.so/Tizer/c57ff4b784d646fa90f46f1f5643fa35
notion_id: c57ff4b7-84d6-46fa-90f4-6f1f5643fa35
---

## 一句话摘要

这篇文章主张，大语言模型的持续学习不应只被定义为“避免遗忘”，而应被定义为：在顺序接触分布不同的新数据时，能够高效地、可组合地学到新能力，同时尽量保持原有通用能力。

## 关键洞察

- 持续学习的核心不只是解决灾难性遗忘，而是建立一套更完整的能力标准：保留通用能力、适应顺序学习、处理分布迁移、强调效率、支持能力组合。

- 文章强调，传统多任务联合训练通过同批次混合数据来避免干扰，而真实世界中的在线学习却要求模型在时间上分批吸收新知识，这才是持续学习真正困难的地方。

- 作者认为，仅靠外部 harness、RAG 或技能文件虽然能临时补足知识，但难以在规模扩大后持续提升“每次前向推理的内在智能密度”，因此仍应重视权重内的参数化持续学习。

- 文中将 class-incremental learning 视为持续学习的重要检验标准：模型不仅要记住先后学到的能力，还要能把不同阶段获得的能力重新组合起来。

- 在开放问题上，作者指出 scaffold training、知识覆盖冲突、数据效率与合成数据质量，都是持续学习从理念走向可用系统前必须回答的问题。

## 提取的概念

- [Continual Learning](concepts/Continual Learning.md)

- [灾难性遗忘](concepts/灾难性遗忘.md)

- [Class-Incremental Learning](concepts/Class-Incremental Learning.md)

- [参数化持续学习](concepts/参数化持续学习.md)

- [Harness Engineering](concepts/Harness Engineering.md)

## 原始文章信息

- 作者：@carnot_cyclist

- 来源：X书签

- 发布时间：2026-04-07

- 原文链接：[X 原文](https://x.com/carnot_cyclist/status/2041479655035679163)

- 源页面：LLM 的持续学习：为什么我们还没解决这个问题，以及解法应该长什么样

## 个人评注

这篇文章对 Tizer 当前的知识编译与 Agent 设计很有启发：它把“外部记忆/工作流编排”与“权重内学习”明确区分开来。对 OpenClaw、HITL 和内容流水线而言，Harness Engineering 依然是短期最可落地的能力放大器，但如果未来希望系统真正把长期经验沉淀成更稳定的能力结构，那么持续学习的评估框架、能力组合性与数据效率问题都值得持续跟踪。
