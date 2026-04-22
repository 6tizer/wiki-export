---
title: CrystalBLEU
type: concept
tags:
- LLM
status: 草稿
confidence: medium
last_compiled: '2026-04-19'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/bf600e1c4e1c4cea8da6db64a003f069
notion_id: bf600e1c-4e1c-4cea-8da6-db64a003f069
---

## 定义

CrystalBLEU 是一种改造后的 BLEU 指标，通过压制语料中高频模板 n-gram 的影响，更准确地衡量代码或结构化文本里的真实语义匹配程度。

## 关键要点

- 它适合 LaTeX、代码等模板噪声很重的文本场景。

- 相比普通 BLEU，它更少被固定样板语法“作弊”。

- 在图表转 TikZ 任务里，它能更有效反映核心绘图逻辑是否一致。

## 来源引用

- [摘要：技术动态 | OpenClaw带火的大量Skill如何做RAG？一项实验报告及学科图表转LaTeXcode强化学习思路](summaries/摘要：技术动态  OpenClaw带火的大量Skill如何做RAG？一项实验报告及学科图表转LaTeXcode强化学习思路.md)
