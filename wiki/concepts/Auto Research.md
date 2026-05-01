---
title: Auto Research
type: concept
tags:
- 模型评测
- 代码生成
status: 草稿
confidence: high
last_compiled: '2026-04-27'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/08798b9a3330422293617b986e03d881
notion_id: 08798b9a-3330-4222-9361-7b986e03d881
---

## 定义

Auto Research（自动化科研）是指利用大语言模型（LLM）端到端地完成科研全流程的方法论，包括 idea 生成、实验设计与执行、论文撰写与审稿。目标是让 AI 智能体独立完成从选题到成稿的完整研究周期，无需人类介入。

## 关键要点

- 典型流程分三阶段：idea 生成 → 实验执行 → 论文写作，每阶段可自我迭代

- 代表系统包括 Karpathy 的 autoresearch、日行迹的 FARS、以及直接使用 Claude Code 的轻量方案

- 当前主要瓶颈在实验设计与代码执行环节，LLM 的 self-review 在此阶段往往失效

- 评测显示 Auto Research 生成的论文尚无法达到顶会水平，与人类论文差距明显

- 更强算力（如 H100）并不能弥补实验逻辑与规划上的短板

## 来源引用

- [摘要：200刀打败18万美元FARS，我们离真正的Auto Research还有多远？](summaries/摘要：200刀打败18万美元FARS，我们离真正的Auto Research还有多远？.md)（[原文](https://mp.weixin.qq.com/s?__biz=MzIwMTc4ODE0Mw%3D%3D&mid=2247719869&idx=1&sn=286785641a7ed52f6a793ada026e99b7&chksm=97fd86517cd8ac029041769d3854be3aa40b9cfb029f9227e4c44dddc772f6182f320b544355#rd)）

## 关联概念

- [FARS](entities/FARS.md)

- [autoresearch](entities/autoresearch.md)

- [Stanford Agentic Reviewer](entities/Stanford Agentic Reviewer.md)

- [Agentic Review 偏差](concepts/Agentic Review 偏差.md)

- [Claude Code](entities/Claude Code.md)
