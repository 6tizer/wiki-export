---
title: Sparse Reference Attention
type: concept
tags:
- 内容创作
- 多模态
status: 审核中
confidence: high
last_compiled: '2026-04-23'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/Tizer/3d9ac69f30f442b9b5ee60cdc1bf9f68
notion_id: 3d9ac69f-30f4-42b9-b5ee-60cdc1bf9f68
---

## 定义

Sparse Reference Attention 是 Avatar V 使用的一种非对称注意力机制：生成 token 可以访问全部参考 token，而参考 token 只进行自注意力，从而把参考长度的计算复杂度压到近似线性。

## 关键要点

- 目标是在不牺牲身份检索能力的前提下扩展参考视频长度。

- 复杂度从包含参考间二次交互的形式，下降为对参考长度近似线性增长。

- 适合需要从长视频中持续提取身份、表情与动作线索的生成任务。

## 来源引用

- [摘要：Avatar V: The End of Avatar Drift](summaries/摘要：Avatar V- The End of Avatar Drift.md)（[原文](https://x.com/joshua_xu_/status/2047099908281499803)）
