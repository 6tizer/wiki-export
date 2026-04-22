---
title: LoRA 微调
type: concept
tags:
- 训练/微调
status: 草稿
confidence: medium
last_compiled: '2026-04-21'
source_tags: ''
source_article_url: ''
notion_url: https://www.notion.so/55a03a82154142cbbc07f89b939c3af5
notion_id: 55a03a82-1541-42cb-bc07-f89b939c3af5
---

## 定义

LoRA 微调是一种参数高效微调方法，通过为预训练模型附加低秩更新矩阵，用较低训练成本让模型快速适配新任务或新领域。

## 核心要点

- 不需要全量更新模型参数，显著降低显存与训练成本。

- 常用于开源模型的轻量适配、行业定制与能力验证。

- 当官方仓库提供 LoRA 微调示例时，通常意味着项目已经开始考虑真实开发者的二次训练需求。

## 来源引用

- [摘要：😱 谷歌偷偷开源了时序预测底座TimesFM 2.5，参数降到200M，上下文飙到16k。](summaries/摘要：😱 谷歌偷偷开源了时序预测底座TimesFM 2.5，参数降到200M，上下文飙到16k。.md)（[原文](https://x.com/oragnes/status/2046130320316207431)）
