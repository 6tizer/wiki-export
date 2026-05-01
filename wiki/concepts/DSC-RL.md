---
title: DSC-RL
type: concept
tags: []
status: 审核中
confidence: high
last_compiled: '2026-04-19'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/4bbdd0d9bde34fe89ecda902e675aeea
notion_id: 4bbdd0d9-bde3-4fe8-9ecd-a902e675aeea
---

## 定义

DSC-RL（Dual Self-Consistency Reinforcement Learning）是一种用于科学图表代码生成的强化学习训练思路，把视觉结果一致性与代码往返一致性同时作为优化目标。

## 关键要点

- 它先检查生成代码是否能编译并在视觉上还原原图。

- 再通过“图像→代码→图像→代码”的往返过程，检验生成代码在语义层面的稳定性。

- 这种做法把奖励从单一视觉相似扩展到执行正确性与代码一致性两条线。

## 来源引用

- [摘要：技术动态 | OpenClaw带火的大量Skill如何做RAG？一项实验报告及学科图表转LaTeXcode强化学习思路](summaries/摘要：技术动态  OpenClaw带火的大量Skill如何做RAG？一项实验报告及学科图表转LaTeXcode强化学习思路.md)
