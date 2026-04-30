---
title: CFG+DMD 蒸馏
type: concept
tags:
- LLM
- 推理优化
status: 审核中
confidence: high
last_compiled: '2026-04-23'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/f75b68b884a0441885e4b9004eea4e4b
notion_id: f75b68b8-84a0-4418-85e4-b9004eea4e4b
---

## 定义

CFG+DMD 蒸馏是 Avatar V 在后训练阶段采用的两阶段蒸馏策略，用于在保持生成质量的同时显著提升推理速度。

## 关键要点

- 属于模型可部署化过程中的速度优化手段。

- 文中将其作为 10× inference speedup 的关键组成之一。

- 说明视频生成产品的竞争力不仅取决于质量，也取决于蒸馏后的成本与时延表现。

## 来源引用

- [摘要：Avatar V: The End of Avatar Drift](summaries/摘要：Avatar V- The End of Avatar Drift.md)（[原文](https://x.com/joshua_xu_/status/2047099908281499803)）
